# Promo page

`workshop_promo.html` is a single-slide, interactive advert for the workshop. It is one self-contained file: the mascots are embedded, and it needs no internet. Open it in any browser, or host it as is.

## What viewers can do

| Action | What happens |
|---|---|
| Click one of the 6 layers (Instructions, Skills, Agents, MCP, Hooks, Plugins) | The mascot changes, a speech bubble updates, and the panel shows what it is, why it helps technical communicators, what you build, and a short animated example. |
| Click **Who it's for**, **What to bring**, **Why it matters**, **What you take home** | The panel and mascot change to answer that question. |
| Click **30-second tour** | It steps through all six layers automatically. Click again to pause. |
| Explore all six layers | A progress counter fills, then the mascot celebrates and the tour button pulses. |
| Keyboard | Left and right arrows move between layers. Keys 1 to 6 jump to a layer. Escape returns to the start. |
| Link to one layer | Add `#hooks`, `#mcp`, `#who`, and so on to the address. |

It adapts to dark mode and phone width, and respects the "reduce motion" setting.

## Before you publish

The page has a white header band (STC India logo, Summit name, date, venue) and a white footer band (workshop by Amandeep Talwar with a LinkedIn link, matching the look of stcindia.org). It shows the STC India logo and the Summit details (STC India Annual Summit 2026, 4 and 5 December 2026, The Chancery Pavilion, Bengaluru). It has no registration link: the STC committee manages registrations. To change the event text or add a link later, edit `_build/promo_template.html`, then rebuild:

```
python3 _build/build_promo.py
```

`_build/mascots/` holds the original images and `_build/stc_india_logo.svg` is the logo. The build script embeds both into the HTML.
