# Safari 26.2 Release Notes

**Framework**: Safari Release Notes

Released December 12, 2025 — 26.2 (20623.1.14)

#### Overview

Safari 26.2 is available for iOS 26.2, iPadOS 26.2, visionOS 26.2, macOS 26.2, macOS Sequoia, and macOS Sonoma.

##### Accessibility

###### New Features

- Added support for automatically scrolling off-screen `<input type="radio">` elements into view when they are focused, improving accessibility for users navigating with screen readers or keyboard shortcuts. (55121458)
- Added support for `aria-colindextext` and `aria-rowindextext` to provide human-readable alternatives to `aria-colindex` and `aria-rowindex`. (109669421)

###### Resolved Issues

- Fixed Voice Control number and name overlays not labeling content inside `iframe` elements. (118252216)
- Fixed incorrect accessibility bounds of SVG roots, ensuring assistive technologies have access to the correct geometry. (153782363)
- Fixed an issue where `<label>` elements targeted by `aria-labelledby` stopped providing accessibility text to assistive technologies after dynamic page changes. (158906980)

##### Animations

###### New Features

- Added support for `Animation.prototype.overallProgress`.  (155625287)
- Added support for endpoint-inclusive active intervals in `Animation.commitStyles()` to correctly persist styles for completed animations. (158684709)

###### Resolved Issues

- Fixed inheritance of additional animation properties (`animation-timing-function`, `animation-play-state`, `animation-iteration-count`, and `animation-direction`) in `::view-transition` pseudo-elements to improve style consistency. (156131284)
- Fixed `animation-name` resolution to correctly find matching `@keyframes` within tree-scoped and shadow DOM contexts. (156484228)
- Fixed a bug where extremely large `animation-duration` values could cause the page to become unresponsive. (158775366)
- Fixed `Animation.commitStyles()` so that custom properties are properly committed to the target element. (158919736)
- Fixed `Animation.commitStyles()` to correctly commit logical properties as their corresponding physical properties. (158920529)

##### Browser

###### Resolved Issues

- Fixed: Safari now reports a frozen OS version in its user agent string on iOS 26 and iPadOS 26, showing the last version released before iOS 26.  (156170132)

##### Css

###### New Features

- Added support for the `cursor` property on pseudo-elements.  (90364915)
- Added support for the `position-visibility` property. (129789653)
- Added support for the new `math-shift` CSS property to control compact or “cramped” rendering of MathML formulas, reducing vertical shifts for superscripts. (138023006)
- Added support for the CSS `random()` function. (145696017)
- Added support for `@scope(:host)`. (153443869)
- Added support for CSS tree-counting functions `sibling-index()` and `sibling-count()`. (155624960)
- Added support for `cross-origin()` and `referrer-policy()` CSS URL modifiers. (155625162)
- Added support for the `safe` keyword with `anchor-center` in CSS Anchor Positioning. (155767796)
- Added support for `position-try` on pseudo-elements like `::before`, `::after`, and `::backdrop`. (156550553)
- Added support for `:scope` when the scoping root is `:visited`. (157588890)
- Added support for non-integral decimal values in the `initial-letter` CSS property to allow fractional sizes. (157808105)
- Added support for the `field-sizing` property. (157907105)
- Added support for `@scope` implicit scoping roots with constructed and adopted stylesheets to correctly apply styles in shadow DOM. (158119016)
- Added support for the `scrollbar-color` property. (158436083)
- Added support for the generic `math` font family in `font-family` allowing better default rendering for MathML content. (158851931)
- Added support for using `color-mix()` without a color space, defaulting to `oklab`. (159039709)
- Added support for `display-p3-linear` colors in CSS. (159579630)
- Added support for `text-decoration-line` values `spelling-error` and `grammar-error`. (160494378)
- Added support for `flip-x` and `flip-y` options in `position-try-fallback` for CSS Anchor Positioning.  (163497870)
- Added support for allowing positioned boxes in scrollable containing blocks to overflow in the scrollable direction. (163595289)

###### Resolved Issues

- Fixed `-webkit-user-select: none` disabling find-in-page in Safari. (8081660)
- Fixed incorrect z-ordering for `position: sticky` elements. (90572595)
- Fixed `getComputedStyle` to correctly ignore `::first-letter` and `::first-line` styles on flex containers, to reflect used style. (94163778)
- Fixed style invalidation so that `:scope` selectors always match even when the scoping root is unavailable. (135907710)
- Fixed propagation of the `body` element’s `writing-mode` to the document element to match the CSS Writing Modes Level 4 specification. (149475070)
- Fixed `@position-try` so that `revert-layer` correctly only reverts the position-try origin instead of affecting other cascade origins. (154355428)
- Fixed positioned boxes in scrollable containing blocks to overflow in scrollable direction. (155625030)
- Fixed `anchor-center` so that when an anchored element has no anchor in the same containing block, it correctly falls back to behaving like `center` as specified. (155768216)
- Fixed `anchor()` positioning in CSS Grid to correctly account for `grid-area`. (155823420)
- Fixed the default computed value for `text-emphasis-style: filled|open` to be `filled|open circle` not `filled|open dot` in horizontal typographic modes. (155911820)
- Fixed the `text-decoration` shorthand to cover all four longhand properties. (156011594)
- Fixed an issue where `@namespace` rules that failed insertion could still affect the namespace node. (156651404)
- Fixed incorrect handling of `auto` inline margins on grid items during track sizing that caused excessive vertical spacing in subgrids. (157638931)
- Fixed automatic `min-size` handling for flex and grid items to correctly treat `overflow: clip` as non-scrollable, aligning with the CSS specifications. (158215991)
- Fixed incorrect baseline alignment for `<button>` elements when `contain: layout` is applied by using the content box as the baseline. (159007878)
- Fixed out-of-flow box with no sibling ignoring align-content. (159097576)
- Fixed CSS anchor positioning to remember the last successful position option at `ResizeObserver` delivery time, aligning with the spec. (159225250)
- Fixed handling of the `::first-line` pseudo-element when floats prevent the initial line from containing inline content, ensuring correct styling is applied to the actual first formatted line. (159613287)
- Fixed an issue where collapsed table rows subtracted `border-spacing` twice. (160542118)
- Fixed `::view-transition` pseudo-element to use `position: absolute` instead of `fixed` to align with the updated specification. (160622000)
- Fixed container queries to allow `container-name` matching across the full flat tree, making container names tree-scoped in line with the CSS Conditional 5 specification. (160696378)
- Fixed handling of `::first-letter` pseudo-elements to always force `inline` display unless floated.(160710650)
- Fixed the behavior of the nesting selector `&` directly inside `@scope` to correctly act like `:where(:scope)` for proper specificity handling. (160769736)
- Fixed `position-try-fallback` resolution by treating names as tree-scoped references to properly search shadow DOM host scopes. (161081231)
- Fixed an issue where a `<select>` element with long `<option>` text caused horizontal scrolling when nested inside a flex item. (161563289)
- Fixed `getComputedStyle` to return numeric values for `orphans` and `widows` instead of the internal `auto` value, ensuring the computed values correctly reflect the CSS specification. (161566631)
- Fixed `column-count: 1` so that it now correctly creates a multi-column container per the CSS Multi-column Layout specification. (161611444)
- Fixed the calculation of anchor positions in `vertical-rl` multi-column layouts by correctly flipping coordinates in fragmented flows. (161616545)
- Fixed the order to try anchor position fallback options, such that the last successful position option is tried first, followed by the original style, and then the remaining options. (161714637)
- Fixed `position-area` handling to include the in-flow scrollable area of the initial containing block. (161741583)
- Fixed `position-visibility: no-overflow` to respond correctly to scrolling. (162173481)
- Fixed: Renamed `position-area` keywords from `x-self-start`, `x-self-end`, `y-self-start`, and `y-self-end` to `self-x-start`, `self-x-end`, `self-y-start`, and `self-y-end` respectively to align with updated CSSWG specifications.(162214793)
- Fixed auto margins by converting them to zero when `position-area` or `anchor-center` is applied in CSS Anchor Positioning. (162809291)
- Fixed `FontFace.family` so that font family names with spaces are treated as plain strings without parsing or serializing aligning with other browsers. (163047573)
- Fixed flex and grid layout to correctly handle padding and margins in all writing modes. (163048874)
- Fixed an issue where underlines using `text-underline-position: right` appeared on top of the text in horizontal writing modes instead of under the line. (163506701)
- Fixed an infinite style resolution loop when a `position-try` box was inside a `display: none` tree. (163691875)
- Fixed `position-area` alignment so that when only one inset is set to `auto`, the element now aligns toward the opposite non-auto inset. (163691905)
- Fixed `text-decoration-thickness` and `text-underline-offset` not working in vertical writing modes. (163727749)
- Fixed an issue where `scrollRectToVisible()` did not scroll pages to bring fixed anchor-positioned boxes into view when navigating with the keyboard. (163764088)
- Fixed an issue where anchor-positioned elements transitioning from `display: block` to `display: none` can not anchor themselves to the anchor. (163861918)
- Fixed incorrect underline positioning for `text-decoration` when inline box sides are trimmed. (163909909)

##### Canvas

###### Deprecations

- Removed non-standard legacy `drawImageFromRect`. (141681635)

##### Dom

###### Resolved Issues

- Fixed an issue where command-clicking to open a link in a new tab navigates the current tab. (57216935)

##### Editing

###### Resolved Issues

- Fixed jumbled text when copy/pasting bidirectional text starting with left-to-right. (152236717)
- Fixed paste performance in `textarea` by skipping unnecessary layout calls and only removing unrendered text nodes in richly editable fields. (157813510)

##### Events

###### Resolved Issues

- Fixed boundary pointer and mouse events not firing when the hit test target changed under a stationary pointer. (160147423)

##### Forms

###### New Features

- Added support for form controls to preserve legibility when using `accent-color` in both light and dark modes. (99018889)
- Added support for normalizing full-width digits, minus signs, and full-width dots to ASCII in `<input type="number">` fields, immediately rejecting disallowed characters. (141257181)

###### Resolved Issues

- Fixed an issue where some websites may sometimes fail to reveal the focused element when the keyboard appears. (50384887)
- Fixed input fields with `field-sizing: content` so that larger placeholder text now correctly expands the height of the field by including the placeholder’s computed height. (123125836)
- Fixed `<select>` element with long `<option>` text causing horizontal scrolling in grid or flex containers. (141633685)
- Fixed an issue on iOS where backing out of the “Take a photo/video” file upload flow caused the upload button to stop working.  (157789623)
- Fixed painting for `<input type="range">` sliders in right-to-left vertical block writing modes. (158567821)
- Fixed an issue where tainted scripts were blocked from reading values of form fields they created, now allowing access if the field was not modified by user input. (163299988)

##### Html

###### New Features

- Added support for displaying HTML `title` attribute tooltips on Catalyst. (79416560)
- Added support for `command` and `commandfor` attributes on buttons to provide a declarative way to control popovers and dialogs. (147442565)
- Added support for `hidden=until-found` and the `beforematch` event. (157348946)
- Added auto-expanding details element. (157349077)

###### Resolved Issues

- Fixed an issue where navigating to `:~:text` fragments on dynamically generated pages did not highlight or scroll to the fragment. (150880542)

##### Home Screen Web Apps

###### Resolved Issues

- Fixed an issue where an audio element failed to play when re-opening a Home Screen Web App.  (155336513)

##### Images

###### Resolved Issues

- Fixed HDR images in CSS backgrounds, CSS borders and inside SVG images so they are now properly decoded and rendered in HDR mode. (158076668)

##### Javascript

###### New Features

- Added support for `Math.sumPrecise`. (155642395)
- Added support for `Map.prototype.getOrInsert`, `WeakMap.prototype.getOrInsert`, and related methods enabling easier insertion of default values into Maps and WeakMaps. (157176714)
- Added support for including `Promise.race` in async stack traces. (161700216)
- Added support for including `Promise.allSettled` in async stack traces. (162266189)

###### Resolved Issues

- Fixed non-standard `new Date(2024-12-3)` yielding to an “Invalid Date” error. (141044926)
- Fixed “text/json/json+json” to be considered an invalid JSON MIME type.  (154912716)
- Fixed compatibility issues with the `timezone` option in the `Intl.DateTimeFormat` constructor. (156148700)
- Fixed `Intl.Local#language` to return `"und"` if the language subtag is `"und"`. (156248659)
- Fixed `Intl` to support non-continental timezones to align with the specification. (156424446)
- Fixed exception check errors by adding a missing exception check for `Array#flat`. (157525399)
- Fixed an issue where the module loader would incorrectly attempt to refetch a module after a failed fetch. (158084942)
- Fixed `Iterator.prototype.flatMap` to properly handle iterators without a `return` method. (158783404)
- Fixed poor error messages for destructing null or undefined values. (159340067)
- Fixed `TypeError` messages to be clearer in `for-of` loops. (159814766)
- Fixed `TypeError` messages when calling class or function constructors without `new` to include the constructor name. (161152354)

##### Mathml

###### Resolved Issues

- Fixed rendering of unknown MathML elements so they now behave like `mrow` as required by the MathML Core specification. (148593275)
- Fixed `mfenced` elements to render like `mrow`. (161416576)

##### Media

###### Resolved Issues

- Fixed western Arabic numbers being displayed in the video viewer instead of eastern Arabic numbers. (141281469)
- Fixed WebVTT `line-height` to be `normal` by default, not `1`. (156633220)
- Fixed handling of null media accessibility caption profile. (159134245)
- Fixed hiding and resuming a webm video that sometimes causes a decoding error. (159508950)
- Fixed `MediaRecorder` to no longer fire erroneous error events when stopped immediately after track changes, aligning behavior with Chrome and closer to Firefox. (161124260)
- Fixed an issue where custom WebVTT caption text size settings did not propagate to cue child elements by moving the `font-size` definition into the cue’s shared `<style>` block. (162547969)

##### Networking

###### Resolved Issues

- Fixed an issue where `rel=preload` link headers with a nonce could trigger erroneous `Content-Security-Policy-Report-Only` violations due to the nonce not being copied into the fetch options. (75060055)
- Fixed an issue where apps that are mistakenly calling the WKWebView API `loadRequest` from a background thread may end up crashing.  (162070925)

##### Pdf

###### Resolved Issues

- Fixed an issue where the active PDF annotation hover effect would remain visible after moving the pointer away. (162951528)

##### Performance Api

###### New Features

- Added support for the Event Timing API. (160970604)
- Added support for Largest Contentful Paint web performance metric. (163498163)

##### Privacy

###### New Features

- Added support for Cookies Having Independent Partitioned State (CHIPS).  (154149154)

##### Rendering

###### New Features

- Added support for text shaping across inline boxes. (162430932)

###### Resolved Issues

- Fixed incorrect clipping of `position: fixed` and `position: sticky` content during view transitions. (154886047)
- Fixed computing static position to correctly size and locate an inset modified containing block. (155650719)
- Fixed alignment candidate to consider both first and last baseline item position. (155806707)
- Fixed the cross axis direction in flexbox to properly consider text directionality when the cross axis aligns with the inline axis to handle `direction` property and `flex-wrap: wrap-reverse` interactions. (156540996)
- Fixed `<button>` elements to use the last line as their baseline instead of the first line to ensure consistent alignment with `<br>` in the text. (157955703)
- Fixed orthogonal table cells so their `writing-mode` is no longer forced to match the table, allowing proper vertical layout. (158221827)
- Fixed an issue where exiting fullscreen could scroll to unscrollable areas. (158351089)
- Fixed an issue where the padding end incorrectly contributed to scrollable overflow when the inline direction was flipped.  (158529814)
- Fixed word breaking so that a hyphen followed by a Latin-1 Supplement character (U+00C0–U+00FF) correctly allows line breaks. (158942361)
- Fixed large inset box shadows to render correctly. (159888287)
- Fixed an issue where sticky elements at the edge of the viewport could disappear during rubber band scrolling. (160385933)
- Fixed an issue where selecting table cells could cause overlapping selections in flex and grid layouts. (160805174)
- Fixed flickering of elements with slow-painting content during view transitions. (160886647)
- Fixed an issue where elements with both `opacity` and CSS `filter` effects could render incorrectly. (161130683)
- Fixed an issue where elements with background images were not counted as contentful for Paint Timing. (161456094)
- Fixed scroll-to-text fragment highlights to automatically choose a contrasting foreground and background color to keep text readable on dark pages, while respecting custom `::target-text` styles. (163166782)
- Fixed an issue where fullscreen dialog backdrops did not properly extend below the address bar by extending the backdrop’s background into obscured inset areas. (163535684)
- Fixed an issue where slotted text nodes could become hidden when adjacent elements in a flex container changed their `display` property. (163571747)

###### Deprecations

- Removed UA styles for `h1` in `article`, `aside`, `nav`, and `section`. (151455566)

##### Svg

###### New Features

- Added support for the `repeatEvent` in SVG animations to align with the SMIL specification and match other browsers. (129919749)
- Added support for the `onbegin` event in the `SVGAnimationElement` IDL interface to align with the SVG animations specification. (130609424)
- Added support for the `async` attribute in `SVGScriptElement` to align behavior with `HTMLScriptElement` and other browsers. (151561361)
- Added support for the `hreflang` IDL attribute on `SVGAElement` to improve SVG link handling. (160133102)
- Added support for `type` attribute on the SVG `<a>` element. (160222206)

###### Resolved Issues

- Fixed an issue where a dynamic change in a CSS property of an SVG  element does not get reflected in the instances of the SVGElement. (98577657)
- Fixed an issue where `stop-color` incorrectly accepted hashless hex color values like `1234` by treating them as invalid to follow the spec. (119166640)
- Fixed `SVGMarkerElement` to correctly support the `SVG_MARKER_ORIENT_AUTO_START_REVERSE` value, aligning behavior with the spec and other browsers. (123453058)
- Fixed absolutely positioned SVG elements to correctly account for the containing block’s padding. (127608838)
- Fixed handling of `word-spacing` so that leading white space in SVG text correctly applies spacing at the start of a text box. (134941299)
- Fixed an issue where SVGs with a `0px` intrinsic width were ignored but now correctly respect degenerate aspect ratios and fall back to the `viewBox` aspect ratio. (156339128)
- Fixed handling semicolons at end of a `keySplines` value. (156511711)
- Fixed unnecessary rounding of `viewportLocation` in `'foreignObject'` layout. (156740732)
- Fixed `<svg>` elements to correctly calculate their intrinsic aspect ratio using `currentViewBoxRect()` when a `<view>` is referenced. (157445966)
- Fixed `SVGFETurbulenceElement` to correctly fallback `numOctaves` to `1` for invalid or negative values, aligning with the specification and other browsers. (158988528)
- Fixed an issue where SVG pattern `tileImage` could appear blurred or pixelated when zooming or printing. (159202567)
- Fixed `SVGStyleElement` so that its `type` and `media` attributes now use pure attribute reflection, matching `HTMLStyleElement`. (159358585)
- Fixed an issue where `<view>` element was not applied to the root element. (159705519)
- Fixed `SVGAElement` so that its `rel` and `relList` attributes now affect navigation behavior, including proper handling of `noopener`, `noreferrer`, and the new `opener` value, aligning SVG links with `HTMLAnchorElement` behavior. (160724516)

##### Security

###### Resolved Issues

- Fixed parsing of `require-trusted-types-for` in CSP to ensure `'script'` is only valid when followed by whitespace or end of buffer. (147760089)

##### Service Worker

###### Resolved Issues

- Fixed an issue where service worker downloads are not being saved to Downloads folder. (154501503)

##### Spatial Web

###### New Features

- Added WebGPU support for WebXR.  (157250939)

##### Storage

###### Resolved Issues

- Fixed WebSockets to correctly inherit storage access from the frame that created them. (147949918)
- Fixed `requestStorageAccess()` should always grant access when called from a same-site iframe. (156545395)
- Fixed Storage Access API to not be usable in insecure contexts. (157337423)
- Fixed `requestStorageAccess()` to reject with a `NotAllowedError`. (157446015)
- Fixed an issue where cross-origin navigations incorrectly preserved storage access. (158446697)
- Fixed an issue where dedicated workers could inherit storage access from their parent document, preventing them from sending cross-site requests with cookies. (158814068)

##### Tables

###### Resolved Issues

- Fixed collapsed table rows retaining nonzero height. (158276634)

##### Web Api

###### New Features

- Added support for fractional coordinates in `PointerEvent` and `TouchEvent` properties such as `clientX/clientY`, `pageX/pageY`, `offsetX/offsetY`, and `screenX/screenY`, while `MouseEvent` values remain whole. (9564176)
- Added support for `document.caretPositionFromPoint()`. (144101675)
- Added support for enforcing cookie name prefix checks in the `CookieStore` API to reject invalid `__Host-Http-` and `__Http-` names. (156373016)
- Added asynchronous URL error handling for Service Workers. (157769176)
- Added support for `document.activeViewTransition` to expose the current active view transition. (158089900)
- Added support in the Cookie Store API for handling `cookieStore.set` calls with an empty string `path`, defaulting to the current URL path. (158319959)
- Added support for the `scrollend` event. (158435888)
- Added support for the Navigation API. (158642673)

###### Resolved Issues

- Fixed an issue where the first `pointerdown` event was lost after triggering a context menu by right-clicking. (84787733)
- Fixed `window.opener` being incorrectly set to `null` when a site-isolated iframe navigated to a new site, ensuring opener relationships persist across frame migrations. (117269418)
- Fixed the ability to delete a cookie through Cookie Store API that was set through `document.cookie`. (142339417)
- Fixed Trusted Types to only verify event handler attributes for elements in the XHTML, SVG, and MathML namespaces, preventing incorrect checks on other namespaces. (147763139)
- Fixed reading the `mutable` field from the outer object instead of as a child of `notification`. (157475553)
- Fixed `location.protocol` setter to be restricted to HTTP(S) schemes. (157607342)
- Fixed `scroll` and `scrollend` events so they correctly fire on `<input type="text">` elements instead of their inner elements. (157880733)
- Fixed `CookieStore` methods to strip tabs and spaces from the names and values passed in. (157907393)
- Fixed JSON modules to fetch with an `application/json` Accept header. (158176845)
- Fixed an issue where `click` and `auxclick` event targeting does not follow pointer capture target override. (159477637)
- Fixed the order of `pointerup` and boundary events so that `pointerout` and `pointerover` fire before `pointerup` when a child element is attached under the cursor. (160913756)
- Fixed `element.scrollTo` and `element.scrollBy` so they correctly scroll text input fields by forwarding scroll operations to the inner text element. (160963921)
- Fixed `EventCounts` interface was not `maplike`. Enables use of methods such as `.forEach()`, `keys()`, and `entries()`. (160968888)
- Fixed an issue where `mousemove` events were still dispatched to removed `mouseover` targets instead of their parent element when the target was deleted. (161203639)
- Fixed missing `pointerenter` and `mouseenter` events when a child element moved under the mouse. (161362257)
- Fixed an issue where only one CSP violation report was sent for multiple enforced `require-trusted-types-for` directives. (161740298)
- Fixed Trusted Types incorrectly treating `null` or `undefined` policy return values as `null` instead of empty strings during `createHTML`, `createScript`, and `createScriptURL` operations. (161837641)
- Fixed `attachShadow()` to default to using the global custom element registry instead of the host’s registry when `customElementRegistry` is `null`. (161949419)
- Fixed `attachShadow()` to use the global custom element registry by default when `customElementRegistry` is `null`, aligning with the specification. (161949493)

###### Deprecations

- Removed support for the non-standard `overflowchanged` event. (71129110)

##### Web Extensions

###### New Features

- Added support for `browser.runtime.getVersion()` to retrieve the extension version from its manifest. (161742137)

###### Resolved Issues

- Fixed an issue where `onInstalled` getting called after every launch of Safari when opening a profile window.  (147491513)
- Fixed `sender.origin` parameter to match `window.location.origin`. (155884667)
- Fixed an issue where Safari extension popups could open scrolled down and some websites could flicker during scrolling. (155965298)
- Fixed an issue that caused the web page to crash when navigating to certain URLs with an extension enabled. (158180410)

##### Web Inspector

###### New Features

- Added Largest Contentful Paint entries to the Layout and Rendering timeline and events list in the Timelines tab.  (163600473)

###### Resolved Issues

- Fixed syntax highlighting for JavaScript features like template literals, private class elements, optional chaining, and others. (107619553)
- Fixed an issue where the Console truncated long string outputs. (124629101)
- Fixed an issue where DOM elements represented in the Console could not be selected. (157015598)
- Fixed an issue where newlines and indentation in HTML markup would show up in DOM node previews in the Console. (157225532)
- Fixed an issue that prevented scrolling of the Media details sidebar from the Elements tab. (157768497)
- Fixed an issue where accepting a completion suggestion for a shorthand property value would malform the combined value. (159107788)
- Fixed an issue where navigating the DOM tree using the keyboard would get stuck in a loop within certain subtrees. (159841729)
- Fixed an issue where the Sources tab won’t show contents of a script that contains a `for` statement with optional chaining in the test condition. (160617913)
- Fixed an issue where adding DOM attributes or node siblings did not work correctly when using the actions from the context menu. (161577627)

##### Webassembly

###### New Features

- Added support for `WebAssembly.Memory.prototype.toFixedLengthBuffer()` and `WebAssembly.Memory.prototype.toResizableBuffer()` to enable resizable WebAssembly memory buffers. (147437929)
- Added support for Wasm Memory buffer APIs. (159305098)
- Added support for Wasm JS String Builtins. (159679027)

##### Webdriver

###### New Features

- Added support for the “Set Storage Access” extension endpoint.  (158063011)
- Added support for new endpoints for setting storage access permission state and granting storage access to embedded frames for specific origins.  (158263193)

###### Resolved Issues

- Fixed the `navigate` endpoint in WebDriver to properly validate URLs against the current browsing context and set the default readiness state to `Interactive` to align with the specification. (157031091)
- Fixed an issue where element references nested inside `Array` or `Object` arguments were not properly extracted when executing scripts. (162571946)

##### Webgpu

###### New Features

- Added support for using `GPUTexture` objects as depth-stencil and resolve attachments in WebGPU render passes to match the specification. (159952306)

##### Webkit Api

###### New Features

- Added support for exporting `WebPage` content as `.png`, `.flatRTFD`, `.rtf`, and `.utf8PlainText` using SwiftUI `Transferable` APIs. (156225187)

##### Webrtc

###### New Features

- Added `encrypted` field to `RTCRtpHeaderExtensionParameters`. (159279401)

###### Resolved Issues

- Fixed camera indicator staying enabled even after ending a meeting or removing access to the camera. (152962650)

## See Also

- [Safari 26.3 Beta Release Notes](safari-26_3-release-notes.md)
  Released December 15, 2025 — 26.3 (20623.2.2)
- [Safari 26.1 Release Notes](safari-26_1-release-notes.md)
  Released November 3, 2025 — 26.1 (20622.2.11)
- [Safari 26.0 Release Notes](safari-26-release-notes.md)
  Released September 15, 2025 — 26.0 (20622.1.22)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-26_2-release-notes)*