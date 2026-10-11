#!/usr/bin/env python3
"""Check that this computer is ready for the VS Code + Copilot workshop.

Run from the workshop folder:
      python3 1_prerequisites/check_setup.py     (macOS/Linux)
      python 1_prerequisites/check_setup.py      (Windows)

Prints PASS / FAIL / WARN per check, then the exact Python command your
machine needs in .vscode/mcp.json. Makes no changes and sends no data.
"""
import json
import os
import platform
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PARTICIPANTS = os.path.join(ROOT, "2_participants")
FACILITATOR = os.path.join(ROOT, "3_facilitator")
IS_WIN = platform.system() == "Windows"
results = []


def report(status, name, fix=""):
    results.append(status)
    print(f"[{status}] {name}")
    if fix and status != "PASS":
        print(f"       -> {fix}")


def run(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return out.returncode, (out.stdout + out.stderr).strip()
    except Exception as e:  # missing binary, timeout
        return 1, str(e)


def python_command():
    """Return the command that runs Python 3 on this machine, or None."""
    for cmd in (["python3"], ["python"], ["py", "-3"]):
        if shutil.which(cmd[0]):
            code, out = run(cmd + ["--version"])
            if code == 0 and out.startswith("Python 3"):
                return cmd, out
    return None, ""


def main():
    print(f"Workshop setup check on {platform.system()} {platform.release()}\n")

    # 1. Python 3 (hooks and the MCP server need it)
    cmd, ver = python_command()
    if cmd:
        report("PASS", f"Python 3 found: {ver} (command: {' '.join(cmd)})")
    else:
        report("FAIL", "Python 3 not found",
               "Install from python.org (Windows: tick 'Add python.exe to PATH'). macOS: brew install python.")

    # 2. VS Code command-line launcher (optional but handy)
    if shutil.which("code"):
        code, out = run(["code", "--version"])
        first = out.splitlines()[0] if out else "?"
        report("PASS", f"VS Code launcher found, version {first}")
        print("       (use the latest stable VS Code: Help > Check for Updates)")
    else:
        report("WARN", "'code' command not on PATH (fine if VS Code is installed)",
               "VS Code: Command Palette > 'Shell Command: Install code command in PATH' (macOS).")

    # 3. Workshop files present
    needed = [
        "1_prerequisites/ATLASSIAN_SETUP.md",
        "1_prerequisites/PREREQUISITE_CREATE_CONFLUENCE_AND_JIRA.md",
        "1_prerequisites/atlassian_seed/content/jira_tickets.md",
        "1_prerequisites/atlassian_seed/content/pages/02_portal_reference_time_off_form.md",
        "1_prerequisites/atlassian_seed/screenshots/01_my_requests.png",
        "2_participants/brightside_workspace/source_material/02_policy_update.md",
        "2_participants/brightside_workspace/docs/how-to-request-time-off.md",
        "2_participants/solution/.github/copilot-instructions.md",
        "2_participants/solution/tools/doc_tools_server.py",
        "2_participants/plugin/brightside-docs-kit/.claude-plugin/plugin.json",
    ]
    missing = [p for p in needed if not os.path.isfile(os.path.join(ROOT, p))]
    if missing:
        report("FAIL", "Workshop files missing: " + ", ".join(missing), "Re-download the workshop folder.")
    else:
        report("PASS", "Workshop files present")

    # 4. The MCP server starts and answers
    server = os.path.join(PARTICIPANTS, "solution", "tools", "doc_tools_server.py")
    if cmd and os.path.isfile(server):
        msgs = "\n".join([
            json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}),
            json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}),
        ]) + "\n"
        try:
            out = subprocess.run(cmd + [server], input=msgs, capture_output=True, text=True, timeout=15)
            names = [t["name"] for t in json.loads(out.stdout.strip().splitlines()[-1])["result"]["tools"]]
            report("PASS", f"MCP server starts and lists {len(names)} tools")
        except Exception as e:
            report("FAIL", f"MCP server did not respond ({e})", "Check the Python install above.")

    # 5. Hooks run and block a bad page
    lint = os.path.join(PARTICIPANTS, "solution", ".github", "hooks", "lint_doc.py")
    if cmd and os.path.isfile(lint):
        bad = os.path.join(ROOT, "_setup_probe", "docs", "probe.md")
        os.makedirs(os.path.dirname(bad), exist_ok=True)
        try:
            with open(bad, "w", encoding="utf-8") as f:
                f.write("# How To Request Time Off\n")
            event = json.dumps({"cwd": os.path.dirname(os.path.dirname(bad)),
                                "tool_name": "create_file", "tool_input": {"filePath": bad}})
            out = subprocess.run(cmd + [lint], input=event, capture_output=True, text=True, timeout=15)
            if out.returncode == 2:
                report("PASS", "Lint hook blocks a Title Case heading (exit code 2)")
            else:
                report("FAIL", f"Lint hook returned {out.returncode}, expected 2", out.stderr.strip())
        finally:
            shutil.rmtree(os.path.join(ROOT, "_setup_probe"), ignore_errors=True)

    # 5b. Facilitator only: the Atlassian seed script and its content are complete (no network)
    seed = os.path.join(FACILITATOR, "seed_atlassian.py")
    if cmd and os.path.isfile(seed):
        out = subprocess.run(cmd + [seed, "--site", "x.atlassian.net", "--email", "a@b.c", "--dry-run"],
                             capture_output=True, text=True, timeout=30)
        if out.returncode == 0:
            report("PASS", "Facilitator seed script and Atlassian content complete (dry run)")
        else:
            report("FAIL", "Atlassian seed content incomplete", (out.stdout + out.stderr).strip()[-200:])

    # 6. What to put in .vscode/mcp.json
    if cmd:
        print("\nIn your .vscode/mcp.json, set \"command\" to:", json.dumps(cmd[0]),
              "" if len(cmd) == 1 else f'and start "args" with {json.dumps(cmd[1:])}')
        print("In .github/hooks/hooks.json the macOS/Linux command uses python3 and the Windows one uses python;")
        if IS_WIN and cmd[0] != "python":
            print("  edit the \"windows\" entries to use", " ".join(cmd))

    print("\nStill to check by hand (cannot be tested from a script):")
    print("  - VS Code > Chat view > you are signed in and Agent mode answers 'hello'")
    print("  - Your employer allows GitHub Copilot, MCP servers, and preview features (hooks)")

    fails = results.count("FAIL")
    print(f"\n{results.count('PASS')} passed, {results.count('WARN')} warnings, {fails} failed.")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
