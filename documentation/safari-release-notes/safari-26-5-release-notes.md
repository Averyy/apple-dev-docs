# Safari 26.5 Release Notes

**Framework**: Safari Release Notes

Released May 11, 2026 — 26.5 (20624.2.5)

#### Overview

Safari 26.5 is available for iOS 26.5, iPadOS 26.5, visionOS 26.5, macOS 26.5, macOS Sequoia, and macOS Sonoma.

##### Accessibility

###### Resolved Issues

- Fixed an issue where the accessibility tree could permanently be empty if built during early page load when only a scroll area and web area were present. (174244620)

##### Animations

###### Resolved Issues

- Fixed support for the `scroll` animation timeline range name in scroll-driven animations. (171630023)
- Fixed an issue where scroll-driven animations were not properly paused when `animation-play-state` was dynamically set to `paused`. (171630127)
- Fixed an issue where view timeline animations near the 0% and 100% thresholds reported incorrect progress values. (171630157)
- Fixed a regression where animating to an implicit value for individual transform properties failed to animate. (173717819)
- Fixed an issue where animation timelines could fail to restore correctly after navigating back to a page from the back-forward cache. (174561577)

##### Css

###### New Features

- Added support for the `:open` pseudo-class for `<details>`, `<dialog>`, `<select>`, and `<input>` elements. (173253012)
- Added support for `element-scoped` keyword in `random()`. Updated `random()` caching behavior so that custom property identifiers like `random(--foo)` are matched globally to the document rather than scoped to individual elements, aligning with the updated specification. Removed support for `element-shared`. (174037391)

###### Resolved Issues

- Fixed an issue where a `display: grid` subgrid inside a `grid-lanes` container incorrectly contributed its items’ intrinsic sizes to the parent’s track sizing algorithm. (171230544)
- Fixed an issue in collapsed border tables where the border style of a cell adjacent to a `rowspan` cell was incorrectly applied across the full length of the spanning cell’s border. (171634786)
- Fixed a layout regression where absolutely positioned elements inside block-in-inline containers were incorrectly overlapping adjacent content. (171732203)
- Fixed a regression where content with `column-count: 1` could fail to display text.  (172306151)
- Fixed an issue where `@font-face` rules with different styles could incorrectly fall back to glyphs from other faces in the same family, rather than proceeding to the next family as specified by the font matching algorithm. (172390840)
- Fixed `hanging-punctuation` to correctly treat U+0027 (apostrophe) and U+0022 (quotation mark) as hangable quote characters. (172668971)
- Fixed an issue where ideographic space did not hang when using `hanging-punctuation: first`. (172669250)
- Fixed an issue where media queries failed to re-evaluate during viewport resizing when CSS anchor positioning and viewport units were both in use. (172864699)
- Fixed an issue where chains of three or more anchor-positioned elements didn’t resolve correctly. (173357622)
- Fixed an issue where `lh` and `rlh` units resolved with double-zoom when `line-height` is a number. (173515568)
- Fixed an issue where the `rlh` unit was double-zoomed when resolving with evaluation-time zoom for unzoomed properties. (173518838)
- Fixed an issue where `anchor()` fallback values did not accept unitless zero. (173554237)
- Fixed an issue where an element with `display: contents` did not establish an anchor scope when using `anchor-scope`. (173718365)
- Fixed an issue where fixed-position boxes anchored to children of sticky-positioned boxes did not stick correctly. (173722628)
- Fixed an issue where `aspect-ratio` was not honored correctly when the page was zoomed in. (174498486)
- Fixed an issue where `:has(:empty)` was not invalidated when the content of a child element changed from empty to non-empty. (174501418)

##### Editing

###### Resolved Issues

- Fixed an issue where pressing backspace on a line below an image in a `contenteditable` region could place the cursor in the wrong position. (171850465)
- Fixed an issue where emoji images copied from websites and pasted into other sites appeared broken due to cross-origin resource policy blocking the SVG image sources. (172775070)
- Fixed an issue where pasting text into an empty list item created an extra blank bullet. (173275372)

##### Forms

###### Resolved Issues

- Fixed an issue where a `readonly` date `<input>` could still be edited via keyboard using the date picker. (171535893)
- Fixed an issue on iOS and iPadOS where `datalist` suggestions were presented directly over the associated input, obscuring it. (174264299)

##### Html

###### Resolved Issues

- Fixed `dragenter` and `dragleave` events to include `relatedTarget` in the event object. (172048448)
- Fixed an issue on iOS where the drag thumbnail could show an incorrect image after long-pressing an image with an embedded link. (172293971)

##### Images

###### Resolved Issues

- Fixed a regression where images with `srcset` and `sizes` attributes containing `calc()` expressions with division by zero were not displayed. (173954748)

##### Javascript

###### Resolved Issues

- Fixed `TypedArray.prototype.sort()` failing when the comparison function accesses the `.buffer` property of the typed array. (172516044)

##### Media

###### Resolved Issues

- Fixed an issue where the media controls volume button was mispositioned and overlapped with other controls in right-to-left locales. (171182590)
- Fixed an issue where `MediaCapabilities.decodingInfo()` always returned `false` for `spatialRendering`. (172689752)

##### Networking

###### Resolved Issues

- Fixed an issue where downloaded files used the file extension from the URL path instead of the HTTP `Content-Type` header. (173705083)
- Fixed an issue where downloaded files were saved with incorrect or missing file extensions when the URL path extension did not match the HTTP `Content-Type` header. (173945210)

##### Rendering

###### Resolved Issues

- Fixed an issue where content inside inline elements with block-level children and rendering layers was not displayed correctly. (171101386)
- Fixed an issue where `getClientRects()` could return rects with zero width and height for spans in multi-column layouts. (171101490)
- Fixed an issue where an empty `<span>` with decoration was incorrectly positioned when a sibling block margin was present inside a block-in-inline context. (171101555)
- Fixed an issue where a `<br>` element was incorrectly positioned inside a block-in-inline context when a block margin was present. (171101748)
- Fixed an issue where grid and flex layout could cause elements to shift position at certain zoom levels. (172118478)
- Fixed an issue where text content could get cut off inside overflow containers when the page was zoomed in. (172118721)
- Fixed an issue where images could appear stretched inside certain flex and grid layout configurations. (172224411)
- Fixed an issue where images inside transformed containers were not properly centered. (172475726)
- Fixed an issue where pinch-to-zoom could cause web content to jump or disappear on some websites. (172507916)
- Fixed an issue where user-installed font variants could interfere with system font matching, causing incorrect fonts to be selected. (173345107)

##### Svg

###### New Features

- Added support for the `color-interpolation` attribute on SVG gradients, enabling `linearRGB` color space interpolation. (171816049)

###### Resolved Issues

- Fixed an issue where `removeAttribute` for `width` or `height` on an SVG root element did not reset to the initial default values. (172132798)
- Fixed event name mapping for `onbegin`, `onend`, and `onrepeat` on `SVGAnimationElement` and added the missing `onend` event handler. (172581017)
- Fixed an issue where an SVG `<image>` element was not repainted when its `href` attribute was removed. (172875166)
- Fixed an issue where UI events such as wheel failed to fire for inner SVG elements. (173009454)
- Fixed an issue where SVG cursors set via `cursor: url()` appeared blurry on high DPI displays. (173950927)

##### Scrolling

###### Resolved Issues

- Fixed an issue where scroll-snap re-snapping after layout changes could cause incorrect scroll positions, resulting in the wrong content being shown. (171541221)

##### Storage

###### Resolved Issues

- Fixed an issue where IndexedDB connections could become permanently broken until the page was reloaded. (172247569)
- Fixed an issue where `document.hasStorageAccess()` could return a Promise that never resolves. (172424614)

##### Web Api

###### New Features

- Added support for the `source` property on `ToggleEvent`, which identifies the element that triggered the toggling of a target element such as a popover’s invoker button. (171635116)
- Added support for the Origin API, which exposes origin information as a structured `Origin` object. (171816045)

###### Resolved Issues

- Fixed an issue where `DecompressionStream` discarded valid decompressed output when extra trailing bytes were present after the compressed stream, instead of enqueuing the output before throwing. (171020155)
- Fixed an issue where calling preventDefault() on pointerdown events did not prevent page scrolling when only passive touch event listeners are installed. (173988278)

##### Web Extensions

###### Resolved Issues

- Fixed an issue where extensions with a trailing comma in `manifest.json` failed to load in Safari. (172120877)

##### Webgl

###### Resolved Issues

- Fixed WebGL shader compilation to properly handle `NaN` and `infinity` values.  (166699074)

##### Webrtc

###### Resolved Issues

- Fixed `RTCIceCandidate.toJSON()` to include the `usernameFragment` property in its serialized output. (172689343)
- Fixed `RTCRtpSender` to allow a `maxFramerate` value of 0. (172689374)
- Fixed `RTCRtpSynchronizationSource.timestamp` to use the correct time base. (172689387)
- Fixed an issue where remote audio and video track IDs were incorrectly derived from SDP. (172689452)
- Fixed `RTCRtpTransceiver.setCodecPreferences()` to accept codecs with case-insensitive `mimeType` matching. (172689477)
- Fixed an issue where the camera did not turn on automatically in Google Meet when media permissions were set to “Allow”. (174023905)

## See Also

- [Safari 26.4 Release Notes](safari-26_4-release-notes.md)
  Released March 24, 2026 — 26.4 (20624.1.16)
- [Safari 26.3 Release Notes](safari-26_3-release-notes.md)
  Released February 11, 2026 — 26.3 (20623.2.7)
- [Safari 26.2 Release Notes](safari-26_2-release-notes.md)
  Released December 12, 2025 — 26.2 (20623.1.14)
- [Safari 26.1 Release Notes](safari-26_1-release-notes.md)
  Released November 3, 2025 — 26.1 (20622.2.11)
- [Safari 26.0 Release Notes](safari-26-release-notes.md)
  Released September 15, 2025 — 26 (20622.1.22)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-26_5-release-notes)*