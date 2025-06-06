# Safari 18.4 Release Notes

**Framework**: Safari Release Notes

Released March 31, 2025 — 18.4 (20621.1.15)

#### Overview

Safari 18.4 is available for iOS 18.4, iPadOS 18.4, visionOS 2.4, macOS 15.4, macOS Sonoma, and macOS Ventura.

##### Authentication

###### New Features

- Added support for setting a pin on a security key when a registration requires it.  (122660610)

##### Browser

###### Resolved Issues

- Fixed an issue where sites would log out automatically after a brief time.  (99829958)

##### Canvas

###### New Features

- Added CanvasRenderingContext2D support for unprefixed `letterSpacing` and `wordSpacing`.  (140614722)

###### Deprecations

- Removed support for `webKitBackingStorePixelRatio`.  (123980544)
- Removed support for the prefixed `webkitImageSmoothingEnabled` to use the standard `imageSmoothingEnabled` property.  (141128458)
- Removed non-standard legacy alias of Canvas Compositing including `setAlpha` and `setCompositeOperation`.  (141510218)

##### Connection Security

###### New Features

- Added the ability to view certificate detail from Page Menu > more > Connection Security Details on iOS, iPadOS, and in visionOS, or Safari > Connection Security Details… on macOS.  (139300381)

###### Deprecations

- Removed the lock icon from the Smart Search field for HTTPS connection. (107993392)  (107993392)

##### Css

###### New Features

- Added support for `writing-mode: sideways-rl` and `writing-mode: sideways-lr`.  (81519211)
- Added support for the `::details-content` pseudo-element.  (129786929)
- Added `attr()` fallback support.  (136763160)
- Added support for `view-transition-name: match-element`.  (138932551)
- Added support for `text-autospace`.  (140008990)
- Added support for the CSS `shape()` function.  (142276582)
- Added support for gradients with only one stop.  (142796999)

###### Resolved Issues

- Fixed table `border-color` to be `currentColor` by default.  (48382483)
- Fixed combining CSS `clip-path` with any property that creates a new stacking context makes `<img>` element disappear.  (86091397)
- Fixed resize to not be applied to generated content.  (121348638)
- Fixed `contain: size` breaking `object-fit`.  (131866042)
- Fixed: Dropped layout containment from `container-type`.  (132549134)
- Fixed handling all of the CSS properties in specifications that should cause a UI widget to devolve to a primitive appearance.  (134273374)
- Fixed `scrollIntoView` alignment to always be honored.  (135484284)
- Fixed:`background-clip: border-area` to do nothing on the root.  (135972986)
- Fixed `vertical-rl` writing mode inter-character ruby text being significantly smaller than over ruby text.  (135973587)
- Fixed CSS cursor to not eagerly evaluate `calc()` values.  (136103471)
- Fixed flex shorthand to not eagerly evaluate `calc()`.  (136103475)
- Fixed `-webkit-perspective` to not eagerly evaluate `calc()`.  (136103493)
- Fixed `@property` `initial-value` descriptor to prevent containing `var(--foo)`.  (136103499)
- Fixed delaying the evaluation of `calc()` for raw font consumers so that each caller can choose the correct behavior.  (136103500)
- Fixed grid to not eagerly evaluate `calc()` for repetitions value.  (136103503)
- Fixed `counter-increment`, `counter-set`, and `counter-reset` to not eagerly evaluate `calc()`.  (136103519)
- Fixed CSS nested declarations inside a `@scope` to behave like `:where(:scope)`.  (136856371)
- Fixed: Updated the `shape()` function to match the proposed syntax.  (138126105)
- Fixed same-document view transitions performance on pages with many elements.  (138966650)
- Fixed an issue where radial gradients with two color stops at 100% failed to extend the last color.  (139369366)
- Fixed `@scope` `start` and `end` to be a classic (non-forgiving) selector list.  (139471866)
- Fixed updating the base background color where the root has `color` set explicitly when switching to light or dark modes.  (139917332)
- Fixed performance of `querySelectorAll()` with `:has()` descendant selectors.  (140093151)
- Fixed the `unicode-bidi` default for the `<bdo>` element.  (140662417)
- Fixed broken `revert-layer` when logical group CSS properties are explicitly inherited.  (140819138)
- Fixed border-spacing to use the shortest possible serialization (“0px” vs “0px 0px”).  (141920587)
- Fixed subsequent nested styles getting ignored after an incorrect nested selector.  (142187930)
- Fixed `font-variant-caps: all-small-caps` causing incorrect `box-sizing` in `flex` inline context.  (142212550)
- Fixed ensuring  the correct logic is run for over-constrained cases when the absolute positioned box is a `writing-mode` root.  (142214631)
- Fixed `animation-name` set from the view transitions dynamic UA stylesheet having extra quotes.  (142298840)
- Fixed the serialization and parsing of `animation-name` strings.  (142318879)
- Fixed `text-box-trim` accumulation failing when updating the CSS dynamically.  (142386761)
- Fixed `text-emphasis` to not paint emphasis marks on punctuations.  (142387538)
- Fixed sizing and positioning issues when a popover changes CSS position upon opening.  (142491219)
- Fixed Page Zoom (⌘+ and ⌘-) to work with `calc()` used with `font-size` on macOS.  (142736427) (FB16287129)
- Fixed `scroll-padding` and `scroll-margin` to be strongly typed CSS/Style values.  (142830546)
- Fixed View Transitions to stop running when the user navigates with a swipe.  (142844150)
- Fixed top-level and nesting selector to have zero specificity matching a recent specification update.  (143765827)

###### Deprecations

- Removed the non-standard `CSSUnknownRule` interface.  (142380626)

##### Editing

###### New Features

- Implemented `ClipboardItem.support()` which gives the page author the ability to understand which formats are [`supported during Clipboard operations`](https://developer.apple.comhttps://w3c.github.io/clipboard-apis/#dom-clipboarditem-supports). It also now returns a TypeError for a new `ClipboardItem()` with an empty Array.  (136008522)

###### Resolved Issues

- Fixed `document.execCommand("copy")` only triggering if there is a selection.  (27792460)
- Fixed an issue where iCloud Notes pasted text copied from a plain text document in Safari as raw markup.  (124788252)
- Fixed highlighting correctly a large text selection that ends with a common phrase.  (135973065)
- Fixed copying a link to a common term in an article to highlight the correct part of the page.  (135973186)
- Fixed missing `SecureContext` in the `ClipboardItem` interface.  (137197266)
- Fixed Hebrew text pasted from Safari getting aligned left.  (139029945)
- Fixed setting selection to not set focus unless there is an existing selection.  (139075809)
- Fixed sometimes being unable to select text for non-editable content.  (143296175)
- Fixed missing selection handles after selecting text across multiple lines.  (143720155)

##### Forms

###### New Features

- Improved `<input type="file" webkitdirectory>` support on iOS.  (125457578)
- Added `alpha` and `colorspace` attributes to `<input type=color>`.  (137737348)

###### Resolved Issues

- Fixed `<textarea>` to handle switching direction.  (73475239)
- Fixed setting a `datetime-local` input to a large value cause a crash.  (135733092)
- Fixed `<datalist>` dropdown keyboard interactions to align with platform conventions.  (143012287)
- Fixed: Disabled all Writing Tools app menu items, except “Compose”, for empty editable content.  (143332082)

##### Home Screen Web Apps

###### Resolved Issues

- Fixed Wake Lock API for Home Screen Web Apps.  (108573133)

##### Html

###### New Features

- Implemented `<details>` and `<summary>` disclosure triangle as a list item.  (95148788)

###### Deprecations

- Removed the `composite` attribute on an `<img>` element.  (143109250)

##### Images

###### Resolved Issues

- Fixed broken WebP images in lockdown mode.  (144224372)

##### Javascript

###### New Features

- Completed the [`Iterator Helpers proposal`](https://developer.apple.comhttps://github.com/tc39/proposal-iterator-helpers) by implementing `map()`, `filter()`, `take()`, `drop()`, and `flatMap()` methods.  (103171739)
- Updated `JSON.parse` to provide the reviver function access to the input source text and extended `JSON.stringify` behavior to support object placeholders.  (131579181)
- Added support for `Math.sumPrecise`.  (131580043)
- Added support for `Iterator.prototype.toArray` from Iterator Helpers Proposal.  (135493558)
- Added support for `Iterator.prototype.forEach` from Iterator Helpers Proposal.  (136010225)
- Added support for `some`, `every`, `find` from Iterator Helpers Proposal.  (136027193)
- Added support for `Iterator.prototype.reduce`.  (136064316)
- Added support for `SetterThatIgnoresPrototypeProperties()` in Iterator helpers.  (137078675)
- Added support for `Atomics.pause`.  (137571229)
- Added support for `Iterator.prototype.chunks` and `Iterator.prototype.windows`.  (138012241)
- Added support for `Iterator.concat`.  (138013723)
- Added support for Iterator Helpers.  (138520150)
- Added support for `Map.prototype.getOrInsert` and `WeakMap.prototype.getOrInsert`.  (138955824)
- Added support for `Error.isError`.  (141132351)
- Added `"never"` and `"formalSymbol"` to the `currencyDisplay` option for `Intl.NumberFormat`.  (141504278)

###### Resolved Issues

- Fixed Array destructuring assignment to close the iterator if an evaluation throws an exception.  (121960887)
- Fixed: Updated `Intl.DurationFormat#resolvedOptions` to the latest specification.  (136276429)
- Fixed Iterator Helpers methods to not iterate an array.  (136303997)
- Fixed `Iterator.prototype.reduce()` not properly forwarding the `return()` call to the underlying iterator.  (137181340)
- Fixed `Set.prototype` methods to invoke `keys()` without arguments.  (137395979)
- Fixed `Array.from()`, `Array.fromAsync()`, and `TypedArray.from()` to invoke `document.all` passed as a mapper.  (137490201)
- Fixed `Intl.DurationFormat` to have a value limit to match the specification.  (137885273)
- Fixed a rounding error for `Intl.DurationFormat`.  (138261569)
- Fixed calendar canonicalization logic in `DateTimeFormat`.  (141792829)
- Fixed broken output for `Intl.DurationFormat` digital style when `hoursDisplay` is `"auto"`.  (141969050)
- Fixed `Intl.DurationFormat` to print a negative sign for minutes after hidden hours.  (142119353)
- Fixed `Array.prototype.toReversed` to fill holes with `undefined`.  (142197604)
- Fixed: Increased the `matchLimit` for regular expressions, allowing complex matches on longer strings.  (143202375)

###### Deprecations

- Removed obsoleted methods for `Temporal.PlainTime` and `Temporal.PlainDateTime` to align with specification changes.  (135509670)

##### Loading

###### New Features

- Added `noopener-allow-popups` support in Cross-Origin-Opener-Policy.  (129664445)

##### Media

###### New Features

- Added support for Ogg Opus and Ogg Vorbis on macOS Sequoia 15.4, iOS 18.4, iPadOS 18.4, and visionOS 2.4.  (131407707)
- Added support for the Image Capture API.  (136860809)
- Added WebM support to MediaRecorder.  (137560454)

###### Resolved Issues

- Fixed handling an empty `srcAttr` in Media Element.  (132042925)
- Fixed getUserMedia video track `getSettings()` returning a stale value for `torch` and `whiteBalanceMode` constraints.  (137870391)
- Fixed the `space` key not pausing a video in fullscreen by making the video mouse focusable.  (138037616)
- Fixed an issue where playback doesn’t always resume after a seek.  (140097993)
- Fixed playing video generating non-monotonic ‘timeupdate’ events.  (142275184) (FB16222910)
- Fixed websites calling `play()` during a `seek()` is allowed by the specification so that the play event is fired even if the seek hasn’t completed.  (142517488)
- Fixed seek not completing for WebM under some circumstances.  (143372794)
- Fixed MediaRecorderPrivateEncoder writing frames out of order.  (143956063)

##### Networking

###### New Features

- Added support for Cookies Having Independent Partitioned State (CHIPS).  (116143212)
- Added support for cookies’ `Partitioned` attribute for opt-in partitioned cookies.  (142317056)
- Blocked partitioned cookies for known tracking domains.  (144184516)

###### Resolved Issues

- Fixed optimistically upgraded navigations to set a timeout based on current network conditions.  (135972599)

###### Deprecations

- Changed 3DES cipher to show a warning to users that it is a legacy TLS cipher.  (138948491)

##### Pdf

###### Resolved Issues

- Fixed switching a PDF from continuous to discrete mode displaying the page(s) that are at the top of the window, even when barely visible.  (137608841)
- Fixed the “Previous Page” context menu option not navigating to previous page in 2-up continuous mode.  (139817364)
- Fixed main frame PDFs served with a CSP sandbox header not loading.  (141166987)

##### Rendering

###### Resolved Issues

- Fixed computing the baseline for replaced elements with an intrinsic ratio but no intrinsic size as flex items.  (74279029)
- Fixed flickering caused by extra resize events dispatched when rotating from landscape to portrait on iOS.  (93767145)
- Fixed adding out-of-flow objects under the inline in a continuation chain, when possible.  (102421379)
- Fixed `mix-blend-mode` to work for large resolution fixed or stick elements.  (104686540)
- Fixed the missing table collapsed border for `<thead>`, `<tbody>`, and `<tfoot>` elements in the wrong order.  (110430887)
- Fixed handling inline-box trailing content.  (112409103)
- Fixed `<input type="range">` taking up space even with `width: 0` applied.  (113402515)
- Fixed the Spotify media player disappearing when rotating to landscape mode on iOS.  (123870311)
- Fixed textarea elements to reserve space for overlay scrollbars.  (129597865)
- Fixed grid layout animation performance by caching intrinsic logical heights during the first row sizing pass, improving efficiency and preventing invalidation issues with complex grid configurations.  (135791322)
- Fixed Grid item which is an image with specified sizes failing to update when the `src` changes.  (135972911)
- Fixed nested inlines’ vertical alignment when `line-fit-edge` is set.  (136036997)
- Fixed the consistency of table layout with `<td width="100%">`.  (136090741)
- Fixed repainting to be more consistent for `text-underline-position`.  (136095297)
- Fixed floats not clearing in the WordPress Classic Editor sidebar layout.  (136362683)
- Fixed handling of out-of-flow children in MathML layout functions to be consistent.  (136683070)
- Fixed a repeating `background-image` sized to the `content-box` failing to fill the viewport in an iframe.  (136725820)
- Fixed consistently triggering a reflow when needed for table DOM manipulations.  (137300794)
- Fixed `scriptlevel` multipler for font-size in MathML.  (137671252)
- Fixed inline marquees to allow them to shrink when adjacent to float(s).  (137766071)
- Fixed a flex container with no flex item to not run flex layout.  (137884128)
- Fixed support for CSS width and height properties on MathML elements.  (138174295)
- Fixed Inline content incorrectly positioning around right-to-left and/or vertical `shape-outside` floats.  (139076129)
- Fixed incorrectly overlapping when a float has `shape-outside: inset`.  (139133291)
- Fixed right-to-left content failing with a `shape-outside` float.  (139198865)
- Fixed incorrectly overlapping a float that has `shape-outside: ellipse` in vertical mode.  (139208636)
- Fixed incorrectly overlapping a float that has `shape-outside: polygon` in right-to-left.  (139215719)
- Fixed outside `list-style-position` quirk to only be applicable in quirks mode.  (140602985)
- Fixed: Updated line box dimensions.  (141167251)
- Fixed incorrect horizontal writing mode state when nested in a vertical block container.  (141543326)
- Fixed baseline calculation few cases for tables with empty rows.  (142046863)
- Fixed to refuse to break inside replaced content.  (142224455)
- Fixed absolute positioned child with percent to include containing block padding.  (142321535)
- Fixed computing an out-of-flow box width correctly when it is inside an inline continuation.  (142417374)
- Fixed a border not showing when a linear gradient and a border radius are set.  (142617573)
- Fixed relative-positioned input elements in scroll areas not rendering outlines.  (142995142)
- Fixed tabbing out of a popover causing a hang in certain cases.  (143145544)
- Fixed setting up inline continuations correctly when not inserting a new child.  (143388080)
- Fixed adding a `margin-top` to a `<rt>` also adds a bottom margin.  (143720832)

##### Scrolling

###### New Features

- Added support for Scroll To Text Fragment feature detection with `document.fragmentDirective`.  (139631353)

###### Resolved Issues

- Fixed changes to the “scrolling” attribute on an iframe element already in the DOM to take effect.  (98911472)

##### Security

###### New Features

- Added support for CSP Hash Reporting keywords: `report-sha256`, `report-sha384`, and `report-sha512`.  (142458671)

###### Deprecations

- Removed support for `Clear-Site-Data: *` for `executionContexts` as Safari was the only browser to ship it.  (120821984)

##### Service Workers

###### Resolved Issues

- Fixed handling the case of busy looping service workers in a process containing web pages.  (138626537)
- Fixed an unexpected failure when serving a redirected response from cache for a navigation loaded via service worker navigation preload.  (146113615)

##### Spatial Web

###### New Features

- Added support behind a feature flag for the `controls` attribute on `<img>` elements for spatial images in visionOS.  (129784451)
- Added support for Writing Tools in visionOS.  (135210076)

##### Storage

###### New Features

- Added support for partitioned cookies in `Clear-Site-Data: Cookies`.  (140403030)

###### Resolved Issues

- Fixed the Storage Access API to consider `AllExceptPartitioned` as not currently having cookie access, ensuring sites can request access to first-party cookie.  (143508260)

##### Svg

###### New Features

- Added support for `SVGImageElement.prototype.decode()`.  (135404215)
- Added support for the `lh` length type.  (142068343)
- Added support for the `ch` length type for character width, but does not include support for upright vertical character width.  (142463263)

###### Resolved Issues

- Fixed not propagating the bounding box for empty `text` to ancestors.  (115217040)
- Fixed SVG masks not working as a `mask-image`.  (127327715)
- Fixed a bug in case of reference elements (e.g., textPath) unable to notify the referring element (e.g, text) about their availability.  (135509733)
- Fixed SVGUseElement to prevent sniffing the content type when loading an external document.  (135972621)
- Fixed vertical writing modes to se the correct bounding rect.  (135973175)
- Fixed: Updated `getTotalLength()` with the web specification to throw an exception when non-renderable and the path is empty.  (136719548)
- Fixed SVG quadratic curve getting incorrectly clipped at tile boundaries.  (139904014)
- Fixed dynamically updating the `transform` attribute.  (140761655)
- Fixed synthesizing a `viewBox` in `<img>` only for the document element `<svg>`.  (141733733)
- Fixed `SVGElement.prototype.ownerSVGElement` on the outermost `<svg>` in `foreignObject`.  (143625675)

###### Deprecations

- Removed the SVG 1.1 kerning property.  (116965514)
- Removed SVGDocument alias to XMLDocument.  (123121696)

##### Tables

###### Resolved Issues

- Fixed table row direction to be determined by the table’s direction, not the section.  (99343532)
- Fixed missing behavior for `rowspan="0"` on HTML tables where 0 means span over all the remaining rows.  (133910430)
- Fixed Table Root to also account for `fill-available` in a fixed table layout.  (137297914)
- Fixed table section and row background to not be treated as opaque.  (142588505)

##### Text

###### Resolved Issues

- Fixed an issue where a thick underline would not show on short content.  (64705955)
- Fixed: The changes for GB18030-2022 now properly impact GBK as well, as required by the Encoding Standard.  (136368583)
- Fixed automatically hyphenating text only when a language specified.  (136826305)
- Fixed the boundary style calculation when `text-spacing: text-autospace` is applied.  (137153961)
- Fixed displaying OpenType-SVG color fonts.  (137496217) (FB15426148)

##### Web Api

###### New Features

- Added support for `element.focus({ focusVisible: true })`.  (97021844)
- Added support for `PublicKeyCredential.toJSON()`.  (109419228)
- Added support for the Cookie Store API.  (135969444)
- Added Key generation, import and export support for CryptoKeyOKP(x25519/ed25519).  (136368298)
- Added support for Brotli to Compression Streams.  (137244214)
- Added an option to set the popover’s invoker from an imperative API.  (139362169)
- Added support for Declarative Web Push.  (141082392)
- Added support for X25519 for Web Cryptography.  (141346336)
- Added support for `dialog.requestClose()`.  (143388390)

###### Resolved Issues

- Fixed: Aligned some MIME type handling in EME with the MIME Sniffing standard.  (114311586)
- Fixed `window.history.replaceState('', '', '')` having no effect on macOS.  (117782346)
- Fixed MutationObserver to observe style attribute changes when resizing the element.  (120109181)
- Fixed: Updated `selectorText` handling to align with the specification for CSSPageRule.  (125588212)
- Fixed Gamepad rumble issue where sending two sequential `playEffect()` requests prevents `reset()` from working as expected.  (126589062) (FB13733668)
- Fixed matching emoji in an element’s `id` attribute from a `<link rel=expect>` with an `href` that uses percent-encoded syntax.  (134531921)
- Fixed the `onrejectionhandled` and `onunhandledrejection` event handler attributes to work correctly on body and frameset elements.  (135401362)
- Fixed render blocking for `<link>` to not match elements that are on a ‘stack of open elements’ for the parser.  (135846827)
- Fixed Distraction Control unexpectedly hiding out-of-flow elements that overlap with a hidden element.  (136358918)
- Fixed CSSOM `setSelectorText(string)` to prepend the implicit selector.  (136791222)
- Fixed `HTMLElement.prototype.requestPointerLock` to return a Promise.  (139854530)
- Fixed `innerText` behavior for `<details>` and `<summary>`.  (140172890)
- Fixed the HTML parser phone number handling to better account for MathML.  (141632782)
- Fixed `Range.getClientRects` to take surrogate pairs into account.  (142098484)
- Fixed tokenization of the rel attribute of the link element and Link header.  (142600096)

###### Deprecations

- Removed wheel event handling for `<input type="number">` to match platform conventions.  (99318505)

##### Web Authentication

###### Resolved Issues

- Fixed `.catch()` for conditional mediation  not getting passed the abort reason that was thrown.  (112178073)

##### Web Extensions

###### New Features

- Added support for loading Safari Web Extensions that have been Developer ID-signed and notarized.  (40429283)
- Added support for temporarily installing web extensions from disk without requiring an Xcode project.  (98208121)
- Added support for `getKeys()` in storage areas.  (136595295)
- Added support for `i18n.getSystemUILanguage` and `i18n.getPreferredSystemLanguages`.  (136929657)
- Added support for `documentId` to the `sender` message object.  (137532821)
- Added support for `documentId` to `tabs.sendMessage()` and `tabs.connect()`.  (137532897)
- Added support for `documentId` in `webNavigation`.  (137532909)
- Added support for `documentId` to `webRequest`.  (141058456)
- Added support for `documentId` to `scripting` and `tabs`.  (141291546)
- Added support for `match_about_blank` and `match_origin_as_fallback` to inject content scripts and styles into more frames.  (145875291)

###### Resolved Issues

- Fixed CORS for Web Extension pages to respect granted per-site permissions. Developers will need to add a `browser.permissions.request({origins: []})` call before doing any `fetch()` that is blocked by CORS.  (102912898)
- Fixed an issue causing content blockers to not hide content in `about:blank` frames.  (134273470)
- Fixed a slowdown in applying rulesets and dynamic rules in declarativeNetRequest.  (136394861) (FB15196130)
- Fixed clicking the “Clear Storage…” button in Safari Extensions Settings.  (137533628)
- Fixed `storage.onChanged` returning undefined as the `areaName`.  (138086765)
- Fixed the `tabs` field missing from the result returned by `windows.create`.  (138529797)
- Fixed es-419 support in Web Extensions.  (138857112)
- Fixed the `webRequest.onBeforeRequest` event missing the `requestBody`.  (140338580) (FB15911234)
- Fixed blurry extension icons.  (142070967) (FB16171862)
- Fixed not picking the “zh” locale when “zh-Hant” is preferred.  (142602243) (FB16271745)
- Fixed `webRequest` event listeners to honor `extraInfoSpec` for better performace.  (142907168)
- Fixed web extension resources to be treated as UTF-8 by default.  (143079179)

##### Web Inspector

###### New Features

- Added support for `ignoreList` in sourcemaps.  (130630075)
- Added support for viewport presets in Responsive Design Mode.  (131541189)
- Added support for the Apps and Devices Inspector.  (134519731)
- Exposed cookie Partition Key in Web Inspector.  (136293236)
- Added the ability to modify only the headers of a request using a Request Local Override.  (139043491)
- Added support for sending Android user agents using the device override menu when Web Inspector is connected to a remote device.  (139305520)
- Added support for `DOMRect` in `console.screenshot`.  (141650264)
- Added an orientation toggle to rotate a viewport preset in Responsive Design Mode.  (142632311)

###### Resolved Issues

- Fixed ensuring that all of the Desktop Sites on iPad site-specific hacks are disabled when the site-specific hacks setting is turned off in Web Inspector.  (50035167)
- Fixed style rules to stay editable after being modified by CSSOM in JavaScript.  (124650808)
- Fixed glitches when trying to edit a style from a stylesheet that has an `@import` statement.  (131756178)
- Fixed error cases to match new source map specification.  (137934436)
- Fixed the overview icon to be inverted dark mode in the Graphics tab.  (140602803)
- Fixed recorded WebGL objects not getting highlighted correctly in the Graphics tab.  (140625113)

##### Webassembly

###### New Features

- Added support for JIT-less Wasm.  (113768974)
- Added support for the new Wasm Exception Specification.  (131409318)
- Implemented relaxed laneselect SIMD instructions.  (138484223)

###### Resolved Issues

- Fixed Wasm legacy `catch_all` instruction to correctly catch thrown JS primitives.  (135972897)

##### Webdriver

###### Resolved Issues

- Fixed a crash that could occur when simulating drag events with the right mouse button.  (137068514)

##### Webkit

###### New Features

- Added support for `WKWebExtension`, `WKWebExtensionContext`, and `WKWebExtensionController` Swift and Objective-C classes to support integrating Web Extensions into WebKit-based browsers.  (121537087)

##### Webrtc

###### New Features

- Added support for MediaSession capture mute API.  (131386187)
- Added support for stuns server URIs.  (136505783)
- Added support for enumerated visible network interfaces.  (137067672)
- Added support for the Speaker Selection API on macOS.  (140918327)

###### Resolved Issues

- Fixed `MediaSession.setMicrophoneActive(true)` prompting repeatedly if the microphone was muted by the user-agent once.  (135941062)
- Fixed `setCameraActive` to not unmute microphone if the user-agent previously muted both camera and microphone.  (136221456)
- Fixed AirPods unmuting to not unmute the camera if website muted the camera.  (137065964)
- Fixed voice search to not re-prompt for camera or microphone permission after a page-initiated same origin navigation.  (138122655)

##### Wkwebview

###### New Features

- Added support for customizing the file upload flow for file inputs.  (130219174)
- Added support for WKNavigationAction/buttonNumber and WKNavigationAction/modifierFlags as API on iOS.  (136865172)
- Added support for the Writing Tools API in visionOS.  (140412673)

###### Resolved Issues

- Fixed calling `WKWebView.evaluateJavaScript` in an async context when nothing is returned by JS.  (139618495) (FB15755273)

## See Also

- [Safari 18.5 Release Notes](safari-18_5-release-notes.md)
  Released May 12, 2025 — 18.5 (20621.2.5)
- [Safari 18.3 Release Notes](safari-18_3-release-notes.md)
  Released January 27, 2025 — 18.3 (20620.2.4)
- [Safari 18.2 Release Notes](safari-18_2-release-notes.md)
  Released December 11, 2024 — 18.2 (20620.1.16)
- [Safari 18.1 Release Notes](safari-18_1-release-notes.md)
  Released October 28, 2024 — 18.1 (20619.2.8)
- [Safari 18.0.1 Release Notes](safari-18_0_1-release-notes.md)
  Released October 3, 2024 — 18.0.1 (20619.1.26.30)
- [Safari 18.0 Release Notes](safari-18-release-notes.md)
  Released September 16, 2024 — 18.0 (20619.1.26)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-18_4-release-notes)*