---
name: Precision SaaS
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#424754'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#727785'
  outline-variant: '#c2c6d6'
  surface-tint: '#005ac2'
  primary: '#0058be'
  on-primary: '#ffffff'
  primary-container: '#2170e4'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#545c72'
  on-tertiary: '#ffffff'
  tertiary-container: '#6c748b'
  on-tertiary-container: '#fefcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#dae2fd'
  tertiary-fixed-dim: '#bec6e0'
  on-tertiary-fixed: '#131b2e'
  on-tertiary-fixed-variant: '#3f465c'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-xs:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  margin: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system delivers a sleek, minimalist, and premium SaaS aesthetic, drawing inspiration from industry-leading tools like Linear and Notion. It is built for high-performance productivity software, developer tools, and modern enterprise platforms.

### Personality & Audience
- **Target Audience:** Modern professionals, developers, product teams, and knowledge workers who value speed, clarity, and precision.
- **Emotional Response:** Calm, focused, efficient, and elevated. The UI should feel weightless, transparent, and effortlessly organized.

### Design Style
The design system adopts a refined **Minimalism** approach characterized by:
- Generous whitespace and strict typographic hierarchy.
- Crisp white and cool gray backgrounds with subtle surface variations.
- Precision blue branding accents (`#3b82f6`) for high-intent actions.
- Soft, highly diffused ambient shadows and low-contrast borders for gentle depth.

## Colors

The color palette is anchored by a crisp, neutral foundation of cool slate-grays and pure whites, punctuated by a vibrant primary blue for interactive states and focus rings.

### Palette Architecture
- **Primary (`#3b82f6`):** Used for primary actions, active states, focus indicators, and key data points.
- **Secondary (`#64748b`):** Slate gray dedicated to secondary text, subtle borders, and inactive icons.
- **Tertiary (`#0f172a`):** Deep slate-black for high-contrast headlines and primary body text.
- **Neutral (`#f8fafc`):** Ultra-light cool gray for background surfaces, canvas areas, and hovered rows.

## Typography

Typography relies entirely on **Inter** to maintain a neutral, highly readable, and systematic information architecture. Letter spacing is slightly tracked in for larger headings to enhance the premium, engineered feel, while body text prioritizes optical legibility at small sizes.

### Responsive Scaling
For viewports smaller than 768px, scale down headline sizes by clamping values: convert `headline-xl` to `32px` and `headline-lg` to `26px`.

## Layout & Spacing

The layout philosophy follows a responsive **Fluid Grid** system combined with an 8px base spacing rhythm. 

### Grid & Breakpoints
- **Desktop (1024px+):** 12-column fluid grid with 24px (`1.5rem`) gutters and 32px (`2rem`) outer canvas margins.
- **Tablet (768px - 1023px):** 8-column grid with 20px gutters and 24px margins.
- **Mobile (< 768px):** 4-column grid with 16px gutters and 16px margins. Content reflows into a single-column stack for dense data views.

## Elevation & Depth

Depth is communicated subtly through layered surface tonality and hyper-diffused ambient shadows, avoiding heavy drop shadows in favor of a weightless, flat-yet-layered interface.

- **Surface Tiers:** Use pure white (`#ffffff`) surfaces floating above the cool gray neutral canvas (`#f8fafc`).
- **Ambient Shadows:** Apply ultra-soft shadows (`0px 4px 20px -2px rgba(15, 23, 42, 0.06)`) for floating elements like dropdowns, modals, and floating action bars.
- **Low-Contrast Outlines:** Use crisp 1px borders in `#e2e8f0` to delineate structural containers without adding visual noise.

## Shapes

The shape language utilizes refined, soft geometry to balance approachability with technical precision. 

- **Base Radius (`rounded`):** 0.375rem (6px) for small components like tags, badges, and inner form controls.
- **Large Radius (`rounded-xl`):** 0.75rem (12px) for primary cards, modals, dropdown menus, and container surfaces.
- **Pill Radius (`rounded-full`):** Reserved exclusively for status indicators, user avatars, and primary pill buttons.

## Components

Component styling must adhere to the minimalist, high-precision SaaS narrative, favoring micro-interactions, clean borders, and clear typographic hierarchy.

- **Buttons:** Primary buttons feature the `#3b82f6` background with white text, `rounded-xl` shape, and a subtle active scale-down effect. Secondary buttons utilize a transparent background with a 1px slate border and hover state background fill of `#f1f5f9`.
- **Chips & Badges:** Compact elements with `rounded-full` styling, low-opacity background tints, and `label-sm` typography.
- **Input Fields:** Built with a clean white background, 1px `#cbd5e1` border, `rounded-xl` corners, and a `#3b82f6` focus ring with a 2px offset.
- **Cards:** White surfaces elevated on the neutral canvas with 1px low-contrast borders (`#e2e8f0`), `rounded-xl` corners, and generous internal padding (`space-lg`).
- **Lists & Tables:** Clean row-based layouts featuring subtle hover states (`#f8fafc`), generous vertical line-height, and bottom borders in `#f1f5f9`.
- **Command Palettes & Menus:** Essential for this aesthetic—floating panels featuring wide search inputs, keyboard shortcut indicators, and soft ambient shadows.