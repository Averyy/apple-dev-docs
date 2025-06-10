# Safari 26.0 Beta Release Notes

**Framework**: Safari Release Notes

Released June 9, 2025 — 26.0 beta (20622.1.14)

#### Overview

Safari 26.0 beta is available for iOS 26 beta, iPadOS 26 beta, visionOS 26 beta, macOS 26 beta, macOS Sequoia, and macOS Sonoma.

##### Accessibility

###### Resolved Issues

- Fixed `aria-expanded` attribute support on navigation links.  (141163086)
- Fixed presentational images with empty `alt` attributes to be ignored by assistive technology, even when additional labeling attributes are set.  (146429365)
- Fixed `<figcaption>` within a `<figure>` element to only contribute to the accessible name of an `<img>` element if the image lacks other labeling methods like `alt`, ARIA attributes, or the `title` attribute.  (150597445)
- Fixed invalid values for `aria-setsize` and `aria-posinset` are now handled according to the updated ARIA specification, to ensure correct accessibility API exposure and predictable behavior for these attributes.  (151113693)

##### Browser

###### New Features

- Added support for SVG icons.  (113567909)
- Added support for reporting a website compatibility issue in Safari.  (133791139)
- Added support for `data:` URL icons.  (143967312)

##### Canvas

###### New Features

- Added HDR support in WebGPU Canvas.  (128164668)

###### Resolved Issues

- Fixed re-drawing a canvas with relative width when the parent element is resized.  (121996660)
- Fixed `getContext('2d', { colorSpace: 'display-p3' })` in iOS Simulator.  (151188818)

##### Css

###### New Features

- Added support for `overflow-block` and `overflow-inline`.  (70579028)
- Added support for `text-wrap: pretty`.  (114346258)
- Added support for the `margin-trim: block inline` syntax for trimming in both directions.  (141784069)
- Added partial support for the `dynamic-range-limit` property: `standard` and `no-limit`, non-animatable.  (144486108)
- Added support for `contrast-color()`.  (144630635)
- Added support for Scroll Driven Animations.  (144887859)
- Added support for `text-wrap-style: pretty`.  (145577976)
- Added support for CSS Anchor Positioning.  (145681750)
- Added support for the self-alignment properties `align-self` and `justify-self` in absolute positioning.  (145689547)
- Added support for CSS `progress()` function.  (145717727)
- Added support for `crossorigin()` and `referrerpolicy()` modifiers on CSS image loads.  (149166339)

###### Resolved Issues

- Fixed `cursor: pointer` not appearing on an `<area>` element used in conjunction with an `<img usemap="...">` element.  (74483873)
- Fixed grid sizing with inline-size containment and auto-fit columns is incorrectly sized.  (108897961)
- Fixed content skipped with `content-visibility: auto` to be findable.  (141237620) (FB16079870)
- Fixed an issue wrapping an SVG at the end of a line when using `text-wrap: balance`.  (141532036)
- Fixed `@font-face font-family` descriptor to not allow a list of values.  (142009630)
- Fixed the computed value of a float with absolute positioning to be `none` when there is no box.  (144045558)
- Fixed: Updated `contrast-color()` to remove the `max` parameter.  (144611470)
- Fixed buttons to not have `align-items: flex-start` by default.  (146615626)
- Fixed `@scope` to create a style nested context.  (148101373)
- Fixed changing `content-visibility` from `visible` to `hidden` to repaint correctly.  (148273903)
- Fixed an issue where float boxes, selections, and carets were incorrectly painted inside skipped subtrees.  (148741142)
- Fixed incorrect `getBoundingClientRect()` inside skipped subtree on an out-of-flow positioned box.  (148770252)
- Fixed making `<pre>` and other elements use logical margins in the User-Agent stylesheet.  (149212392)

###### Known Issues

- The `position-visibility` property is partially supported with an implementation of the default `anchors-visible` value.  (129789653)
- Explicit anchor elements are required when using anchor functions on pseudo-elements. Implicit anchor element support is not currently supported.  (152635393)

##### Dom

###### Resolved Issues

- Fixed the serialization of `CDATASection` nodes in HTML.  (150739105)

##### Editing

###### New Features

- Added support for rendering native selection UI inside scrolled content.  (136988607)

###### Resolved Issues

- Fixed the selection UI to be clipped in overflow scrolling containers.  (9906345)
- Fixed selection issues caused by `<br>` elements between absolute positioned elements.  (123637358)
- Fixed selection failing to update during auto or keyboard scrolling.  (144581646)

##### Forms

###### Resolved Issues

- Fixed form associated ElementInternals always reporting a `customError` when using `setValidity`.  (115681066)
- Fixed `setValidity` of `ElementInternals` to handle missing optional `anchor` parameter.  (123744294)
- Fixed programmatically assigned File objects to display the correct filename in `<input>` elements, even without a file path.  (152048377)
- Fixed labels inside `<select>` elements to behave consistently with other browsers by using standard attribute matching instead of quirk mode handling.  (152151133)

##### Images

###### New Features

- Added support for HDR Images on iOS, iPadOS, macOS and in visionOS.  (134397601)

##### Javascript

###### New Features

- Added support for Regular Expression Pattern Modifiers.  (131580854)
- Added support for `@@dispose` and `@@asyncDispose` from the Explicit Resource Management Proposal behind runtime flag.  (150816114)
- Added support for `SuppressedError` from the Explicit Resource Management Proposal behind runtime flag.  (151132111)
- Added support for `DisposableStack` constructor from the Explicit Resource Management Proposal behind runtime flag.  (151280591)
- Added support for the `notation` option for `Intl.PluralRules`.  (152149896)

###### Resolved Issues

- Fixed `Array.prototype.pop` to throw an exception when the array is frozen.  (141805240)
- Fixed performance of `Math.hypot()` that was significantly slower than `Math.sqrt()`.  (141821484)
- Fixed `Array#indexOf` and `Array#includes` to treat `+0` and `-0` as the same value.  (148472519)
- Fixed iterator helpers incorrectly closing iterators on early errors.  (148774612)
- Fixed `Iterator.prototype.reduce` failing with an `undefined` initial parameter.  (149470140)
- Fixed `f() = 1` behavior with other engines when not using strict mode.  (149831750)
- Fixed nested negated classes resulting in incorrect matches.  (151000852)

##### Lockdown Mode

###### New Features

- Added support for more web fonts in Lockdown Mode by replacing a fragile hard-coded allowlist with a safe parser that handles a broader range of fonts without compromising security.  (149314760)

##### Media

###### New Features

- Added support for in-band tracks in MSE.  (129295806)
- Added support for `detachable` MediaSource objects to allow for seamless switching between objects attached to a media element.  (129298010)
- Added support for MediaSource prefers DecompressionSession.  (142761051)
- Added support for WebCodec’s AudioEncoder and AudioDecoder.  (142916087)
- Added support for ALAC and PCM audio in MediaRecorder.  (144145333)

###### Resolved Issues

- Fixed picture-in-picture to exit when the video element is removed.  (123869436)
- Fixed MP4 seeking with b-frames to prevent out-of-order frame display by suppressing frames with earlier presentation timestamps following the seek point.  (140415210)
- Fixed media elements on iPadOS to support the volume being changed by web developers, similar to macOS and visionOS. The `:volume-locked` pseudo-class can continue to be used for feature detection.  (141555604)
- Fixed seeking or scrubbing not always seeking to the time requested.  (142275903) (FB16223006)
- Fixed stale audio buffer data after seeking when playing sound through an AudioContext.  (146057507)
- Fixed subtitle tracks with no `srclang` to be shown with the correct label.  (147722563)
- Fixed MediaSession to handle SVG icons with subresources.  (150665852)
- Fixed `MediaCapabilitiesDecodingInfo.configuration` to be correctly populated even when `.supported` is `false`.  (150680756)

##### Networking

###### New Features

- Added support for `<link rel=dns-prefetch>` on iOS while improving privacy on macOS.  (144699889)

##### Privacy

###### New Features

- Added support for preventing fingerprinting for known tracking scripts.  (134227067)

##### Rendering

###### Resolved Issues

- Fixed an issue to allow images in scroll containers to load when they are near the viewport rather than when they are intersecting the viewport.  (118706766)
- Fixed a disappearing stretched image in a vertical flexbox layout.  (135897530)
- Fixed CSS gradient interpolation into regions beyond the first or last color stop.  (142738948)
- Fixed integrating `position-area` and `self-alignment` properties for `align-self` and `justify-self`  (145889235)
- Fixed `will-change: view-transition-name` to create a stacking context and a backdrop root.  (146281670)
- Fixed `will-change: offset-path` to create a stacking context and a containing block.  (146292698)
- Fixed `<datalist>` dropdowns not displaying option labels.  (146921617)
- Fixed the text indicator sometimes getting clipped during a bounce animation.  (147602900)
- Fixed geometry values inside `content-visibility: hidden` subtrees.  (148553259)
- Fixed not marking `content-visibility: hidden` content for layout when targeting `content-visibility: auto`.  (148663896)
- Fixed incorrect `ruby` annotation positioning in `sideways-lr`.  (148713073)
- Fixed: Prevented hit testing content inside a skipped subtree.  (148741508)
- Fixed an issue where `feMerge` incorrectly positioned HTML elements when merging the same `feMergeNode` multiple times.  (149431216)
- Fixed an issue in determining when a flex item should be used for percentage resolution during intrinsic width computation.  (149615295)
- Fixed an issue causing a `<canvas>` element to disappear for one frame if a view transition occurs.  (149709642)
- Fixed invisible `<audio>` controls when transformed due to incorrect coordinate space calculations for clipped child elements.  (150526971)
- Fixed centering text for `<input type=button>` elements with `display: flex`.  (151148821)
- Fixed showing a resize cursor even when text overlaps the resize control.  (151309503)

##### Safari View Controller

###### Resolved Issues

- Fixed `lvh` and `vh` viewport units getting incorrectly sized relative to the small viewport in SFSafariViewController.  (108380836)

##### Scrolling

###### Resolved Issues

- Fixed selection does not update during autoscroll when selecting with a gesture or a mouse.  (144744443)
- Fixed autoscrolling for smooth scrolling while selecting text.  (144900491)

##### Service Workers

###### Resolved Issues

- Fixed the ReadableStream cancel method not getting reliably called in Service Worker.  (144297119)
- Fixed an issue where navigation preload responses incorrectly retained a redirection flag when served from disk cache, causing security check failures during loading.  (144571433)

##### Spatial Web

###### New Features

- Added support for the `<model>` element for embedding interactive 3D models into web content in visionOS.  (99085736)
- Added playback support for 180º, 360º, and Apple Projected Media Profile formats.  (140124611)
- Added support for spatial audio in visionOS.  (145661522)

##### Svg

###### New Features

- Added support for `pointer-events="bounding-box"` for SVG `group` containers.  (148181592)

###### Resolved Issues

- Fixed SVG paint server fallback handling for a non-existent URL.  (144493507)
- Fixed respecting the CSS `image-rendering` property when drawing an SVG.  (144507619)
- Fixed handling `url(...) none` to match the [`SVG Paint Server specification`](https://developer.apple.comhttps://svgwg.org/svg2-draft/painting.html#SpecifyingPaint).  (146454258)
- Fixed ancestor bounding box for “disabled” `<foreignObject>` and `<image>`.  (147455573)
- Fixed: Improved handling of SVG images with subresources.  (148607855)

##### Text

###### Resolved Issues

- Fixed generating scroll to text fragments around text that contains newlines.  (137109344)
- Fixed generating text fragments when the selected text starts and ends in different blocks.  (137761701)
- Fixed bold synthesis to be less aggressive.  (138047199)
- Fixed Copy Link to Highlight not working when selecting text that is its own block and when that text exists higher up in the document.  (144392379)
- Fixed selections that start or end in white space not creating text fragments.  (145614181)
- Fixed `<b>` and `<strong>` to use `font-weight: bolder` to match the Web Specification.  (146458131)

##### Urls

###### Resolved Issues

- Fixed making URL host and hostname setters handle `@` correctly.  (146886347)

##### Web Animations

###### Resolved Issues

- Fixed CSS scroll-driven animations on pages using `requestAnimationFrame` to animate correctly after navigating away and back to the page.  (141528296)
- Fixed computing the time offset as needed when applying accelerated actions.  (142604875)

##### Web Api

###### New Features

- Added support for the URLPattern API.  (114658976)
- Added support for scrollMargin in IntersectionObserver.  (117527880)
- Added support for the AudioDecoder and AudioEncoder APIs.  (118883953)
- Added support for Trusted Types.  (130065736)
- Added support for the WebAuthn Signal API.  (134729866)
- Added support for Scoped Custom Element Registry.  (144888965)
- Added support for the Digital Credentials API.  (145536102)
- Added support for the File System WritableStream API.  (145875384)
- Added support for the request-close command for dialogs.  (146103521)
- Added support for the `alg` parameter when importing or exporting Edward’s-curve based JSON Web Keys in WebCrypto.  (147323269)

###### Resolved Issues

- Fixed: URL’s protocol setter should forbid switching non-special to special schemes.  (82549495)
- Fixed event dispatching to be done by the fullscreen rendering update steps.  (103209495)
- Fixed an overly broad fullscreen exit trigger by restricting it to only text-entry elements gaining focus, preventing non-text input types from causing unexpected fullscreen exits.  (136726993)
- Fixed `WKDownload.originatingFrame` of downloads originated without a frame.  (145328556)
- Fixed fullscreen to use a single queue for event dispatching.  (145372389)
- Fixed the `ProgressEvent` members `loaded` and `total` to use the `double` type as per a recent specification change.  (146356214)
- Fixed Intrinsic Sizing of SVG embedded via `<embed>` to be invalidated on navigation.  (147198632)
- Fixed an issue where pending utterances do not receive an error event when speech synthesis is cancelled.  (148731039)
- Fixed escaping `<` and `>` when serializing HTML attribute values.  (150520333)
- Fixed making the SpeechRecognition interface available only within a secure context.  (151240414)
- Fixed the option element to not trim the label value and correctly handle an empty label.  (151309514)

###### Deprecations

- Removed the `getSVGDocument()` method from `HTMLFrameElement` to align with the specification.  (133800070)

##### Web Apps

###### New Features

- Added support for any website to become a web app on iOS or iPadOS.  (113034903)

##### Web Extensions

###### New Features

- Added support for showing extension keyboard shortcuts in Safari Settings and allow customization on macOS.  (99049863)
- Added an option to allow all website access from settings if `<all_urls>` is an optional host permission.  (145704875)
- Added support for the request-method content blocker trigger field.  (148474901)

###### Resolved Issues

- Fixed a `declarativeNetRequest` bug that prevents redirects to extension resources.  (145569361) (FB16607632)
- Fixed converting `declarativeNetRequest` rules so that higher numbers are treated as higher priority.  (145570245) (FB16607998)
- Fixed an issue causing `wasm-unsafe-eval` to not get parsed as a valid CSP keyword.  (147551225)
- Fixed `permissions.getAll()` to return the correct origins if all urls and/or hosts match pattern(s) have been granted.  (147872012)

##### Web Inspector

###### New Features

- Added support for the console to log both the URI and the time when entering a new navigation context.  (116901390)
- Added support for automatic inspection of Service Workers.  (118233905)
- Added support for `console.profile` in `Worker`.  (144672019)
- Added support for exporting and importing data from worker targets in the Timelines tab.  (145330533)
- Added a a badge for `<slot>` to quickly jump to the assigned node in the Elements tab.  (148297936)
- Added support for recording Workers in the Timelines tab.  (151721737)

###### Resolved Issues

- Fixed pretty-printing CSS to avoid adding a space after the universal selector (`*`) when followed by a pseudo-class or pseudo-element, preventing unintended changes to CSS selector behavior.  (71544976) (FB8906066)
- Fixed to show a separate overview for each target in the Timelines tab.  (146356054)
- Fixed a performance issue when blackboxing a large number of sourcemaps.  (148116377)
- Fixed the debugger to step over an `await` statement as though it is synchronous code.  (149133320)
- Fixed parsing sourcemaps asynchronously so that large sourcemaps do not block rendering.  (151269154)
- Fixed the Timelines tab to consistently display the target’s hierarchical path for JavaScript and Events to prevent confusion when working with multiple targets.  (152357197)

###### Deprecations

- Removed support for inspecting WebSQL in Web Inspector.  (143596276)
- Removed support for inspecting ApplicationCache.  (143596399)

##### Webassembly

###### New Features

- Added support for an in-place interpreter for Wasm.  (113768719)

##### Webgpu

###### New Features

- Added support for WebGPU.  (145801580)

##### Webkit Api

###### New Features

- Added support for a WebKit API in SwiftUI.  (65050537) (FB7842345)
- Added support for local storage and session storage restoration APIs.  (137700273)
- Added support for applying `backdrop-filter` to content behind a transparent webview.  (144100719)

###### Known Issues

- Property changes of an `@Observable` cannot be observed.  (110504118)
- `WKPreferences.isLookToScrollEnabled` is not available on non-visionOS platforms.  (152106377)

##### Webrtc

###### New Features

- Added support for exposing CSRC information for RTCEncodedVideoStream.  (76548862)
- Added support for the Speaker Selection API on iOS and iPadOS.  (141436868)
- Added serialisation of RTCEncodedAudioFrame and RTCEncodedVideoFrame.  (148244334)
- Added support for `ImageCapture.grabFrame`.  (148425176)
- Added support for `RTCRtpScriptTransformer.generateKeyFrame` to take a `rid` parameter.  (148592676)
- Added support for RTCEncodedAudioFrame and RTCEncodedVideoFrame constructors.  (149541424)
- Added support for exposing a default system speaker device.  (151761469)

###### Resolved Issues

- Fixed switching from speaker to receiver does not work the first time, but only the second time.  (141685006)
- Fixed `enumerateDevices` returning devices as available when permissions are denied.  (147313922)
- Fixed` enumerateDevices` to not check for device permission.  (148094614)
- Fixed WebRTC encoded transform to transfer to the RTC encoded frame array buffer.  (148343876)
- Fixed RTC encoded frame timestamp should be persistent.  (148580865)
- Fixed the `configurationchange` event to fire when a microphone’s audio unit changes its echo cancellation mode, ensuring web pages are notified of such changes to update track settings accordingly.  (150770940)

##### Wkwebview

###### New Features

- Added Screen Time support to WKWebView.  (62901207)

###### Known Issues

- Digital Credentials, [`announced at WWDC`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/232) is not supported in WKWebView. Follow WebKit bug [`268516`](https://developer.apple.comhttps://bugs.webkit.org/show_bug.cgi?id=293646) for updates.  (152531092)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-26-release-notes)*