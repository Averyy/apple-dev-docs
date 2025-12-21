# Safari 26.0 Release Notes

**Framework**: Safari Release Notes

Released September 15, 2025 — 26.0 (20622.1.22)

#### Overview

Safari 26.0 is available for iOS 26, iPadOS 26, visionOS 26, macOS 26, macOS Sequoia, and macOS Sonoma.

##### Accessibility

###### Resolved Issues

- Fixed `aria-expanded` attribute support on navigation links. (141163086)
- Fixed presentational images with empty `alt` attributes to be ignored by assistive technology, even when additional labeling attributes are set. (146429365)
- Fixed `<figcaption>` within a `<figure>` element to only contribute to the accessible name of an `<img>` element if the image lacks other labeling methods like `alt`, ARIA attributes, or the `title` attribute. (150597445)
- Fixed handling of invalid values for `aria-setsize` and `aria-posinset` according to the most-recent revision of the ARIA specification. (151113693)
- Fixed VoiceOver reading “Processing page %infinity” when loading large pages. (152617082)
- Fixed VoiceOver failing to output newlines in certain circumstances when using caret navigation. (154368379)
- Fixed an issue where dynamic changes to iframe display properties could cause the iframe’s scroll view to incorrectly become the accessibility root, preventing assistive technologies from accessing content outside the iframe.  (156440342)
- Fixed CSS `content` `alt` text when used on an element to be announced by VoiceOver.  (156666741)

##### Animations

###### New Features

- Added support for `animation-range`, `animation-range-start`, `animation-range-end`, and `animation-timeline` properties for `::marker`. (154021467)

##### Browser

###### New Features

- Added support for SVG icons.  (113567909)
- Added support for reporting a website compatibility issue in Safari.  (133791139)
- Added support for `data:` URL icons. (143967312)

###### Resolved Issues

- Fixed keyboard typing to cancel voice dictation.  (152597958)
- Fixed: Safari now reports a frozen OS version in its user agent string on iOS 26 and iPadOS 26, showing the last version released before iOS 26.  (156170132)

##### Css

###### New Features

- Added support for `overflow-block` and `overflow-inline`. (70579028)
- Added support for the `margin-trim: block inline` syntax for trimming in both directions. (141784069)
- Added partial support for the `dynamic-range-limit` property: `standard` and `no-limit`, non-animatable. (144486108)
- Added support for `contrast-color()`. (144630635)
- Added support for Scroll-driven Animations. (144887859)
- Added support for allowing declarations directly inside `@scope` rule without a style rule ancestor. (145101643)
- Added support for `text-wrap-style: pretty`. (145577976)
- Added support for CSS Anchor Positioning. (145681750)
- Added support for the self-alignment properties `align-self` and `justify-self` in absolute positioning. (145689547)
- Added support for CSS `progress()` function.  (145717727)

###### Resolved Issues

- Fixed `cursor: pointer` not appearing on an `<area>` element used in conjunction with an `<img usemap="...">` element. (74483873)
- Fixed: Apply space from align-content when grid container and rows have definite sizes during column sizing (85252183)
- Fixed `<frame>` and `<frameset>` to always be in-flow and non-floating. (102670652)
- Fixed grid sizing with inline-size containment and auto-fit columns is incorrectly sized. (108897961)
- Fixed “inherit” as a variable substitution fallback when setting custom property. (136463977)
- Fixed content skipped with `content-visibility: auto` to be findable.  (141237620)
- Fixed an issue wrapping an SVG at the end of a line when using `text-wrap: balance`. (141532036)
- Fixed `@font-face font-family` descriptor to not allow a list of values. (142009630)
- Fixed the computed value of a float with absolute positioning to be `none` when there is no box. (144045558)
- Fixed buttons to not have `align-items: flex-start` by default. (146615626)
- Fixed style container query on `:host` CSS pseudo-class to be correctly applied to slotted elements. (147684247)
- Fixed `@scope` to create a style rule with a nested context. (148101373)
- Fixed changing `content-visibility` from `visible` to `hidden` to repaint correctly. (148273903)
- Fixed an issue where float boxes, selections, and carets were incorrectly painted inside skipped subtrees. (148741142)
- Fixed incorrect `getBoundingClientRect()` inside skipped subtree on an out-of-flow positioned box. (148770252)
- Fixed making `<pre>` and other elements use logical margins in the User-Agent stylesheet. (149212392)
- Fixed `space-around` and `space-evenly` to fallback to `safe center` for `align-content`. (153403381)
- Fixed the serialization of `<color>` custom properties to provide the used value. (153675017)

##### Canvas

###### New Features

- Added HDR support in WebGPU Canvas.  (128164668)

###### Resolved Issues

- Fixed re-drawing a canvas with relative width when the parent element is resized. (121996660)
- Fixed `getContext('2d', { colorSpace: 'display-p3' })` in iOS Simulator. (151188818)

##### Content Blockers

###### New Features

- Added support for `unless-frame-url`. (139456686)
- Added support for the request-method content blocker trigger field. (148474901)
- Added support for `isContentRuleListRedirect`.  (150692793)

##### Dom

###### Resolved Issues

- Fixed the serialization of `CDATASection` nodes in HTML. (150739105)

##### Device Management

###### New Features

- Added support for a managed device to have a folder of managed bookmarks.  (133974240)
- Added support for a managed device to have managed new tab or new window page (home page, blank page, extension new tab page).  (134425148)

##### Editing

###### New Features

- Added support for rendering native selection UI inside scrolled content.  (136988607)

###### Resolved Issues

- Fixed the selection UI to be clipped in overflow scrolling containers.  (9906345)
- Fixed selection issues caused by `<br>` elements between absolute positioned elements.  (123637358)
- Fixed selection failing to update during auto or keyboard scrolling. (144581646)

##### Forms

###### Resolved Issues

- Fixed form associated ElementInternals always reporting a `customError` when using `setValidity`. (115681066)
- Fixed `setValidity` of `ElementInternals` to handle missing optional `anchor` parameter. (123744294)
- Fixed updating scrollbar appearance correctly for the page and `<textarea>` elements. (151496190)
- Fixed programmatically assigned File objects to display the correct filename in `<input>` elements, even without a file path. (152048377)
- Fixed labels inside `<select>` elements to behave consistently with other browsers by using standard attribute matching instead of quirk mode handling.  (152151133)
- Fixed allowing the custom element itself to be passed as validation anchor in the `setValidity()` API. (154303420)
- Fixed the intrinsic size of number inputs when the spin button width is a percentage value. (154680747)

##### Http

###### New Features

- Added Safari support for WebSocket over HTTP/2 and HTTP/3.  (104137162)

##### Images

###### New Features

- Added support for HDR Images on iOS 26, iPadOS 26, macOS 26 and visionOS 26.  (134397601)

###### Resolved Issues

- Fixed zoomed `<img>` to not cause unwanted rounding of `width` and `height`. (150473104)

##### Javascript

###### New Features

- Added support for Regular Expression Pattern Modifiers. (131580854)
- Added support for the `notation` option for `Intl.PluralRules`.  (152149896)
- Added support for `Intl.Locale.prototype.variants` getter. (153939662)

###### Resolved Issues

- Fixed `Array.prototype.pop` to throw an exception when the array is frozen. (141805240)
- Fixed performance of `Math.hypot()` that was significantly slower than `Math.sqrt()`. (141821484)
- Fixed `RegExp#[Symbol.search]` to throw `TypeError` when `lastIndex` isn’t writable. (146488846)
- Fixed `Array#indexOf` and `Array#includes` to treat `+0` and `-0` as the same value. (148472519)
- Fixed iterator helpers incorrectly closing iterators on early errors. (148774612)
- Fixed `Iterator.prototype.reduce` failing with an `undefined` initial parameter. (149470140)
- Fixed: Aligned `f() = 1` behavior with other engines when not using strict mode. (149831750)
- Fixed nested negated classes resulting in incorrect matches. (151000852)
- Fixed DateTime string parsing for ISO8601 inputs. (153679940)
- Fixed `toIntegerOrInfinity` to truncate negative fractional values to `+0.0`. (153939418)
- Fixed the order of function’s special properties returned by `Object.keys` and `Object.entries`. (155607661)

##### Lockdown Mode

###### New Features

- Added support for more web fonts in Lockdown Mode by replacing a fragile hard-coded allowlist with a safe parser that handles a broader range of fonts without compromising security. (149314760)

##### Media

###### New Features

- Added support for in-band tracks in MSE.  (129295806)
- Added support for `detachable` MediaSource objects to allow for seamless switching between objects attached to a media element.  (129298010)
- Added support for MediaSource prefers DecompressionSession. (142761051)
- Added support for WebCodec’s AudioEncoder and AudioDecoder. (142916087)
- Added support for ALAC and PCM audio in MediaRecorder. (144145333)

###### Resolved Issues

- Fixed picture-in-picture to exit when the video element is removed. (123869436)
- Fixed MP4 seeking with b-frames to prevent out-of-order frame display by suppressing frames with earlier presentation timestamps following the seek point. (140415210)
- Fixed media elements on iPadOS to support the volume being changed by web developers, similar to macOS and visionOS. The `:volume-locked` pseudo-class can continue to be used for feature detection.  (141555604)
- Fixed seeking or scrubbing not always seeking to the time requested. (142275903)
- Fixed stale audio buffer data after seeking when playing sound through an AudioContext. (146057507)
- Fixed subtitle tracks with no `srclang` to be shown with the correct label. (147722563)
- Fixed MediaSession to handle SVG icons with subresources. (150665852)
- Fixed `MediaCapabilitiesDecodingInfo.configuration` to be correctly populated even when `.supported` is `false`. (150680756)
- Fixed video elements with WebM object URLs causing MediaError code 2. (151234095)

##### Networking

###### New Features

- Added support for `<link rel=dns-prefetch>` on iOS while improving privacy on macOS.  (144699889)

##### Pdf

###### Resolved Issues

- Fixed “Open with Preview” button to open a PDF in the Preview app. (148680145)

##### Privacy

###### New Features

- Added support for preventing fingerprinting for known tracking scripts.  (134227067)

##### Rendering

###### Resolved Issues

- Fixed `overflow: hidden` to not clip `filter: drop-shadow()`. (72205047)
- Fixed a `list-style-position: inside` list item marker to be rendered as the first child of the list item. (79587134)
- Fixed using `setDragImage` with a fixed-position element, so that the drag preview bitmap includes the correct content. (90120656)
- Fixed an issue to allow images in scroll containers to load when they are near the viewport rather than when they are intersecting the viewport. (118706766)
- Fixed CSS filters to establish a containing block like transform does. (119130847)
- Fixed a disappearing stretched image in a vertical flexbox layout. (135897530)
- Fixed CSS gradient interpolation for “longer hue” gradients when an end color stop is omitted. (142738948)
- Fixed `will-change: view-transition-name` to create a stacking context and a backdrop root. (146281670)
- Fixed `will-change: offset-path` to create a stacking context and a containing block. (146292698)
- Fixed `<datalist>` dropdowns not displaying option labels.  (146921617)
- Fixed the text indicator sometimes getting clipped during a bounce animation. (147602900)
- Fixed geometry values inside `content-visibility: hidden` subtrees. (148553259)
- Fixed not marking `content-visibility: hidden` content for layout when targeting `content-visibility: auto`. (148663896)
- Fixed incorrect `ruby` annotation positioning in `sideways-lr`. (148713073)
- Fixed: Prevented hit testing content inside a skipped subtree. (148741508)
- Fixed an issue where `feMerge` incorrectly positioned HTML elements when merging the same `feMergeNode` multiple times. (149431216)
- Fixed `box-shadow` with spread on a border-radius box to scale the radii correctly. (149490613)
- Fixed an issue in determining when a flex item should be used for percentage resolution during intrinsic width computation. (149615295)
- Fixed an issue causing a `<canvas>` element to disappear for one frame if a view transition occurs. (149709642)
- Fixed `<div contenteditable>` within an `<iframe>` not scrolling into the viewport on receiving focus for the second time. (150521759)
- Fixed invisible `<audio>` controls when transformed due to incorrect coordinate space calculations for clipped child elements. (150526971)
- Fixed centering text for `<input type=button>` elements with `display: flex`. (151148821)
- Fixed showing a resize cursor even when text overlaps the resize control. (151309503)
- Fixed SVG transform `translate(X)` not equal to `translate(X,0)`. (151643419)
- Fixed `border-image` repaint code is broken in some writing modes. (152396671)
- Fixed rendering an image with a `filter` and `mix-blend-mode` only getting filtered but not mixed. (152460888)
- Fixed `box-shadow` to repaint correctly in `vertical-rl` and `horizontal-bt` writing modes. (152803240)
- Fixed `border` to no longer be adjusted in computed style for elements with native appearance (153152167)
- Fixed `margin-trim` to not trim inline margins on block-level boxes, regardless of their position. (153240895)
- Fixed `text-wrap-style` to not constrain single line content. (153755326)
- Fixed inputs within `inline-block` containers shifting vertically when text is deleted and re-entered into an input. (154094432)
- Fixed baseline alignment participation to expand to items with automatic logical width in the alignment axis. (154311395)
- Fixed grid containers incorrectly processing first-letter pseudo-elements when they should not contribute a first formatted line according to the CSS Grid specification. (154504582)
- Fixed grid items hit-testing order to align with painting order. (154990290)

##### Svg

###### New Features

- Added support for `pointer-events="bounding-box"` for SVG `group` containers. (148181592)

###### Resolved Issues

- Fixed SVG paint server fallback handling for a non-existent URL. (144493507)
- Fixed respecting the CSS `image-rendering` property when drawing an SVG. (144507619)
- Fixed handling `url(...) none` to match the [`SVG Paint Server specification`](https://developer.apple.comhttps://svgwg.org/svg2-draft/painting.html#SpecifyingPaint). (146454258)
- Fixed ancestor bounding box for “disabled” `<foreignObject>` and `<image>`. (147455573)
- Fixed: Improved handling of SVG images with subresources. (148607855)
- Fixed handling of `auto` for `rx` and `ry` on `<ellipse>`. (153274593)

##### Safari View Controller

###### Resolved Issues

- Fixed `lvh` and `vh` viewport units getting incorrectly sized relative to the small viewport in SFSafariViewController.  (108380836)

##### Scrolling

###### Resolved Issues

- Fixed selection does not update during autoscroll when selecting with a gesture or a mouse. (144744443)
- Fixed autoscrolling for smooth scrolling while selecting text. (144900491)
- Fixed inconsistent decimal values from `getBoundingClientRect` for sticky elements. (147163986)
- Fixed scroll compensation transform to be applied before any other transforms.  (155992464)

##### Security

###### New Features

- Added support for enforcing the `Integrity-Policy` header on script destinations.  (152244156)
- Added new configuration to support Google Safe Browsing version 5 traffic to Safari and WebKit clients with the web browser entitlement.  (154114595)

##### Service Workers

###### Resolved Issues

- Fixed the ReadableStream cancel method not getting reliably called in Service Worker. (144297119)
- Fixed an issue where navigation preload responses incorrectly retained a redirection flag when served from disk cache, causing security check failures during loading.  (144571433)
- Fixed `structureClone` to preserve `Error.cause`. (152725880)

##### Spatial Web

###### New Features

- Added support for the `<model>` element for embedding interactive 3D models into web content in visionOS.  (99085736)
- Added playback support for 180º, 360º, and Apple Projected Media Profile formats.  (140124611)

###### Resolved Issues

- Fixed various issues related to spatial audio not working in visionOS that could occur when repositioning Safari widows or moving a tab to a new window.  (145661522)
- Fixed the shape of gaze glow regions for elements with associated labels when the element has non-uniform border radii or if the element is styled with `clip-path`.  (154258426)

##### Text

###### Resolved Issues

- Fixed generating text fragments around text that contains newlines. (137109344)
- Fixed generating text fragments when the selected text starts and ends in different blocks. (137761701)
- Fixed bold synthesis to be less aggressive. (138047199)
- Fixed Copy Link with Highlight not working when selecting text that is its own block and when that text exists higher up in the document. (144392379)
- Fixed selections that start or end in white space not creating text fragments. (145614181)
- Fixed `<b>` and `<strong>` to use `font-weight: bolder` to match the Web Specification. (146458131)
- Fixed Korean counter styles to be aligned with manual Korean numbering in lists. (152969810)
- Fixed content spacing for elements with `text-align: justify` and `white-space: pre-wrap` applied. (154211168)

##### Urls

###### Resolved Issues

- Fixed percent-encoding `^` in non-opaque URL paths. (146233526)
- Fixed ensuring that opaque URL paths always roundtrip. (146848690)
- Fixed making URL host and hostname setters handle `@` correctly. (146886347)
- Fixed Windows drive letter after `file:///` when parsing URLs. (147381130)

##### Web Api

###### New Features

- Added support for the URLPattern API.  (114658976)
- Added support for scrollMargin in IntersectionObserver. (117527880)
- Added `toggle` event support for dialog open and close.  (122185814)
- Added support for Trusted Types. (130065736)
- Added support for the WebAuthn Signal API.  (134729866)
- Added support for Scoped Custom Element Registry.  (144888965)
- Added support for the Digital Credentials API. (145536102)
- Added support for the File System WritableStream API. (145875384)
- Added support for the `alg` parameter when importing or exporting Edward’s-curve based JSON Web Keys in WebCrypto. (147323269)
- Added support for `userAgentAllowsProtocol` in the Digital Credentials API. (153776127)

###### Resolved Issues

- Fixed: URL’s protocol setter should forbid switching non-special to special schemes. (82549495)
- Fixed event dispatching to be done by the fullscreen rendering update steps.  (103209495)
- Fixed the `mousemove` event to be fired when the mouse stays in the document but there is no element. (120551245)
- Fixed an overly broad fullscreen exit trigger by restricting it to only text-entry elements gaining focus, preventing non-text input types from causing unexpected fullscreen exits. (136726993)
- Fixed `WKDownload.originatingFrame` of downloads originated without a frame.  (145328556)
- Fixed fullscreen to use a single queue for event dispatching. (145372389)
- Fixed the `ProgressEvent` members `loaded` and `total` to use the `double` type as per a recent specification change. (146356214)
- Fixed Intrinsic Sizing of SVG embedded via `<embed>` to be invalidated on navigation. (147198632)
- Fixed an issue where pending utterances do not receive an error event when speech synthesis is cancelled. (148731039)
- Fixed escaping `<` and `>` when serializing HTML attribute values. (150520333)
- Fixed making the SpeechRecognition interface available only within a secure context. (151240414)
- Fixed the `<option>` element to not trim the label value and correctly handle an empty label. (151309514)
- Fixed IntersectionObvserver to notify observers asynchronously. (152684301)
- Fixed setting `innerHTML` to correctly use a scoped custom element registry associated with the context object. (154333132)
- Fixed `attachShadow` throwing type error with a ShadowRoot document-fragment. (154658449)

###### Deprecations

- Removed the `getSVGDocument()` method from `HTMLFrameElement` to align with the specification. (133800070)

##### Web Animations

###### Resolved Issues

- Fixed CSS scroll-driven animations on pages using `requestAnimationFrame` to animate correctly after navigating away and back to the page. (141528296)
- Fixed computing the time offset as needed when applying accelerated actions. (142604875)

##### Web Apps

###### New Features

- Added support for any website to become a web app on iOS or iPadOS.  (113034903)

###### Resolved Issues

- Fixed the “Add to Home Screen” flow failing to load webpage data, preventing users from making new Home Screen web apps.  (154655565)

##### Web Extensions

###### New Features

- Added support to show Web Extension commands in the menubar on macOS and iPadOS. On macOS, users can customize the keyboard shortcut associated with a command in Safari Settings.  (99049863)
- Added support for web extensions in WebDriver. (144725173)
- Added support for `dom.openOrClosedShadowRoot()`. (153118095)

###### Resolved Issues

- Fixed `tabs.update` to not remove history from the target tab.  (134939755)
- Fixed including the extension’s icon in the commands menu item and prevented customization using System Settings. (135360504)
- Fixed a bug where the `runtime.MessageSender` origin parameter would be lowercased, differing from the result returned from `runtime.getURL`. (140291738)
- Fixed high priority redirects to supercede low priority blocks for declarativeNetRequest. (145241581)
- Fixed `"excludeMatches"` array in `scripting.registerContentScripts()` API getting ignored in Safari web extensions. (145489255)
- Fixed a `declarativeNetRequest` bug that prevents redirects to extension resources. (145569361)
- Fixed processing of `declarativeNetRequest` rules so that higher numbers are treated as higher priority. (145570245)
- Fixed an issue causing `wasm-unsafe-eval` to not get parsed as a valid CSP keyword. (147551225)
- Fixed `permissions.getAll()` to return the correct origins if all urls and/or hosts match pattern(s) have been granted.  (147872012)
- Fixed a non-fatal `webRequest` error for non-persistent background content. (150051544)
- Fixed `allowAllRequests` declarativeNetRequest rules so that a higher priority correctly overrides a lower-priority block rule. (152746422)
- Fixed CSS `display: none` matching everything still getting applied even after an `ignore-following-rules` action was matched. (152996225)
- Fixed calling `scripting.registerContentScripts()` sometimes returning the error: “Error: Invalid call to scripting.registerContentScripts(). Failed to add content script.” (153001967)

##### Web Inspector

###### New Features

- Added support for the console to log both the URI and the time when entering a new navigation context.  (116901390)
- Added support for automatic inspection of Service Workers.  (118233905)
- Added support for showing `@scope` styles in the Styles sidebar.  (138840732)
- Added support for `console.profile` in `Worker`.  (144672019)
- Added support for exporting and importing data from worker targets in the Timelines tab. (145330533)
- Added a a badge for `<slot>` to quickly jump to the assigned node in the Elements tab. (148297936)
- Added support for recording Workers in the Timelines tab. (151721737)
- Added support for `@starting-style`. (153862298)

###### Resolved Issues

- Fixed pretty-printing CSS to avoid adding a space after the universal selector (`*`) when followed by a pseudo-class or pseudo-element, preventing unintended changes to CSS selector behavior. (71544976)
- Fixed to show a separate overview for each target in the Timelines tab. (146356054)
- Fixed a performance issue when blackboxing a large number of sourcemaps. (148116377)
- Fixed the debugger to step over an `await` statement as though it is synchronous code. (149133320)
- Fixed parsing sourcemaps asynchronously so that large sourcemaps do not block rendering. (151269154)
- Fixed the Timelines tab to consistently display the target’s hierarchical path for JavaScript and Events to prevent confusion when working with multiple targets.  (152357197)
- Fixed clicking on the “+” button in the Sources tab sidebar doing nothing when Web Inspector is undocked. (153193833)
- Fixed Quick Open dialog to show results when an Inspector Bootstrap script exists. (154947309)

##### Webassembly

###### New Features

- Added support for an in-place interpreter for Wasm. (113768719)

##### Webgpu

###### New Features

- Added support for WebGPU.  (145801580)

##### Webkit Api

###### New Features

- Added Screen Time support to WKWebView.  (62901207)
- Added support for a WebKit API in SwiftUI.  (65050537)
- Added support for local storage and session storage restoration APIs.  (137700273)
- Added support for applying `backdrop-filter` to content behind a transparent webview.  (144100719)
- Added a new `obscuredContentInsets` property to WKWebView that allows developers to specify areas of the web view that are covered by browser UI elements like tab bars or toolbars. Set this property to automatically adjust the layout viewport so web content renders within the visible area without being obscured by overlapping interface elements.  (155921447)

###### Resolved Issues

- Fixed a crash at launch in iOS Simulator for apps built for older deployment targets that bind to specific WebKit API.  (152200884)

###### Deprecations

- Deprecated WKProcessPool and WKSelectionGranularity.  (152447218)

##### Webrtc

###### New Features

- Added support for exposing CSRC information for RTCEncodedVideoStream. (76548862)
- Added support for the Speaker Selection API on iOS and iPadOS.  (141436868)
- Added serialization of RTCEncodedAudioFrame and RTCEncodedVideoFrame. (148244334)
- Added support for `ImageCapture.grabFrame`. (148425176)
- Added support for `RTCRtpScriptTransformer.generateKeyFrame` to take a `rid` parameter. (148592676)
- Added support for RTCEncodedAudioFrame and RTCEncodedVideoFrame constructors. (149541424)
- Added support for exposing a default system speaker device. (151761469)

###### Resolved Issues

- Fixed switching from speaker to receiver does not work the first time, but only the second time. (141685006)
- Fixed `enumerateDevices` returning devices as available when permissions are denied. (147313922)
- Fixed `enumerateDevices` to not check for device permission. (148094614)
- Fixed WebRTC encoded transform to transfer to the RTC encoded frame array buffer. (148343876)
- Fixed RTC encoded frame timestamp should be persistent. (148580865)
- Fixed the `configurationchange` event to fire when a microphone’s audio unit changes its echo cancellation mode, ensuring web pages are notified of such changes to update track settings accordingly. (150770940)

###### Deprecations

- Removed the `fec` and `rtx` from WebRTC encoding parameters. (155046829)

## See Also

- [Safari 26.3 Beta Release Notes](safari-26_3-release-notes.md)
  Released December 15, 2025 — 26.3 (20623.2.2)
- [Safari 26.2 Release Notes](safari-26_2-release-notes.md)
  Released December 12, 2025 — 26.2 (20623.1.14)
- [Safari 26.1 Release Notes](safari-26_1-release-notes.md)
  Released November 3, 2025 — 26.1 (20622.2.11)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-26-release-notes)*