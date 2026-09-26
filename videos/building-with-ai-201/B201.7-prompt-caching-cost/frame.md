---
colors: { canvas: "#07192A", surface: "#0E2A44", fg: "#EEF3F7", muted: "#9FB3C6", hit: "#00C1D4", miss: "#FF6900", brand: "#3D7BFF" }
typography: { title: { family: "Literata", weight: 600 }, body: { family: "IBM Plex Sans", weight: 400 }, data: { family: "JetBrains Mono", weight: 500 } }
components: { corners: "10px panels, 4px token blocks", shadows: "none; depth comes from glow and the 3D scenes", logo: "none" }
---

# B201.7 frame

Concept angle: the prompt is a row of physical token blocks. A cache hit lights them teal and they are
reused; a miss turns them orange and they are rebuilt. Every scene reuses that one visual language, so
the viewer learns to read teal as cheap and orange as expensive.

Dark navy canvas with a faint token grid. Literata for the one statement per scene, IBM Plex for support,
JetBrains Mono for every number, token and byte string. Teal and orange are semantic only, never
decoration. Focal hierarchy: one statement, one mechanism or chart, small source line at the bottom edge.
