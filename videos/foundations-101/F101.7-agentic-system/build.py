"""Expand src/*.html placeholders (fonts, logos, icons, helpers) into compositions/."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).parent
LOGOS = json.loads((ROOT / "assets/logos.json").read_text())
FONTS = """@font-face { font-family: "Literata"; src: url("assets/fonts/Literata-600.woff2") format("woff2"); font-weight: 600; }
        @font-face { font-family: "IBM Plex Sans"; src: url("assets/fonts/IBMPlexSans-var.woff2") format("woff2"); font-weight: 100 700; }
        @font-face { font-family: "JetBrains Mono"; src: url("assets/fonts/JetBrainsMono-var.woff2") format("woff2"); font-weight: 100 800; }"""
ICONS = {
    "glean": '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="27" cy="27" r="17" fill="none" stroke="#003DA5" stroke-width="8"/><path d="M40 40l16 16" stroke="#FF6900" stroke-width="10" stroke-linecap="round"/></svg>',
    "calendar": '<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="6" y="10" width="52" height="48" rx="8" fill="#003DA5"/><path d="M6 18a8 8 0 0 1 8-8h36a8 8 0 0 1 8 8v8H6z" fill="#FF6900"/><rect x="16" y="4" width="6" height="14" rx="3" fill="#091F31"/><rect x="42" y="4" width="6" height="14" rx="3" fill="#091F31"/><g fill="#EAF2FF"><rect x="14" y="32" width="8" height="8" rx="2"/><rect x="28" y="32" width="8" height="8" rx="2"/><rect x="42" y="32" width="8" height="8" rx="2"/><rect x="14" y="44" width="8" height="8" rx="2"/><rect x="28" y="44" width="8" height="8" rx="2"/></g></svg>',
    "lock": '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M20 30v-8a12 12 0 0 1 24 0v8" fill="none" stroke="#091F31" stroke-width="7"/><rect x="12" y="28" width="40" height="30" rx="7" fill="#091F31"/><circle cx="32" cy="42" r="5" fill="#FF6900"/></svg>',
    "chat": '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M8 10h48a4 4 0 0 1 4 4v28a4 4 0 0 1-4 4H28L14 58V46H8a4 4 0 0 1-4-4V14a4 4 0 0 1 4-4z" fill="#003DA5"/><rect x="14" y="20" width="32" height="5" rx="2.5" fill="#EAF2FF"/><rect x="14" y="31" width="22" height="5" rx="2.5" fill="#EAF2FF"/></svg>',
    "file": '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M14 4h26l14 14v42H14z" fill="#003DA5"/><path d="M40 4v14h14z" fill="#EAF2FF"/><rect x="22" y="30" width="24" height="4" rx="2" fill="#EAF2FF"/><rect x="22" y="40" width="24" height="4" rx="2" fill="#EAF2FF"/><rect x="22" y="50" width="16" height="4" rx="2" fill="#EAF2FF"/></svg>',
    "globe": '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="26" fill="none" stroke="#003DA5" stroke-width="6"/><ellipse cx="32" cy="32" rx="11" ry="26" fill="none" stroke="#003DA5" stroke-width="5"/><path d="M8 24h48M8 40h48" stroke="#003DA5" stroke-width="5"/></svg>',
    "person": '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="20" r="12" fill="currentColor"/><path d="M10 58a22 22 0 0 1 44 0z" fill="currentColor"/></svg>',
    "check": '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="28" fill="#003DA5"/><path d="M19 33l9 9 17-19" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "eye": '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M4 32s10-18 28-18 28 18 28 18-10 18-28 18S4 32 4 32z" fill="#EAF2FF" stroke="#003DA5" stroke-width="5"/><circle cx="32" cy="32" r="10" fill="#003DA5"/></svg>',
    "send": '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M6 30L58 8 44 58 32 38z" fill="#FF6900"/><path d="M32 38L58 8" stroke="#091F31" stroke-width="4"/></svg>',
}
HELPERS = """const DUR = {{DUR}};
          const tl = gsap.timeline({ paused: true });
          const A = (s, t, o = {}) => tl.fromTo(s, { opacity: 0, x: o.x || 0, y: o.y === undefined ? 40 : o.y, scale: o.s || 1 }, { opacity: 1, x: 0, y: 0, scale: 1, duration: o.d || 0.5, ease: o.e || "power3.out", stagger: o.st || 0 }, t);
          const P = (s, t, o = {}) => tl.fromTo(s, { opacity: 0, scale: o.s || 0.5 }, { opacity: 1, scale: 1, duration: o.d || 0.6, ease: o.e || "back.out(1.7)", stagger: o.st || 0 }, t);
          const OUT = (s, t, d) => tl.to(s, { opacity: 0, duration: d || 0.35, ease: "power2.in" }, t);
          const DRAW = (s, t, d, st) => tl.fromTo(s, { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: d || 0.8, ease: "power2.inOut", stagger: st || 0 }, t);
          const LOOP = (s, props, cyc, from, to) => tl.to(s, Object.assign({ duration: cyc, yoyo: true, repeat: Math.max(0, Math.floor((to - from) / cyc) - 1), ease: "sine.inOut" }, props), from);"""

counter = {"n": 0}


def logo(name):
    svg = LOGOS[name]
    counter["n"] += 1
    n = counter["n"]
    for gid in ("jiraA", "jiraB", "confA", "confB"):
        svg = svg.replace(f'id="{gid}"', f'id="{gid}{n}"').replace(f"url(#{gid})", f"url(#{gid}{n})")
    return svg


def icon(name):
    if name in ICONS:
        return ICONS[name]
    return logo(name)


def expand(text):
    text = text.replace("{{FONTS}}", FONTS).replace("{{H}}", HELPERS)
    text = text.replace("{{CLAUDE}}", LOGOS["claudecode"])
    return re.sub(r"\{\{I:([a-z]+)\}\}", lambda m: icon(m.group(1)), text)


if __name__ == "__main__":
    raise SystemExit("run assemble.py; it expands src/ with narration cue times")
