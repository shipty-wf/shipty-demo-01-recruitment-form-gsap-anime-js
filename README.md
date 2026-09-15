# SHIPS — Crency-Agency-Inspired Recruitment Portal Demo

> High-impact, multi-stage interactive software engineering recruitment experience built with **GSAP 3** timeline choreography, **Anime.js** physics & particle dynamics, and a brutalist dark aesthetic inspired by [Crency Agency](https://crency.agency/).

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Frontend: Vanilla HTML5/CSS3/ES6](https://img.shields.io/badge/Stack-Vanilla%20%7C%20TailwindCSS%20%7C%20GSAP%20%7C%20Anime.js-blue.svg)
![Live Ready](https://img.shields.io/badge/Deployment-Zero%20Build%20Step-brightgreen.svg)

---

## 🌟 Key Highlights & Design System

1. **Aesthetic Direction (Crency Agency Tone)**:
   - **Obsidian Dark Palette**: Ultra-deep background (`#08080a`) layered with subtle SVG fractal noise grain overlay.
   - **High-Contrast Neon Accents**: Acid Lime (`#a3e635`), Electric Cyan (`#06b6d4`), and Hot Coral (`#f43f5e`).
   - **Kinetic Typography**: Large brutalist headings (`Syne` and `Space Grotesk`) with masked line reveals and staggered entrance cascades.

2. **GSAP 3 Motion Architecture**:
   - **Inertial Horizontal Wizard Transitions**: Seamless screen shifts using custom cubic bezier ease curves (`power3.inOut`).
   - **Magnetic Interaction Triggers**: Primary action buttons dynamically snap and gravitate toward the user's cursor.
   - **Dynamic HUD Progress**: Synchronized step counter, real-time progress track, and navigation breadcrumbs.

3. **Anime.js Micro-Interactions & Physics**:
   - **Interactive Tech Arsenal**: Staggered pill buttons that bounce with spring physics upon selection.
   - **Dual Trailing Lerp Cursor**: Fluid trailing ring with contextual states (`SELECT`, `DRAG`, `TOGGLE`, `TYPE`, `VIEW`).
   - **Celebratory Particle Canvas**: Physics-driven burst upon final application dispatch.

4. **Interactive 4-Step Flow**:
   - **Step 01 — Candidate Persona**: Full name, primary email, portfolio/GitHub URL, and primary engineering specialty.
   - **Step 02 — Technical Depth**: Interactive tech stack pill selection, slider for years of experience, and target compensation range.
   - **Step 03 — Architecture & Philosophy**: Engineering scenario prompt with live character meter and thought-process framing.
   - **Step 04 — Review & Dispatch**: Live glassmorphic dossier card displaying entered profile data with animated confirmation.
   - **⚡ Instant Demo Evaluation (Auto-Fill)**: One-click header pill (`⚡ AUTO-FILL MOCK`) instantly calibrates all 4 steps with candidate data, spring-animated skill tags, slider calibrations, and architecture narrative for frictionless review.

---

## 🚀 Getting Started

This demo is completely standalone and requires **no build step, bundler, or node_modules**.

### Quick Run
Simply open `index.html` in any modern desktop or mobile browser:

```bash
# Clone the repository
git clone https://github.com/shipty-wf/shipty-demo-01-recruitment-form-gsap-anime-js.git
cd shipty-demo-01-recruitment-form-gsap-anime-js

# Open in browser (Windows PowerShell)
Start-Process index.html

# Or run with any local HTTP server
npx serve .
# or
python3 -m http.server 8080
```

---

## 🛠 Tech Stack

- **Tailwind CSS 3.4** (via CDN with custom color extensions)
- **GreenSock Animation Platform (GSAP 3.12)**
- **Anime.js 3.2.2**
- **Lucide Icons**
- **Canvas Confetti & Particle Engine**

---

## 📄 License
MIT License. Created by [SHIPS Software House](https://github.com/shipty-wf).
