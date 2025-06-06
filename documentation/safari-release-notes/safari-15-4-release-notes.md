# Safari 15.4 Release Notes

**Framework**: Safari Release Notes

Released March 14, 2022 — Version 15.4 (17613.1.17)

#### Overview

Safari 15.4 ships with the iOS and iPadOS 15.4 and macOS 12.3.

##### General

###### Known Issues

- Safari 15.4 in macOS Catalina running on an iMac (Late 2012 or 2013) with a NVIDIA GPU may experience multiple sites that fail to load or continuously refresh after loading. (88177392)

##### Css

###### New Features

- Added `::backdrop` pseudo-element support.
- Added support for CSS Containment with the `contain` property.
- Added CSS Cascade Layer support for improved developer control over cascading rules.
- Added `accent-color` support to alter the accent color of form controls `<input type="checkbox">`, `<input type="radio">`, `<progress>`, `<select>`; text-input types with a `<datalist>` in macOS, iPadOS, and iOS; and `<input type="range">`, `<button>`, and `<input type="button">` in iPadOS and iOS.
- Added `:has()` pseudo-class support to match an element with an element that matches a given selector.
- Added support for `text-decoration-skip-ink` to control how underlines and overlines are rendered.
- Added support for small (`svw`, `svh`, `svi`, `svb`, `svmin`, `svmax`), large (`lvw`, `lvh`, `lvi`, `lvb`, `lvmin`, `lvmax`), dynamic (`dvw`, `dvh`, `dvi`, `dvb`, `dvmin`, `dvmax`), and logical (`vi`, `vb`) viewport units.
- Added support for the `:focus-visible` pseudo-class to style the focus indicator only when rendered by the browser.
- Added support for the `font-palette` property and the `@font-palette-values` rule to support recoloring color fonts.
- Implemented the `ic` unit, equivalent to inline direction length (width or height) of the “水” glyph in the element’s current font.
- Implemented `calc()` math functions including `sin`, `cos`, `tan`, `e`, `pi`, `exp`, `log`, `atan`, `acos`, `asin`, and `atan2`.
- Added the `appearance` property, including `appearance: auto`, and aliased `-webkit-appearance` to the unprefixed property.
- Added the `mask` property, along with the long-hand forms `mask-image`, `mask-size`, `mask-repeat-x`, `mask-repeat-y`, `mask-origin`, and aliased `-webkit-mask`.
- Added the `backface-visibility` property and aliased `-webkit-backface-visibility` to the unprefixed property.
- Added the `text-combine-upright` property and aliased `-webkit-text-combine` to the unprefixed property.
- Added the `print-color-adjust` property and aliased `-webkit-print-color-adjust` to the unprefixed property.
- Added the `match-parent` CSS value and aliased `-webkit-match-parent` for the `text-align` CSS property.

###### Resolved Issues

- Fixed the drawing area to be painted when the computed `border-width` is 0 and the `border-image-width` is set or defaults to a number.
- Fixed `rem` in media queries to calculate using `font-size: initial`, not the root element `font-size`.
- Fixed `background-attachment: local`.
- Fixed gradient color interpolation for colors with alpha transparency.

###### Removed Features

- Removed non-standard CSS properties `-webkit-border-fit`, `-webkit-margin-collapse`, `-webkit-margin-top-collapse`, `-webkit-margin-bottom-collapse`, `-webkit-margin-before-collapse`, `-webkit-margin-after-collapse`, and `-webkit-background-composite`.

##### Html

###### New Features

- Added support for the `<dialog>` element.
- Added lazy-loading support for images with the `loading` attribute on the `<img>` element.
- Added support for the `autofocus` attribute.

##### Web Api

###### New Features

- Added support for Web App Manifest icons, shown when no `apple-touch-icon` is provided and when either `"purpose": "any"` is present or the `"purpose"` key isn’t present at all.
- Improved Web App Manifest to always attempt to fetch the manifest file.
- Enabled BroadcastChannel for communication between different windows, tabs, frames, or iframes.
- Added support for ServiceWorker downloads.
- Added support for ServiceWorker Navigation Preload.
- Added support for the CSS `scroll-behavior` property and `ScrollOptions`, allowing smooth scrolling to anchors or via JavaScript.
- Added support for the `ResizeObserverEntry` and `ResizeObserverSize` interfaces.
- Added support for the Web Locks API.
- Added support for recurring payments with the Payment Request API.
- Added support for controlling the initially selected shipping method in the Payment Request API.

###### Resolved Issues

- Fixed Fetch using `FormData` with a file not going through ServiceWorker.

###### Removed Features

- Removed the XSS Auditor.

##### Javascript

###### New Features

- Added `Object.hasOwn()`.
- Added `self.structuredClone()`.
- Added `Array.prototype.findLast` and `Array.prototype.findLastIndex`.
- Added `Array.prototype.at` , `String.prototype.at` , and `TypedArray.prototype.at`.
- Added `Intl.NumberFormat.prototype.formatRange` and `Intl.NumberFormat.prototype.formatRangeToParts`.
- Added `Intl.PluralRules.prototype.selectRange`.
- Added the `Intl` enumeration.
- Added the `Intl.Locale` info extension.
- Updated `Intl.DisplayNames` to V2.
- Updated `Intl.NumberFormat` to V3, supporting new options.
- Supported the `TimeZoneName` option in `Intl.DateTimeFormat`.

##### Media

###### New Features

- Added support for WebRTC perfect negotiation.
- Added in-band chapter tracks support.

##### Private Click Measurement

###### New Features

- Enabled unlinkable tokens for triggering events on a merchant website.
- Added support for same-site conversion pixels on merchant websites, to enable removal of cross-site tracking pixels.
- Allowed measurement of links in nested, cross-site iframes on publisher websites.

##### Safari Web Extensions

###### New Features

- Added support for `manifest_version` 3 and related API changes.
- Added support for `service_worker` background scripts as an alternative to nonpersistent background pages.
- Added support for script and style injection via the `browser.scripting` APIs.
- Added support for dynamic and session rules via the `browser.declarativeNetRequest` APIs.
- Added support for webpage-to-extension messaging using `externally_connectable:matches`.

##### Resolved Issues

- Fixed: Limits are now enforced on the size and number of items in extension sync storage.
- Fixed: More directives are now allowed to be included in the `content_security_policy` of an extension’s manifest, such as the `sandbox` directive.
- Fixed: Special matching characters (`*`, `|`, `||`, and `^`) in `urlFilter` of `declarativeNetRequest` rules are now handled, instead of being treated as regex patterns.
- Fixed: `Promise` returns from `runtime.onMessage` listeners are now allowed for the message reply.

##### Security

###### New Features

- Improved support for Content Security Policy 3: - Added correct blocked resource violation reporting for inline script, inline style, and eval execution.
- Added support for the `'strict-dynamic'` source expression.
- Added support for the `'unsafe-hashes'` source expression.
- Added support to allow external JavaScript matching hash source expressions.
- Added support for the `'report-sample'` expression.

##### Web Inspector

###### New Features

- Added CSS alignment controls in the Styles panel.
- Added support for showing the related `@layer` for CSS rulesets in the Styles panel.
- Improved CSS auto-completion in the Styles panel with fuzzy matching.
- Added CSS variables grouping by type in the Computed panel.

## See Also

- [Safari 15.6 Release Notes](safari-15_6-release-notes.md)
  Released July 20, 2022 — Version 15.6 (17613.3.9)
- [Safari 15.5 Release Notes](safari-15_5-release-notes.md)
  Released May 16, 2022 — Version 15.5 (17613.2.7)
- [Safari 15.2 Release Notes](safari-15_2-release-notes.md)
  Released December 13, 2021 — Version 15.2 (17612.3.6)
- [Safari 15 Release Notes](safari-15-release-notes.md)
  Released September 20, 2021 — Version 15 (17612.1.27)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-15_4-release-notes)*