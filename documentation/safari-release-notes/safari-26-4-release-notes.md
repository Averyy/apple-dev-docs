# Safari 26.4 Release Notes

**Framework**: Safari Release Notes

Released March 24, 2026 — 26.4 (20624.1.16)

#### Overview

Safari 26.4 is available for iOS 26.4, iPadOS 26.4, visionOS 26.4, macOS 26.4, macOS Sequoia, and macOS Sonoma.

##### Accessibility

###### Resolved Issues

- Fixed an issue where Voice Control commands could cause Safari to hang. (168364189)
- Fixed an issue where a button’s label would not update when a descendant’s `aria-hidden` attribute changed. (169012516)
- Fixed elements with `aria-controls` or `aria-expanded` and the `hidden` attribute to no longer appear in VoiceOver’s Form Control menu. (169499630)
- Fixed an issue where VoiceOver would announce with extra verbosity when moving onto the first item of a list on the webpage.  (169982730)
- Fixed an issue where controls with `aria-labelledby` pointing to visually-hidden elements could not obtain proper bounding box geometry through accessibility APIs. (170639492)

##### Animations

###### New Features

- Added support for threaded scroll-driven animations, improving performance. (168027635)

###### Resolved Issues

- Fixed incorrect overlap calculations for transform animations including `translate`, `scale`, and `rotate` properties. (88383253)

##### Browser

###### New Features

- Added Compact tabs back to Safari on macOS and iPadOS.  (148723398)

###### Resolved Issues

- Fixed Safari gesture support to prevent pages that should not be able to scroll, such as with explicit `overflow: hidden`, from unexpectedly scrolling.  (163660111)

##### Css

###### New Features

- Added support for a new blocks-in-inline layout approach. (19534458)
- Updated absolutely positioned boxes in scrollable containing blocks to allow alignment overflow in scrollable directions, in accordance with a recent CSS spec change. (162722820)
- Added support for `flow-tolerance` in CSS Grid Lanes. (164043151)
- Added support for a new grid layout integration system resolving a number of grid layout issues. (164406235)
- Added support for parsing and evaluating name-only `@container` queries that have no conditions, allowing named containers to match without explicit constraints. (164648718)
- Added support for an automatic initial value for `grid-auto-flow` in CSS Grid Level 3 to switch flow orientation based on `grid-template-rows` and `grid-template-columns` for grid lane layouts. (164791817)
- Added support for CSS `display: grid-lanes`. (164858227)
- Added support for `math-depth`. (167332590)
- Added support for the `cursor` property on the `::marker` pseudo-element. (168362833)

###### Resolved Issues

- Fixed an issue where `display: list-item` was incorrectly supported on `fieldset`. (95638460)
- Fixed an issue where `max-width` was not correctly applied to tables with fixed widths. (96554687)
- Fixed incorrect sizing and fragment URL handling for SVG images used in `-webkit-cross-fade()`. (106633417)
- Fixed `text-combine-upright` to properly ignore `letter-spacing` when composing text horizontally, aligning with the CSS Writing Modes specification. (116562622)
- Fixed an issue where `background-blend-mode` was not applied correctly when combined with `background-clip: text`. (120901898)
- Fixed table layout so that fixed horizontal margins on `<caption>` elements now contribute to the table’s minimum preferred logical width, preventing captions from causing narrower than expected tables. (120990942)
- Fixed incorrect width calculation for `positioned` elements using `box-sizing: border-box` with an `aspect-ratio`, ensuring borders and padding are not double-counted. (121500004)
- Fixed the UA style sheet to use `:focus-visible` instead of `:focus` for outline properties. (123155364)
- Fixed `HighlightRegistry` to remove its non-standard `constructor` and updated tests to use `CSS.highlights` while ensuring `Map.prototype` is properly restored after tampering. (125529396)
- Fixed handling of `@property` registration so that the `initial-value` descriptor can be optional. (131288198)
- Fixed baseline alignment for grid items by adding correct first baseline and last baseline row axis handling and properly accounting for baseline offsets.  (155967278)
- Fixed baseline handling for table cells when cell has no inflow children. (160774504)
- Fixed `getComputedStyle("top")` to correctly resolve percentage values for absolutely positioned elements inside inline containers. (161390162)
- Fixed an infinite style resolution loop when a `position-try` box was inside a `display: none` subtree. (161570947)
- Fixed `width`, `height`, `min-width`, `min-height`, `max-width` and `max-height` to apply CSS zoom at used-value time. (161848512)
- Fixed CSS zoom to scale `<iframe>` element contents. (162314059)
- Fixed `getBoundingClientRect` and `getClientRects` to return scaled lengths according to CSS zoom instead of unscaled values, aligning with the CSS Viewport specification. (162325730)
- Fixed scrolling behavior so that `scrollRectToVisible()` can bring fixed anchor-positioned boxes outside the viewport into view, improving keyboard navigation. (162378346)
- Fixed an issue where `@font-face` and `FontFace.family` failed when the font family name contained spaces, ensuring the family name is now treated as a plain string instead of being parsed. (162637501)
- Fixed `top`, `left`, `right`, and `bottom` to apply CSS zoom at used-value time (162663056)
- Fixed `margin` to apply CSS zoom at used-value time. (162907254)
- Fixed evaluation of `calc()` expressions to correctly apply the used `zoom` factor to length values, ensuring properties like `line-height` and box dimensions scale properly. (163141549)
- Fixed an issue where `calc(em)` values for unzoomed properties were incorrectly adjusted. (163267333)
- Fixed `position-area` normal alignment to align toward the non-auto inset when only one inset is auto, in accordance with recent CSS spec changes. (163317238)
- Fixed an issue where `calc()`  incorrectly treated margins as present. (163605539)
- Fixed `devicePixelRatio` so that page zoom now affects the main frame consistently with iframes, keeping their values synchronized. (163857955)
- Fixed incorrect underline positioning for `text-decoration` when inline box sides are trimmed. (163858721)
- Fixed an issue where CSS `@starting-style` entry animations were only applied on the first transition, especially when interacting with anchor positioning or position fallbacks. (163928932)
- Fixed an issue where fixed-positioned boxes using `position-area` were incorrectly included in the root scrollable containing block, ensuring they position correctly while still allowing overflow when appropriate. (163955483)
- Fixed `-webkit-line-clamp` so that it no longer propagates into `inline-block` children. (164488778)
- Fixed `line-height` to correctly scale font-relative units when text zoom is applied. (165073337)
- Fixed an issue where nested identical CSS `filter` effects were not rendered. (165163823)
- Fixed `element.clientWidth` and `element.clientHeight` to correctly include padding for `content-box` tables. (165515755)
- Fixed: Refactored the handling of block-level boxes inside inline boxes. (165523565)
- Fixed table column width distribution when a `colspan` spans mixed percentage and auto-width columns to properly respect percentage constraints. (165561401)
- Fixed an issue where `text-decoration: underline` appeared higher than expected when `text-box-trim` was applied to the root inline box. (165614136)
- Fixed `::first-line` pseudo-element to always use `inline` display to match the CSS Display specification. (166068698)
- Fixed an issue where `shape-outside` did not update correctly after web fonts loaded. (166336491)
- Fixed incorrect text selection ranges for truncated right-to-left content. (166944754)
- Fixed table height calculation to correctly account for captions with orthogonal `writing-mode`. (167220730)
- Fixed `counter-*` properties serialization order. (167518994)
- Fixed `outline-width` and `outline-offset` to follow updated computed style resolution rules. (167618367)
- Fixed the computed style resolution for `border-*-width` properties. (167689519)
- Fixed performance and correctness issues with inheritance in the modern CSS Zoom implementation. (167715972)
- Fixed the computed style resolution for the `column-rule-width` property. (167725940)
- Fixed `border-*-width`, `outline-width`, and `column-rule-width` so they now pixel snap correctly during CSS animations and transitions. (167763497)
- Fixed the disclosure triangle in `<details>` elements to use the larger `system-ui` font variant, preventing it from rendering as an emoji and ensuring consistent display across writing directions. (168364553)
- Fixed CSS rules within `@scope` not being applied to `<input>` and `<textarea>` elements. (169751338)
- Fixed an issue where empty CSS rules sharing a selector with non-empty rules could prevent dynamic style updates from applying correctly. (170348749)
- Fixed an issue where `padding-inline-end` was not included in the scrollable overflow for block containers. (170503510)
- Fixed an issue where `position-area` for elements in scrollable containers only used the initial scrollport bounds instead of the entire scrollable area. (170503694)
- Fixed an issue where CSS transitions were incorrectly triggered when `border-width` computed values did not change, causing unexpected layout shifts. (170657059)
- Fixed an issue where absolutely-positioned elements inside inline containers did not correctly account for the margin of a preceding block when determining their static position. (170934098)
- Fixed an issue where multi-column layout rendered columns at incorrect positions for some fonts. (171016194)

###### Deprecations

- Removed the `FontFaceSet` constructor from the CSS Font Loading API as it was deemed unnecessary, aligning with the CSSWG resolution. (132031306)

##### Canvas

###### Resolved Issues

- Fixed `ImageBitmap` created from SVG image sources to correctly honor the `flipY` orientation. (83959718)

##### Clipboard

###### Resolved Issues

- Fixed an issue where using the “Copy Image” context menu in Safari would also copy the image URL, causing some sites to paste the URL instead of the image. (76598990)

##### Editing

###### Resolved Issues

- Fixed incorrect text selection when dragging across pseudo elements. (142905243)
- Fixed an issue on iOS 26 where the edit menu would not appear when tapping inside an already-focused text field that had a looping `content` animation. (164290305)
- Fixed an issue where focusing a hidden editable element would incorrectly display the text cursor and selection at full opacity. (165489471)
- Fixed a regression where dragging to select text would stop scrolling when the cursor left the window. (169983104)

##### Encoding

###### Resolved Issues

- Fixed incorrect handling of invalid UTF-8 sequences in the `TextDecoder` streaming decoder to properly manage partial sequence buffers. (166583808)

##### Events

###### Resolved Issues

- Fixed an issue where `mouseleave` and `mouseout` events were not dispatched when a window moved out from under a stationary cursor. (161493924)

##### Forms

###### Resolved Issues

- Fixed an issue where input fields did not display user input while typing. (163613957)
- Fixed an issue where `input[type="search"]` fields with `appearance: none` incorrectly reserved space for the datalist dropdown button. (166754216)
- Fixed an incorrect fallback for the menu style for empty lists, improving readability and correctness. (167662316)

##### Html

###### New Features

- Added support for using the `min()`, `max()`, and `clamp()` math functions in the `sizes` attribute of `<img>` elements. (167526292)

###### Resolved Issues

- Fixed an issue where nested `about:blank` frames were incorrectly treated as self-referencing, preventing them from loading. (148373033)
- Fixed `shadowrootcustomelementregistry` attribute serialization to correctly compare ShadowRoot and document registries. (165476421)
- Fixed `HTMLImageElement.currentSrc` to return an empty string for `<img src="">` instead of resolving to the document base URL. (167229274)

##### Images

###### Resolved Issues

- Fixed image uploading to not transcode images when `accept="image/*"` is specified. (166124206)

##### Javascript

###### New Features

- Added support for iterator sequencing.  (167633152)

###### Resolved Issues

- Fixed `Date` constructor overflow handling so that invalid day values now return `NaN`. (155776209)
- Fixed `Intl.DateTimeFormat` to throw a `RangeError` for legacy non-IANA timezones, aligning behavior with TC39 standards. (156857252)
- Fixed `Intl.Locale.prototype.getWeekInfo()` to remove the `minimalDays` property for compliance with the specification. (165083619)
- Fixed `Intl.NumberFormat` to properly apply `minimumFractionDigits` and `maximumFractionDigits` to ensure currency and compact notations behave correctly. (165875014)
- Fixed `%TypedArray%.prototype.includes` to correctly check that the `index` is less than the array length, aligning its behavior with ECMA-262. (167183441)
- Fixed async functions without any `await` to inline their bodies for performance and corrected async stack traces with a single function entry for exceptions thrown from or through async functions. (167254635)

##### Mathml

###### New Features

- Added support for CSS size containment in MathML elements using `contain-intrinsic-inline-size` and `contain-intrinsic-block-size`. (166323213)
- Added support for `math-style` and `math-shift` to animate as discrete values. (167369164)

###### Resolved Issues

- Fixed default MathML rule thickness to use the font’s `underlineThickness` metric with a zero fallback. (164693673)
- Fixed `mpadded` elements in RTL (`dir="rtl"`) to respect `lspace`. (164740784)
- Fixed an issue where empty `<msqrt>` radical operators in MathML were not painted correctly. (164776629)
- Fixed MathML `<mpadded>`, `<mfrac>`, `<munderover>`, `<mover>` and `<mspace>` elements not updating layout when attributes like `width`, `height`, `depth`, `lspace`, and `voffset` etc. changed. (164797996)
- Fixed MathML boolean attributes so they are now compared ASCII case-insensitively. (164819048)
- Fixed incorrect positioning of `mpadded` content in right-to-left mode. (166045517)
- Fixed an issue where `<msqrt>` or `<mroot>` elements did not update their radical operators when children were dynamically added or removed. (166556627)
- Fixed `<mpadded>` so that percentage values for `width`, `height`, and `depth` attributes are treated as absent and use content dimensions as defaults, matching the MathML Core specification. (167350169)

##### Media

###### New Features

- Added support for a pop-up menu on macOS that allows users to select and manage caption style profiles. (163067314)

###### Resolved Issues

- Fixed an issue where `<video>` poster images were incorrectly double-scaled when `zoom` was applied by using the cached intrinsic poster size without reapplying zoom. (150976146)
- Fixed dispatching of enter and exit events on `TextTrackCue` and `VTTCue` objects with no associated track, aligning with other browsers. (160195643)
- Fixed an issue where changing an `HTMLMediaElement` volume from `0` to `0` did not activate the audio session or update the sleep disabler. (161691743)
- Fixed an issue where videos would freeze on the first frame when transitioning from encrypted to clear content by ensuring the decoded buffer maintains at least 100ms of frames even when the next frame is far in the future. (162234566)
- Fixed an issue where the mute button disappeared in macOS inline videos with adjustable sizes. (162897286)
- Fixed playback of `application/ogg` blob media. (163119790)
- Fixed an issue where Video Viewer UI elements overlapped or exited unexpectedly. (164051864)
- Fixed an issue where empty `<track>` elements prevented media from advancing its readyState and blocked `play()` calls. (164125914)
- Fixed an issue where `HTMLMediaElement` did not correctly detect new audio or video tracks causing Safari to pause video when leaving a tab. (164514685)
- Fixed a crash in `AudioData.copyTo()` when copying the last channel of 3-channel audio. (164730320)
- Fixed an issue where the `ended` event for Media Source Extensions might never fire by ensuring buffered ranges update correctly and playback gaps are observed even when the video does not start at time zero. (165430052)
- Fixed an issue where caption previews were not shown in the default media controls. (165931046)
- Fixed the caption menu’s `On` option to correctly enable the highest-scoring text track and mark the appropriate language as checked in the subtitle menu. (166158394)
- Fixed `parseSequenceHeaderOBU` to return an `AV1CodecConfigurationRecord`, fully decode the Sequence Header OBU, and capture the complete color profile. (166439682)
- Fixed an issue where the macOS inline media controls timeline scrubber overlapped the right container buttons. (167634241)
- Fixed an issue where `WebCodecs VideoDecoder` could output H264 frames in the wrong order. (168046597)
- Fixed an issue where the mute button and volume slider overlapped in the video player controls when using a right-to-left language. (170174446)

##### Networking

###### New Features

- Added support for WebTransport.  (165721145)

###### Resolved Issues

- Fixed a regression where `fetch()` would throw a `TypeError` when using `targetAddressSpace: 'loopback'` for localhost requests. (166574523)

##### Privacy

###### Resolved Issues

- Fixed an issue where cross-browser Private Click Measurement recorded attribution entries even when “Allow privacy-preserving measurement of ad effectiveness” was disabled.  (170669444)

##### Rendering

###### Resolved Issues

- Fixed over-aggressive clipping of child layers in multicolumn layouts to prevent visual overflow issues with `position: relative` elements and `transform:scale()` text. (126413036)
- Fixed unreadable Scroll-to-Text-Fragment highlights on dark pages. (126539910)
- Fixed an issue where auto-positioned absolutely positioned descendants were not always marked for layout when their parent’s border box moved. (131806062)
- Fixed an issue where positioned, transformed, or opacity-altered `<img>` elements with HDR JPEG gainmaps would incorrectly render in SDR. (156858374)
- Fixed an issue on iPadOS where closing the sidebar or resizing the window could cause the page to remain zoomed in by recalculating the target scale to automatically match the new minimum scale. (157676989)
- Fixed an issue where fixed positioned elements were not rendered correctly in right-to-left pages using the `vertical-rl` writing mode. (161712734)
- Fixed a performance issue in  layouts with long `pre` blocks and `word-break: break-all` by including whitespace in overflow width calculations. (162695099)
- Fixed an issue where overconstrained sticky elements were not properly adjusting their insets when the sticky box rectangle was larger than the viewport. (163654023)
- Fixed an issue where applying `word-spacing` to `::first-line` could cause other lines to disappear. (163779992)
- Fixed inconsistent text layout when using `list-style-type` by ensuring outside list markers do not affect intrinsic width calculations. (164650313)
- Fixed incorrect min and max width calculations for block-level boxes inside inline content. (166157696)
- Fixed an issue where color fonts could affect the color of other DOM elements. (166631312)
- Fixed an issue where `getClientRects` returned an incomplete list of rectangles for inline boxes containing block elements. (167209147)
- Fixed `<col>` elements with `span > 1` not applying their width to all spanned columns during table layout, aligning behavior with other browsers. (167225435)
- Fixed table layout `min-width` distribution for spanning cells with mixed `percent`, `fixed`, and `auto` columns. (167684748)
- Fixed: Improved drop-shadow and blur effects rendering performance. (169472992)

##### Svg

###### New Features

- Added support for the `lighter` operator in `SVGFECompositeElement` IDL to align with the Compositing and Blending specification. (166704079)

###### Resolved Issues

- Fixed an issue where `stroke-dasharray` incorrectly propagated to SVG markers when explicitly marked as ‘0’. (46607685)
- Fixed an issue where `foreignObject` elements in SVG incorrectly allowed margin collapsing. (97208795)
- Fixed SVG intrinsic sizing and `preferredAspectRatio()` to correctly transpose dimensions for vertical writing modes. (103262534)
- Fixed animation of the `stop-color` attribute on `<stop>` elements. (109823555)
- Fixed an issue where dynamically changing `marker-start`, `marker-mid`, or `marker-end` attributes on SVG elements did not trigger re-rendering. (130678384)
- Fixed tiling gaps in CSS reference filters using `<feDisplacementMap>`. (135448018)
- Fixed `SVGLength` parsing to correctly return the initial value when encountering parser errors or invalid values. (136102554)
- Fixed an issue where `SVGImage` did not respect system dark mode changes. (140661763)
- Fixed breaking SVG resource referencing when removing a resource which shares its `id` with other resources. (147015037)
- Fixed behavior to avoid incorrect pruning of SVG mask subtrees based on visibility. (157729389)
- Fixed an issue where SVG `animateTransform` animations on hidden elements were triggering full-page rendering updates each frame. (159647563)
- Fixed `SVGLength.prototype.valueAsString` to throw a `SyntaxError` when assigned an empty string. (165429393)
- Fixed `SVGLength` percentage resolution for elements inside non-instanced `<symbol>` elements. (165431008)
- Fixed an issue where lengths with leading or trailing whitespace failed to be parsed. (165501190)
- Fixed an issue where `SVGLength.value` did not update for font-relative units (e.g., `ch`, `em`) after changes to `writing-mode`. (166190252)
- Fixed missing gradient fills when using paint-order `stroke fill`. (166997630)
- Fixed embedded `<svg>` elements in `<img>` without an explicit `viewBox` to synthesize `preserveAspectRatio='none'` so the SVG stretches to fill the container. (167121931)
- Fixed the `<stop>` element `offset` attribute in SVG to reject invalid values with trailing characters and correctly fall back to `0`. (167356988)
- Fixed the transform order for `clipPath` elements so that the bounding box is scaled correctly before applying the local transform. (167417135)
- Fixed `<clipPath>` to clip to its `<use>` child element based on the visibility of the `<use>` target element. (167491519)
- Fixed incorrect rendering when combining `markerUnits=strokeWidth` with `vector-effect=non-scaling-stroke`. (167493417)
- Fixed displaying an SVG filter referencing an element with a huge stroke. (167516452)
- Fixed hit testing for overlapping `<text>` and `<tspan>` elements in SVG. (167691166)
- Fixed rendering of dimensionless SVG images. (168176556)

##### Spatial Web

###### Resolved Issues

- Fixed auto-dimming for playback sessions in visionOS. (163824973)

##### Storage

###### Resolved Issues

- Fixed an issue where IndexedDB databases might have mismatched metadata version and database name encoding format. (163219457)

##### Text

###### New Features

- Added support for parsing and computing `font-size: math` with scaling logic. (163323845)

##### Wkwebview

###### Resolved Issues

- Fixed an issue where `WKWebView` apps with a toolbar would fail to display a top scroll edge effect when relying on automatic content inset adjustments. (161370795)

##### Web Api

###### New Features

- Added support for `ReadableStream.getIterator()` and the `[@@asyncIterator]` methods to enable iteration over streams. (96318671)
- Added support for auxiliary mouse button values in `MouseEvent.button`. (137592588)
- Added support for the Keyboard Lock API. (161422221)
- Added support for using readable byte streams as `fetch` request and response bodies and enabling synchronous start behavior. (162107262)
- Added support for reading `Blob.stream()` with a BYOB (`getReader({mode:'byob'})`) reader. (164307723)
- Added support for `ReadableByteStream`. (164877711)
- Added support for upgrading elements in `CustomElementRegistry.prototype.initialize`. (165045530)
- Added support for the `customelementregistry` content attribute and handling of `null` `customElementRegistry` values in `document.createElement`, `document.createElementNS`, and `element.attachShadow`. (165096267)
- Exposed the`MediaDeviceInfo` interface  in secure contexts only. per the web specification. (165318702)
- Added support for Resource Timing Level 3 attributes `finalResponseHeadersStart` and `firstInterimResponseStart` to capture timing for both interim (1xx) and final HTTP response headers for proper measurement of events like 103 Early Hints. (167073003)

###### Resolved Issues

- Fixed `DeviceMotionEvent` and `DeviceOrientationEvent` interfaces so that they only show up in secure contexts just like the corresponding events and made `ondevicemotion` and `ondeviceorientation` enumerable, aligning with the specification. (44804273)
- Fixed an issue where `IntersectionObserver` computed the root rectangle incorrectly when overflow clipping was present. (117143395)
- Fixed Trusted Types to correctly send CSP violation reports when a default policy returns an invalid `javascript:` URL or throws an exception. (160960418)
- Fixed `Element.requestFullscreen` on iOS to correctly reflect hardware keyboard attachment state during fullscreen sessions and exit automatically when the keyboard is detached. (161429040)
- Fixed event ordering and committed promise timing for intercepted `Navigation API` traverse navigations. (161445256)
- Fixed the processing order of Trusted Types for DOM attribute setting. (162143148)
- Fixed `NavigateEvent` to correctly fire an `AbortSignal` when a navigation is aborted. (163957784)
- Fixed `NavigateEvent.sourceElement` to correctly reference elements from different browsing contexts. (163962362)
- Fixed the Navigation API to prevent scripts from flooding the system with navigation requests. (164510890)
- Fixed an issue where `scroll-margin` from `IntersectionObserver` incorrectly applied to scrollers inside cross-origin iframes. (164994009)
- Fixed `ReadableStream` and `WritableStream` to correctly pass abort and cancel reasons and improved `WebTransport` stream handling. (165474756)
- Fixed `DigitalCredential` behavior to make user mediation implicitly required. (165597827)
- Fixed an issue where the Big5 `TextDecoder` failed to recover and emit ASCII characters after encountering an invalid leading byte. (166672674)
- Fixed `MouseEvent.offsetX` and `MouseEvent.offsetY` so they are now calculated relative to the padding edge of the target element. (168015965)
- Fixed an issue where pointer events would fail to dispatch after a parent view’s custom gesture recognizer blocked `touchesEnded:` or `touchesCancelled:`. (169109808)
- Fixed an issue where JavaScript-to-native object serialization could fail entirely when any individual key-value pair could not be serialized, causing broken workflows in some apps. (171547386)

##### Web Authentication

###### New Features

- Added support for the WebAuthn PRF extension that maps to the CTAP `hmac-secret` extension, enabling credential-bound cryptographic secrets for both credential creation and authentication flows with security keys. (113572812)
- Added support for WebAuthn CTAP PIN/UV Auth Protocol 2 using HKDF-SHA-256 for key derivation, enabling proper FIPS-compliant authenticators. (157884782)

###### Resolved Issues

- Fixed an issue where the `excludeCredentials` list was not sent over CTAP when its size was 1. (164546088)

##### Web Extensions

###### Resolved Issues

- Fixed an issue where `window.open()` calls from web extensions would incorrectly open “about:blank” instead of the intended URL by ensuring each extension URL loads in a fresh tab configuration.  (143901129)

##### Web Inspector

###### New Features

- Added support for capturing `console.screenshot` images within a `Worker`, including handling of `ImageData`, `ImageBitmap`, `OffscreenCanvas`, various `CanvasRenderingContext` types, and valid base64 `data:` URLs. (98223234)
- Added support for starting and stopping `<canvas>` recordings from the `console` within a `Worker` using `console.record()` and `console.recordEnd()`. (98223237)
- Added a context menu option to DOM nodes in the Elements Tab to copy pretty-printed HTML. (102125455)
- Added a setting to toggle the visibility of User Agent stylesheet rules in the Elements tab.(164265183)
- Added support for showing actual composited layer snapshots in the 3D Layers view. (164977594)
- Added support in the Web Inspector Timelines Heap view to display the dominator object, if any, when viewing the shortest GC path. (165177746)
- Added support for auto-completion of `sideways-lr` and `sideways-rl` values for the `writing-mode` CSS property. (165777054)
- Added support for auto-completion of `grid-lanes` and `inline-grid-lanes` values for the `display` CSS property. (165873256)
- Added support for Web Inspector to fetch CSS property keyword completions based on feature support. (165914089)
- Added support for displaying `Order Numbers` in CSS Grid and CSS Grid Lanes overlays in Web Inspector, including new UI settings for toggling order number visibility. (166648769)
- Added Grid Inspector support for visualizing gaps between items arranged by Grid Lanes. (166984079)

###### Resolved Issues

- Fixed incorrect breakpoint and search result positions in the Web Inspector after pretty-printing inline scripts containing multi-line template literals. (29417859)
- Fixed the Styles sidebar filter in Web Inspector to be case-insensitive. (36086981)
- Fixed an issue where a large number of search results in the Search tab would freeze Web Inspector. (49234522)
- Fixed an issue where the Console tab search bar in Web Inspector would disappear when the window was too narrow. (50922509)
- Fixed an issue where CSS properties added to new rules were not applied and were marked as invalid. (103548968)
- Fixed context menu items to rename `Copy HTTP Request` and `Copy HTTP Response` to `Copy HTTP Request Headers` and `Copy HTTP Response Headers` for clarity. (117708766)
- Fixed incorrect grid track sizing display in the Web Inspector when using CSS custom properties. (141709306)
- Fixed an issue in the Console where the count of identical consecutive messages could be wrong. (162612099)
- Fixed an issue where breakpoints and search results in Web Inspector could point to the wrong location after a previously formatted source file was reopened in an unformatted state. (165059693)
- Fixed an issue where the Sources navigation sidebar could be empty when reloading the page. (166141968)
- Fixed timestamp formatting in the Web Inspector to remove unnecessary trailing `.0` values for readability. (166500013)
- Fixed item order labels in the Web Inspector grid and flex overlays to remove the `#` symbol, changing from `Item #N` to `Item N`. (166767949)
- Fixed an issue where the text filter in the Sources tab did not apply to the Local Overrides and Console Snippets sections. (169804196)
- Fixed a performance issue in the Web Inspector search panel by limiting initial results to 100 per resource and adding UI controls to load more or all results, reducing unnecessary UI work for large queries. (169804865)
- Fixed an issue where the search bar settings icon disappeared when the search field was focused. (169997100)

##### Webassembly

###### Resolved Issues

- Fixed `Error.isError(WebAssembly.Exception)` to correctly return `false` based on current WebAssembly spec semantics. (167110254)

##### Webgpu

###### Resolved Issues

- Fixed incorrect handling of some PNG pixel formats in WebGPU. (158797747)

##### Webrtc

###### New Features

- Added support for capturing audio from multiple microphones on macOS with `getUserMedia` while managing echo cancellation and dynamically migrating existing captures to non-VPIO units. (163945062)
- Added network slicing support for WebRTC on iOS.  (165202088)

###### Resolved Issues

- Fixed `RTCDataChannelInit` to support `[EnforceRange]` on the `maxPacketLifeTime` and `maxRetransmits` fields to align with the WebRTC specification. (133630397)
- Fixed an issue on macOS where calling `getUserMedia` with echo cancellation disabled could unintentionally affect existing audio tracks. (151143554)
- Fixed `MediaStreamTrackProcessor` to respect `track.enabled = false`. (165199900)
- Fixed an issue where `RTCDataChannel` close events did not fire when `RTCPeerConnection` was closed. (165617848)
- Fixed `RTCConfiguration.iceServers` to be a non-optional sequence with an empty array as the default, improving spec compliance and ensuring `RTCPeerConnection` behaves correctly when `iceServers` is undefined. (167607478)

## See Also

- [Safari 26.5 Release Notes](safari-26_5-release-notes.md)
  Released May 11, 2026 — 26.5 (20624.2.5)
- [Safari 26.3 Release Notes](safari-26_3-release-notes.md)
  Released February 11, 2026 — 26.3 (20623.2.7)
- [Safari 26.2 Release Notes](safari-26_2-release-notes.md)
  Released December 12, 2025 — 26.2 (20623.1.14)
- [Safari 26.1 Release Notes](safari-26_1-release-notes.md)
  Released November 3, 2025 — 26.1 (20622.2.11)
- [Safari 26.0 Release Notes](safari-26-release-notes.md)
  Released September 15, 2025 — 26 (20622.1.22)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-26_4-release-notes)*