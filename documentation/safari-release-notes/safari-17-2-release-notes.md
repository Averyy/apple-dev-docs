# Safari 17.2 Release Notes

**Framework**: Safari Release Notes

Released December 11, 2023 — Version 17.2 (19617.1.17)

#### Overview

Safari 17.2 is available for iOS 17.2, iPadOS 17.2, macOS Sonoma, macOS Monterey, and macOS Ventura.

##### Accessibility

###### Resolved Issues

- Fixed parsing the ARIA `role` attribute to ignore leading and trailing whitespace, including line breaks.  (113923520)
- Fixed form landmarks being incorrectly exposed when they are missing a label.  (115462091)
- Fixed non-group and non-tree-item children of `role="treeitem"` elements becoming stale after dynamic changes.  (115936550)
- Fixed Play Animation and Pause Animation animated image context menu items sometimes not appearing after setting toggle.  (117215059)
- Fixed VoiceOver not announcing button labels if the button is in a shadow root.  (118118138)

##### Apple Pay

###### Deprecations

- Deprecated `enabled` in favor of `available` in `shippingContactEditingMode`.  (113159800)

##### Autofill

###### Resolved Issues

- Fixed clipping the “Strong Password” button after selecting “Suggest New Password”.  (113701243)

##### Css

###### New Features

- Added support for the CSS Custom Highlight API.  (68662936)
- Added support for `mask-border` properties.  (82991599)
- Added support for the `counter-set` property and support for the `list-item` value with the `counter-set`, `counter-reset`, and `counter-increment` properties.  (88663348)
- Added support for `linear(...)` timing function for CSS animations & transitions.  (93088094)
- Added support for the `cap` unit.  (97025854)
- Added support for the `<position>` parameter in `ray()`.  (110821024)
- Added the support for mixed percentage and length/number arguments in CSS `round()`, `mod()`, and `rem()` functions.  (113234898)
- Added new relaxed parsing behavior for CSS Nesting.  (113475843)
- Added support for `xywh()` shape for `shape-outside`, `clip-path` and `offset-path`.  (113643020)
- Added support for `offset-position: normal` for CSS Motion Path.  (113644765)
- Added support for the `rcap`, `rex`, `ric`, and `rch` units.  (114367871)
- Added support for `rect()` shape for `shape-outside`, `clip-path` and `offset-path`.  (114479534)
- Added new typed OM factory functions for font and root font relative units.  (114482930)
- Added support for the `coord-box` parameter in `ray()`.  (114577300)
- Added support for `border-radius` when using  `<coord-box>`  in Motion Path syntax.  (114883507)
- Added `offset-position` support for `circle()` and `ellipse()`.  (114951375)

###### Resolved Issues

- Fixed the `font-family` descriptor for `@font-palette-values` to accept multiple values.  (105975619)
- Fixed `:has(:scope)` matching.  (106524140)
- Fixed container selection for container units in pseudo-elements.  (106739553)
- Fixed container query with font units to invalidate when the font changes.  (106739736)
- Fixed `:nth-child()` invalidation when not in subject position.  (106740353)
- Fixed `:has(:host)` invalidation.  (106768205)
- Fixed `:has(:nth-child())` invalidation and related.  (106768224)
- Fixed invalidating scope-breaking `:has(:is(...))` selectors.  (106768250)
- Fixed handling dynamic updates to viewport units when used in `@property` initial value.  (108287215)
- Fixed baseline aligned flex items to also be aligned using their fallback alignment.  (109496710)
- Fixed: Changed to allow an empty `font-family` name in `@font-face` and `@font-palette-values`.  (109613703)
- Fixed the `<basic-shape>` implementation for `offset-path`.  (110565070)
- Fixed `:user-invalid` and `:user-valid` interactions with form reset and submission.  (110677832)
- Fixed `<coord-box>` implementation for `offset-path`.  (110938788)
- Fixed `<position>` to never serialize to a single value.  (111750372)
- Fixed `NaN` numeric representation to be `0` not `Infinity`.  (111984451)
- Fixed serializing CSS math function root nodes.  (111984509)
- Fixed `min()` and `max()` with one argument to always collapse to `calc()`.  (111986569)
- Fixed animation using `padding-block` or `padding-inline` not overriding the set padding style.  (112023856)
- Fixed `color-mix()` to respect `:visited` style to resolve “currentcolor”.  (112419198)
- Fixed serialization to always serialize implicit `&` and an implicit nested rule.  (112900363)
- Fixed `<hr>` `width` attribute set to `0` or `0px` to correctly compute to `0px`.  (113087533)
- Fixed `mod()` evaluation.  (113213059)
- Fixed `round()` evaluation when the number is a multiple of the step.  (113233588)
- Fixed computation of the `from-font` value for `font-size-adjust`.  (113328110)
- Fixed the serialization of percentages in `color-mix()`.  (113399146)
- Fixed `border-image` to fall back to the `border` property if the image is invalid.  (113646392)
- Fixed `<family-name>` to forbid generic families.  (113746537)
- Fixed the check for in-progress layout when setting a containing block rect for `ray()` used with `motion-path`.  (113780201)
- Fixed animating a `rotate` property when the `scale` property is also used.  (113999490)
- Fixed `<resolution>` to not accept negative resolutions for `@property`.  (114235642)
- Fixed `currentcolor` to correctly inherit computed `:visited` style.  (114254856)
- Fixed nested subgrids from contributing to the calculation of the enclosing track size.  (114271839)
- Fixed `container-name` to use scoped names.  (114284428)
- Fixed container unit resolution to check if the selected container is eligible.  (114291153)
- Fixed the `scripting` media query to never match `initial-only`.  (114340361)
- Fixed form submission to also affect `:user-invalid` and `:user-valid` state.  (114580382)
- Fixed the container for the `::part` pseudo-element to be selected from the originating element tree.  (114626579)
- Fixed serialization of `infinity` and `-infinity` in colors.  (114808320)
- Fixed `lab`, `lch`, `oklab`, `oklch` components to be clamped to appropriate ranges.  (114808444)
- Fixed `color-mix()` to not serialize to legacy color syntax.  (114949008)
- Fixed resolving the size of a replaced element by using its intrinsic size as the width.  (115007278)
- Fixed basic shapes to use an offset motion path.  (115068196)
- Fixed grid to not always put first and last baseline aligned items into different alignment contexts.  (115083708)
- Fixed determining non-orthogonal grid item’s columnAxisPosition by considering fallback alignment for first/last baseline.  (115136343)
- Fixed `:has(~ :is(.x ~ .y))` to consider all siblings of the `:has` scope when invalidating.  (115205991)
- Fixed invalidating `:default` pseudo-class changes on input elements.  (115236525)
- Fixed `calc(clamp(1px, 1em, 1vh))` to collapse to `clamp(1px, 1em, 1vh)`.  (115240159)
- Fixed offset path inset shapes with a `border-radius`.  (115316728)
- Fixed determing baseline for grid by considering the first and last baseline-aligned grid items.  (115441833)
- Fixed the serialization of the computed style of `grid-area`.  (115521493)
- Fixed not serializing `at <position>` in `circle()` or `ellipse()` if unspecified.  (115866108)
- Fixed serialization of `shape-outside`.  (115938310)
- Fixed serialization issues with `clip-path` and `offset-path`.  (115953688)
- Fixed `getComputedStyle()` to return a resolved value for `font-size-adjust: from-font`.  (116151111)
- Fixed non-orthogonal subgrid margin, border, and padding to be considered for self-align baseline items in the same alignment context.  (116206243)
- Fixed subgrids to have their row-start margins resolved after column sizing in the outer grid.  (116369419)
- Fixed accumulating the sum of non-orthogonal nested subgrids margin, border, and padding for first baseline alignment in the column axis.  (116443747)
- Fixed CSS grid support for last baseline alignment in the column axis for subgrid items with non-orthogonal ancestors.  (116484865)
- Fixed validating `@property` at parse-time.  (116803886)
- Fixed computing the definite free space of grid rows when the grid has an `aspect-ratio` and definite logical width.  (117138268)
- Fixed the continuity of transform animations through singular transforms.  (117209302)
- Fixed `@supports selector(:popover-open)` to reflect disabled state.  (117226626)
- Fixed CSS grid to synthesize the central baseline of grid items in the column axis.  (117424263)
- Fixed serialization for CSS highlight pseudo-elements.  (117864974)

##### Dom

###### Resolved Issues

- Fixed handling tasks scheduled for web pages in the back-forward cache.  (116349535)

###### Deprecations

- Removed the non-standard `incremental` attribute and `search` event.  (48937114)

##### Fonts

###### Resolved Issues

- Fixed COLRv0 font rendering.  (115721319)

##### Html

###### New Features

- Added support for the `name` attribute in the `<details>` element.  (114677170)
- Added support for `one-time-code` as an allowed `autocomplete` field name.  (115684196)

###### Resolved Issues

- Fixed `<input type="number">` not returning the correct value when a decimal is entered.  (107187010)
- Fixed alert sounds in web apps being replayed when the system play/pause key is pressed. Playing short-duration `<audio>` sources no longer registers the page as the system’s Now Playing application.  (114667001)
- Fixed dynamic handling of `<base>` elements.  (114756660)
- Fixed URL encoding of `<base>` elements.  (114861187)
- Fixed URL encoding of SVG `<image>` elements.  (114873373)
- Fixed empty value attributes to not be ignored on image input types.  (114887143)
- Fixed `[dir=auto]` invalidation with password fields.  (115887776)

##### Http

###### Resolved Issues

- Fixed COOP header breaking back and forward behavior when client-side redirects are involved.  (104659192)

##### Javascript

###### New Features

- Added support for `Intl.NumberFormat`’s FormatApproximately operation.  (113461245)
- Added support for `import` attributes.  (113940597)

###### Resolved Issues

- Fixed an edge case in the semantics of `for` loops.  (44730906)
- Fixed: Optimized `Array#splice` to skip result array creation if it is not used at all.  (113367762)
- Fixed: Updated `Intl.DateTimeFormat`’s to obtain options only once, matching spec changes.  (113789192)
- Fixed: Increased `minimumFractionDigits` and `maximumFractionDigits` limit from 20 to 100.  (113869343)
- Fixed rounding to nearest in optimizing JITs.  (114208146)
- Fixed global and eval code to throw a TypeError if a function declaration attempts to shadow a non-configurable, non-writable global property.  (114215396)
- Fixed `Intl.NumberFormat` and `Intl.PluralRules` `roundingIncrement` to match specification changes.  (114219889)

##### Loading

###### Resolved Issues

- Fixed navigation to about scheme URLs without opaque paths.  (116238322)

##### Media

###### New Features

- Added unprefixed support for `preservesPitch`.  (66579074)
- Implemented automatic text track selection for `'metadata'` tracks.  (113004825)
- Added support for H264 L1T2 for WebCodecs.  (114940765)

###### Resolved Issues

- Fixed an issue where Safari would briefly change `document.visibilityState` to `hidden` when entering fullscreen.  (104984915)
- Fixed `canplay` event to fire for video elements where the first sample’s presentation time is slightly greater than 0.  (105169372)
- Fixed `RTCRtpSender maxFramerate` encoding parameter having no effect.  (112397603)
- Fixed handling `NaN` in audio delay curves.  (114881060)
- Fixed WebCodecs hardware encoders losing a frame.  (115252749)
- Fixed audio elements with event listeners not getting garbage collected.  (116346717) (FB13224538)
- Fixed the close algorithms for audio and video WebCodec decoders and encoders to match specification changes.  (116346725)
- Fixed picture-in-picture when the `srcObject` is a video stream.  (116465668)
- Fixed constraints on the maximum width or height causing blurry `getDisplayMedia` video.  (116810370)
- Fixed `object-fit: fill` to work for a video element using a canvas stream `srcObject`.  (116832514)
- Fixed the limit for the number of real-time audio threads.  (116864442)

##### Networking

###### Resolved Issues

- Fixed an issue causing embedded videos in iWork documents to fail.  (116493190)

##### Privacy

###### New Features

- Added support for blob partitioning.  (94442816)

##### Rendering

###### Resolved Issues

- Fixed the scrollbar not updating on CSS color-scheme change.  (99567600)
- Fixed ignoring `calc()` values on `<colgroup>` elements.  (106692191)
- Fixed out-of-flow boxes not showing.  (112733052) (FB12722063)
- Fixed out-of-flow `<br>` to not trigger a line break.  (113208050)
- Fixed ancestor subgrids’ gutters to add to the extra layer of margin for descendant subgrids.  (114271857)
- Fixed a bug where swapping to Safari from another app (or tab) would flash black.  (116530284)

##### Safari

###### Resolved Issues

- Fixed website notifications delivered through APNS to appear with the domain name and Safari icon, matching the appearance of website notifications delivered through Web Push.  (116612341)

##### Safari Extensions

###### Resolved Issues

- Fixed an issue where dynamic declarativeNetRequest rules would not override static rules.  (107044339) (FB12074742)
- Fixed behavior of `domains`, `requestDomains`, `excludedDomains`, and `excludedRequestDomains` declarativeNetRequest values to match subdomains by default.  (117592996)

##### Scrolling

###### Resolved Issues

- Fixed clicking and dragging the overlay scrollbar that overlaps a composited, positioned descendant of a container with `overflow: scroll`.  (89598421)
- Fixed scrolling on nested `pointer-events: auto` inside `pointer-events: none`.  (110954175)
- Fixed a bug that caused some complicated websites to freeze when scrolling.  (113318934)

##### Service Workers

###### Resolved Issues

- Fixed a cache miss bug in DOMCache that triggered service worker fetch errors.  (115740959) (FB13188943)

##### Svg

###### New Features

- Added the missing default value `translate` for `animateTransform`.  (113681862)
- Added support for SVG `<image crossorigin>`.  (114462749)

###### Resolved Issues

- Fixed the motion path anchor point used for SVG when the `transform-box` is not the `view-box`.  (108285569)
- Fixed `paint-order` property to inherit.  (114030037)
- Fixed the SVG mask to work as a mask-resource for the CSS `mask-image`.  (114465545)
- Fixed repainting an SVG element with a CSS reference filter when the filter changes.  (117047658)

##### Text

###### Resolved Issues

- Fixed font fallback to ignore generic families for Private-Use Area Unicode codepoints.  (115901340) (FB13197885)

##### Web Animations

###### Resolved Issues

- Fixed `color-scheme` to support discrete animation.  (94615599)

##### Web Api

###### New Features

- Added support for `CanvasRenderingContext2D.reset()`.  (77842434)
- Enabled responsive images in `<link rel=preload>`.  (83891023)
- Added support for `from-image` to ImageBitmapOptions.  (104398244)
- Added support for Fetch Priority.  (106852027)
- Added support for sending mouse events to disabled form controls.  (110656783)
- Added support for the `title` attribute for pattern validation errors.  (111394402)

###### Resolved Issues

- Fixed `createPattern` to return null for a zero height image.  (104285727)
- Fixed: Aligned `<script type language>` with the HTML Standard.  (109600797)
- Fixed  returning opaque origin for `blob:` URL containing inner non-http(s): URL.  (109781193)
- Fixed: Changed navigable target names to `_blank` if they have dangling markup.  (110134016)
- Fixed incorrect tab stop if the tab-size is a `<length>` and the distance to the next tab stop is less than `0.5ch`.  (112043546)
- Fixed `URL`, `pathname`, and `search` setter incorrectly stripping trailing spaces.  (112433299)
- Fixed custom highlight text decoration to respect priority.  (112494779)
- Fixed handling focusability for plugin elements which have browsing context.  (112821601)
- Fixed: Converted embed hidden into a proper boolean attribute.  (113051256)
- Fixed edge cases in parsing options.  (113826514)
- Fixed `<a>` and `<area>` origin getters to return an empty string for non-parsable URLs.  (114078288)
- Fixed `<a>` and `<area>` protocol setters for non-parsable URLs.  (114371380)
- Fixed URL’s protocol setter to forbid change a special URL to a non-special URL.  (114624048)
- Fixed Worker and SharedWorker to fire an Event instead of an ErrorEvent for a parsing error.  (114694487)
- Fixed `adoptedStyleSheets.length` to be settable and improved `ObservableArray` alignment with the specification.  (114822538)
- Fixed a bug that could cause incorrect equality checks between DOM Document objects.  (114857465)
- Fixed checking for `NaN` when creating a DelayNode for WebAudio.  (115008784)
- Fixed `element.querySelector(":has(:scope *)")` to never match.  (115158183)
- Fixed mutation events for child nodes.  (115527098)
- Fixed mouse event handling such that if a drag operation is initiated from a canceled `mousedown` event, all subsequent mouse events are sent to the originating frame until the drag operation ends with a corresponding `mouseup` event.  (116668701)
- Fixed light dismiss for a popover element within a complex shadow DOM breaks light dismiss calculation.  (117214343)

##### Web Apps

###### New Features

- Added support for copying cookies when saving a website to the Home Screen on iOS and iPadOS.  (104438319)
- Users can now enable the status bar from the View menu on macOS.  (109663387)
- Users can now set the current page as the homepage for web apps on macOS.  (112819599)

###### Resolved Issues

- Fixed many common issues such as an icon appearing blurry with jagged edges, lacking padding, or failing to load by improving how web app icons are loaded. If you supply multiple size variants for the preferred icon kind, all sizes are saved, allowing the most appropriate size to be displayed based on context. For example, the largest size variant is shown in Finder’s Gallery view and Quick Look, a medium sized variant is shown in the Dock and Launchpad, while a smaller sized variant is shown in Spotlight. To provide the best user experience, supply at least one opaque, full-bleed `maskable` square icon in the web app manifest, either as an SVG (any size) or high resolution bitmap (1024x1024). If the web app manifest doesn’t specify any high resolution full-bleed icon, Safari may fall back to the `apple-touch-icon` if it improves the user experience. If you specify an `apple-touch-icon` through `link` elements in the webpage, do not omit these link elements based on user agent detection. When you only supply a transparent icon with custom shape, Safari automatically adjusts spacing between your icon and the standard system background to avoid tangents.  (102449619)
- Fixed an issue where page zoom is reset to 100% after quit and relaunch.  (110298546) (FB12233006)
- Fixed a bug where `theme-color` is not applied to the title bar in web apps.  (112980819)
- Fixed an issue where sign in pages sometimes unexpectely open in Safari instead of the web app.  (113520837)
- Fixed an issue where clicking on notifications after 30 seconds from delivery fail to open the web app.  (113757950)
- Fixed an issue that repeatedly asks for camera access after relaunching a web app.  (114110664)
- Fixed remembering window size for a webpage added to the Dock.  (114534506)
- Fixed an issue where a blank window remains on screen after starting a download.  (115457207)
- Fixed an issue where some login pages unexpectedly open in Safari.  (115527738) (FB13171758)
- Fixed a bug where the `scope` member in the web app manifest is not respected.  (116261588)
- Fixed an issue where AutoFill settings in Safari do not take effect in web apps.  (117671220)
- Fixed an issue where option+clicking a link failed to start a download.  (117809013)
- Fixed an issue where JavaScript-based redirection to an external website causes a blank window to appear or the current window to disappear.  (117809066)
- Fixed an issue where web app usage is not reflected in Screen Time.  (117809075) - Fixed an issue that prevents Ignore Screen Time Limits from working in web apps.  (117809075)

##### Web Assembly

###### Resolved Issues

- Fixed WebAssembly SIMD vectors that can get corrupted when using `v128.any_true`.  (111050621)

##### Web Inspector

###### New Features

- Added color palette with CSS variables in color picker.  (112099603)
- Added a specialized editor for the CSS `steps()` timing function.  (113345146)

###### Resolved Issues

- Fixed: Moved the details sidebar to the bottom when Web Inspector is too narrow.  (63567675) (FB7711657)
- Fixed objects logged to the console with multiple private fields that use the same name.  (109215331)

##### Webdriver

###### Resolved Issues

- Fixed dispatched mouse events always having `buttons` property set to zero.  (116049187)

##### Webgl

###### New Features

- Added support for `EXT_blend_func_extended`.  (115158977)
- Enabled support for `WEBGL_clip_cull_distance` by default.  (115174172)

###### Resolved Issues

- Fixed a bug where multi-level textures would lose levels in WebGL.  (116362216)

##### Webrtc

###### Resolved Issues

- Fixed long delays switching audio input in video conferencing applications.  (102724364)
- Fixed video quality when using TransformStream with Simulcast.  (110395571)
- Fixed WebRTC UDP traffic to use interfaces already used by TCP traffic.  (111000448)
- Fixed RTCDataChannel to use BinaryType to align with specifications.  (114559008)

## See Also

- [Safari 17.6 Release Notes](safari-17_6-release-notes.md)
  Released July 29, 2024 — 17.6 (19618.3.11)
- [Safari 17.5 Release Notes](safari-17_5-release-notes.md)
  Released May 13, 2024 — 17.5 (19618.2.12)
- [Safari 17.4 Release Notes](safari-17_4-release-notes.md)
  Released March 5, 2024 — 17.4  (19618.1.15)
- [Safari 17.3 Release Notes](safari-17_3-release-notes.md)
  Released January 22, 2024 — Version 17.3 (19617.2.4)
- [Safari 17.1 Release Notes](safari-17_1-release-notes.md)
  Released October 25, 2023 — Version 17.1 (19616.2.9)
- [Safari 17 Release Notes](safari-17-release-notes.md)
  Released September 18, 2023 — Version 17 (19616.1.27)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-17_2-release-notes)*