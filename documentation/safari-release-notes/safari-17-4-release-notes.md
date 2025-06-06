# Safari 17.4 Release Notes

**Framework**: Safari Release Notes

Released March 5, 2024 — 17.4  (19618.1.15)

#### Overview

Safari 17.4 is available for iOS 17.4, iPadOS 17.4, visionOS 1.1, macOS Sonoma, macOS Monterey, and macOS Ventura.

##### Accessibility

###### New Features

- Added support for the new CSS `content` alternative text syntax.  (26942023)

###### Resolved Issues

- Fixed exposing the correct `<summary>` element role.  (13661104)
- Fixed non-accessible content within iframes with ARIA roles.  (104611075)
- Fixed VoiceOver word echo on text inputs with a `combobox` role.  (112488137)
- Fixed an issue where `innerHTML` and `innerText` changes to labels did not update their corresponding input element’s accessibility title.  (113872525)
- Fixed `<details>` and `<summary>` elements not included in VoiceOver form controls menu or list.  (117308226)
- Fixed comboboxes not notifying assistive technologies when `aria-activedescendant` changes.  (117747058)
- Fixed toggling accessibility preferences to correctly update form control appearance.  (117914468)
- Fixed: Removed the default ARIA-level heading for a heading role, matching removal from ARIA specifications.  (119059172)
- Fixed text missing from accessibility labels for many common shadow DOM scenarios.  (120223342)

##### Autofill

###### New Features

- Added support for Apple Cash virtual card numbers and showing the user their Apple Cash balance when using AutoFill.  (107634154)

##### Browser Changes

###### New Features

- Added support for webpage translation in `<iframe>` elements.  (99293324)
- Added support for hiding titles in the Favorites Bar.  (119145918)

###### Resolved Issues

- Fixed loading a ⌘Click fragment link in a background tab.  (119079650)

##### Css

###### New Features

- Added support for `@scope`.  (82359096)
- Added support for percentages in `letter-spacing` and `word-spacing`.  (114538918)
- Added support for `align-content` on block containers.  (114740670)
- Added support for invalidating `:any-link`, `:link`, and `:-webkit-any-link` inside `:has()`.  (116616425)
- Added the `white-space-collapse` and `text-wrap-mode` CSS properties.  (117248327)
- Added support for CSS custom properties of `::backdrop`.  (117949961)
- Added support for `::grammar-error` and `::spelling-error`  (119314048)
- Added support for `align-content` on table cells.  (119701629)

###### Resolved Issues

- Fixed the default link color contrast for the dark color scheme.  (61149466)
- Fixed `getComputedStyle()` for invalid pseudo-elements.  (98504661)
- Fixed `querySelector()` to not throw an exception for `-webkit-` prefixed pseudo-elements.  (99299129)
- Fixed `:user-invalid` triggering while typing a date.  (110687369)
- Fixed: Updated `text-transform: full-size-kana` to align with Unicode 15.  (111508663)
- Fixed `contain: inline-size` breaking `grid-template-rows: auto`.  (113915953)
- Fixed `svh` and `dvh` units being unexpectedly equal when the Safari tab bar is not visible.  (115085360)
- Fixed `mixed-blend-mode` to blend correctly against the root background.  (115688282)
- Fixed `backdrop-filter` with many interoperability improvements.  (115703346)
- Fixed `oklab` and `oklch` lightness value clamping.  (116195533)
- Fixed flex layout invalidation in cases where the content of a flex item changes or style changes impact the preferred widths computation of its items.  (117181858)
- Fixed selection gaps to get painted with the expected `::selection` pseudo-element color.  (117796745)
- Fixed parsing and serialization of `-webkit-` prefixed pseudo-elements.  (118081134)
- Fixed `::backdrop` to be allowed after `::slotted()`.  (119015204)
- Fixed to allow `:checked` and `:indeterminate` to match at the same time.  (119075969)
- Fixed grid with size containment and `min-height` not sizing row correctly.  (119736473)
- Fixed computing values of basic shape `rect()` and `xywh()` as the equivalent `inset()`.  (119739406)
- Fixed poor performance with `:has(+ :not(.class))` pseudo-class selector.  (119819247)
- Fixed CSS `content` computed value serialization.  (120061551)
- Fixed pseudo-element parsing in `getComputedStyle()` and `KeyframeEffect.prototype.pseudoElement` so they require them starting with `::` (or `:` for 4 legacy pseudo-elements).  (120170550)
- Fixed CSS `linear()` easing.  (120290721)
- Fixed named at-rule container getting skipped when  the container is named in a `:host` selector.  (120428386)
- Fixed `:not(:has(:not(foo)))` getting misclassified as scope breaking.  (120492012)
- Fixed the name for a `::slotted` pseudo-element in a container query getting resolved against the wrong scope.  (122224135)

###### Deprecations

- Made `-apple-` prefixed pseudo-elements no longer valid.  (120268884)

##### Forms

###### New Features

- Added support for vertical writing mode support for form controls.  (12072686)
- Added support for `<hr>` inside `<select>` rendered as a separator on iOS.  (108783915)
- Added support for the `showPicker()` method for `<input type="date">` on macOS.  (110099910)
- Added support for `<input type="checkbox" switch>`.  (119378678)

###### Resolved Issues

- Fixed `<select>` not refreshing the dropdown after an `<option>` is removed on iPad.  (88292987)
- Fixed `text-indent` to affect the selected file(s) label for file inputs.  (105223868)
- Fixed `dir=auto` to work for `hidden`, `password`, `submit`, `reset`, and `button` input types, made `dirname` work for `password` and `submit` input types, and removed `dirname` support from `number` input types.  (113127508)
- Fixed serialization of `autocomplete` with a `webauthn` token.  (116107937)
- Fixed `<option>` elements outside of an `<optgroup>` getting added to the preceding group.  (117930480)

##### Fullscreen

###### Resolved Issues

- Fixed viewport units to be correct after entering and exiting fullscreen mode on iOS, iPadOS, and in visionOS.  (120496571)

##### Html

###### Resolved Issues

- Fixed the `system-ui` font family within `<canvas>`.  (117231545)
- Fixed `<progress>` to use the page’s preferred rendering update interval.  (118976548)
- Fixed missing support for the `direction` attribute in the list of attributes whose values are matched case-insensitively with attribute selectors.  (119432066)

##### Javascript

###### New Features

- Added support for `Promise.withResolvers`.  (116473362)
- Added `TimeZoneOffset` format support to `Intl.DateTimeFormat`.  (117124296)
- Aligned the implementation of the internal function IntlMathematicalValue (used in `Number.prototype.toLocaleString`, and `Intl.NumberFormat`) with its current specification.  (117535507)
- Enabled Array group methods.  (118037635)
- Added support for `ArrayBuffer.prototype.detached`, `ArrayBuffer.prototype.transfer`, and `ArrayBuffer.prototype.transferToFixedLength`.  (118037759)

###### Resolved Issues

- Fixed stringification algorithm of the Function constructor to match specifications.  (102065151)
- Fixed block-level function declarations to have correct scope in global code and aligned the detection of hoistable block-level legacy function declarations with the spec.  (113880075)
- Fixed an edge case with detecting a semantic error in generators.  (117497786)
- Fixed Temporal API to throw TypeErrors for unexpected primitives.  (117992134)
- Fixed Temporal options handling to align with the specification.  (118088676)
- Fixed `Temporal.Now.timeZone()` to be updated to `timeZoneId()`.  (118674314)

##### Loading

###### Resolved Issues

- Fixed Link-stylesheet elements to not fire load events for non-text/css and non-2XX responses.  (116112223)
- Fixed link-stylesheet elements to not fire load events for non-2XX responses such as 3XX responses that do not redirect.  (116331826)

##### Lockdown Mode

###### Resolved Issues

- Fixed Lockdown Mode disabling on sites with COOP and COEP HTTP headers.  (119503109)

##### Media

###### New Features

- Added support for all of HTML’s character entities in WebVTT.  (51064890)
- Added support for VP8/VP9 and WebM on iOS and iPadOS.  (64825245)
- Added WebCodecs HEVC support.  (112067287)
- Added MediaStream support for `whiteBalanceMode`.  (115552800)
- Added support for the Vorbis audio codec on iOS, iPadOS, and in visionOS.  (116776158)
- Added prioritizing video sources with power efficient hardware-decoded codecs before software-decoded codecs.  (120679553)

###### Resolved Issues

- Fixed WebVTT regions to position according to specifications.  (23091897)
- Fixed pausing MediaRecorder continuing to call `ondataavailable` at every timeslice event.  (115979604)
- Fixed an HEVC decoder issue when translating annexb data.  (116768196)
- Fixed WebVTT to treat negative percentages as invalid values.  (117615681)
- Fixed `object-fit: fill` on `<video>` elements.  (118020922)
- Fixed WebRTC calls not unmuting automatically after using Siri sometimes losing incoming audio.  (118461093)
- Fixed white bars across the top and bottom of fullscreen video playback while using Light Mode.  (118530255)
- Fixed the always empty `video.buffered` attribute.  (118550061)
- Fixed WebVTT to correctly parse region `id` settings.  (118551267)
- Fixed VideoEncoder produces no frames with latencyMode “realtime” when framerate/bitrate are not given.  (118725549)
- Fixed AV1-in-MP4 codec string not shown in Show Media Stats.  (118850797)
- Fixed `getDisplayMedia` `frameRate` always at 30 regardless of constraints.  (118874132)
- Fixed returning to fullscreen from picture-in-picture breaking subsequent touch input.  (119832557)
- Fixed HLS video captions where there are multiple text tracks available.  (119839950)
- Fixed fullscreen video not scaling to display size when the Safari window is in Full Screen App Mode.  (119893556)
- Fixed handling key renewal requests that cause playback errors for some DRM content.  (120230860)
- Fixed camera and mic activation failure due to media capability granting and activation order.  (120510826)
- Fixed paint-on captions shifting during playback.  (120847946)
- Fixed videos shifting up and down when fullscreen overlay controls appear or disappear.  (120848395)
- Fixed volume slider flickering when adjusting volume in Safari in visionOS.  (120855936)
- Fixed blocked encrypted sampled not getting enqueued after a CDM is attached to a SourceBuffer.  (120879185)
- Fixed video playback on Twitter.com in Safari in visionOS.  (121391975)
- Fixed Netflix.com content that can become zoomed-in and cropped when in fullscreen mode.  (121822831)
- Fixed pseudo-element font size calculation to fix subtitle size in fullscreen mode.  (122584350)

##### Rendering

###### Resolved Issues

- Fixed incorrectly oriented Traditional Mongolian script characters.  (93426525)
- Fixed resizing behavior with `writing-mode: vertical-rl` or `direction: rtl`.  (102620110)
- Fixed opacity and rendering the root element background image.  (115396444)
- Fixed the color of the drop shadow to preserve its alpha channel.  (115812347)
- Fixed filters with outsets to repaint the entire filterRegion if GraphicsStyles are used.  (115817290)
- Fixed compositing the filter style transparency layers to not clip the destination context.  (115901634)
- Fixed a bug where the returned transform from `getComputedStyle` was incorrect.  (117523629)
- Fixed handling images with color spaces not supported by the backend to fallback to render in sRGB.  (118238178)
- Fixed check boxes and radio buttons to avoid floats.  (118660695)
- Fixed rendering for a `<div>` within a transformed parent `<div>` with  `overflow: hidden`.  (118901069)
- Fixed rendering issues when editing text.  (119833765)
- Fixed `offsetHeight` and `offsetWidth` are 0 for an inline box wrapping a block.  (119955792)
- Fixed a floating element causing a list item bullet to be orphaned on constrained lines.  (120022893)
- Fixed incorrect inline box (hugging) outline painting in vertical writing modes.  (120217559)
- Fixed incorrect `ch` unit value in `vertical-rl` and `vertical-lr` when `text-orientation` is not upright.  (120293590)
- Fixed graphics artifacts when scrolling a Heroku app.  (120373474)
- Fixed `overflow: hidden` to not prevent CSS Subgrid from applying.  (120848131)
- Fixed the repaint area for underline text decorations.  (121082290)
- Fixed `align-content` and `justify-content` on scroll containers causing overflowing content to become inaccessible.  (121366949)
- Fixed rendering floats and an out-of-flow `<br>` element with `clear`.  (121444267)
- Fixed a line break at gaps between two inline elements in a container with `white-space: nowrap`.  (121859917)
- Fixed cropped first letter for custom fonts that report negative advance width.  (121891210)

###### Deprecations

- Removed `margin-trim` behavior for floats to match specification changes.  (115794102)

##### Safari Extensions

###### New Features

- Extensions that haven’t been granted permission to Private Browsing can now open Private Browsing windows.  (105983371)

###### Resolved Issues

- Fixed sending an error back to the caller if an error occurs for `scripting.executeScript()`.  (107996753)
- Fixed an issue where scripts may not be removed after calling `scripting.unregisterContentScripts()`.  (113171510)

##### Scrolling

###### Resolved Issues

- Fixed unusable horizontal scrollbars for right-to-left, `vertical-rl`, or flexbox reverse mode elements.  (104944522)
- Fixed a `scrollTo()` followed by an animated scroll ending at the wrong scroll position.  (117608836)
- Fixed wheel overflow behavior with Shadow DOM elements.  (118496293)
- Fixed keyboard scrolling beyond the page getting stuck at a bad scroll offset.  (120053910)

##### Storage

###### Resolved Issues

- Fixed cases where website data is unexpectedly evicted.  (119818267)

##### Svg

###### New Features

- Added support for `kernelUnitLengthX` and `kernelUnitLengthY` for SVGFESpecularLightingElement.  (118768259)

###### Resolved Issues

- Fixed applying `rx` or `ry` exclusively via CSS having no effect.  (113500023)
- Fixed negative SVGTransform scale values to be correctly stringified.  (118656892)
- Fixed the layout of an SVG when it is inside an `<iframe>` without affecting the size of the `<iframe>`.  (120178866)

###### Deprecations

- Removed support for SVGRenderingIntent.  (102516681)

##### Urls

###### Resolved Issues

- Fixed CSS invoked URL parsing to always use UTF-8 as agreed by the W3C CSS WG.  (114889625)

##### Web Animations

###### New Features

- Added support for `transition-behavior: allow-discrete`.  (108703206)

###### Resolved Issues

- Fixed style invalidation for animations.  (118500247)
- Fixed a paused animation where `currentTime` is changed to 0 not restarting when unpaused.  (118826588)

##### Web Api

###### New Features

- Added `Element.prototype.setHTMLUnsafe()`, `ShadowRoot.prototype.setHTMLUnsafe()`, and `Document.parseHTMLUnsafe()` methods.  (115345128)
- Added `scaleNonUniform` in DOMMatrixReadOnly.  (117875678)
- Added support for `AbortSignal.any()`.  (117985827)
- Added support for `element.checkVisibility()`.  (118157977)
- Added ShadowRoot `clonable` property.  (119707278)
- Added support for CustomStateSet in custom elements and `:state()` pseudo-class.  (120072599)

###### Resolved Issues

- Fixed invalid coordinates on `wheel` and `gesturechange` events inside an iframe.  (105243167)
- Fixed HTMLAreaElement to align with the HTML Standard.  (110028213)
- Fixed the result of `Range.getClientRects()` and `Range.getBoundingRect()` for certain ranges.  (112543805)
- Fixed Scroll To Text Fragment to not scroll after dynamic stylesheet loads and the user has scrolled.  (112608578)
- Fixed SharedWorker referrer policy to default to its context referrer policy if none is provided in its script http response.  (114625126)
- Fixed URL encoding for `Request`’s `referrer` feature and `Response.redirect()`. They now always use UTF-8.  (115219660)
- Fixed reprocessing `<meta name="color-scheme">` when their `name` or `content` attribute changes.  (115958450)
- Fixed `FetchResponse.formData()` to parse headers names as case insensitive.  (116742000)
- Fixed declarative shadow trees to match the latest specifications.  (117655691)
- Fixed jiggling caused by repeated calls to `scrollIntoView({ block: 'center' })`.  (117755250)
- Fixed fullscreen warning banner to prevent cutting off long domain names.  (118078137)
- Fixed updating `resizeBy` and `resizeTo` to use `int` rather than `float` to align with specifications.  (118872048)
- Fixed the CookieChangeEvent to not be exposed when the Cookie Store API is disabled.  (118902989)
- Fixed `Element.prototype.setAttributeNode()` to not treat attribute names case insensitively.  (119013600)
- Fixed toggling the `spellcheck` attribute not toggling spelling markers on input elements.  (119269616)
- Fixed removing highlights in the Custom Highlights API.  (119531671)
- Fixed `getElementsByName()` to only return HTML elements, not SVG, MathML, or other types of elements.  (120275680)
- Fixed the `button` value for a `pointerup` event not matching the `pointerdown` event.  (120429508)
- Fixed a wheel event to fire on an element that has been re-inserted after `document.open`.  (120893136)
- Fixed Scroll To Text Fragment Text Directives to find text with additional unrendered white space in their node data.  (120913588)
- Fixed changing HTMLCanvasElement width or height causing intermediate buffer allocations.  (122309325)
- Fixed canvas `captureStream` stuttering with WebGL.  (122471664)

##### Web Apps

###### New Features

- Added support for the shortcuts manifest member on macOS. Shortcuts are available in the File menu and the Dock context menu. Users can set up custom keyboard shortcuts for them in System Settings > Keyboard > Keyboard Shortcuts > App Shortcuts.  (106137954)
- Added support for the categories manifest member on macOS. When creating a Launchpad folder containing web apps, the folder is automatically named accordingly.  (116480550)

##### Web Assembly

###### New Features

- Enabled extended constant expressions.  (118190467)

##### Web Inspector

###### New Features

- Added support for grouping source map load errors.  (109239646)
- Added support for logging a message to the Console when a page attempts to load a font URL blocked by Lockdown Mode.  (114657783)

###### Resolved Issues

- Fixed Home Screen Web Apps in Simulator to be listed under a “Home Screen Web Apps” section in the device submenu of the Develop menu.  (117742935)
- Fixed the `tan()` function to not trigger the color picker.  (118724061)

##### Webauthn

###### New Features

- Added support for `getClientCapabilities()`.  (119058559)

##### Webgl

###### New Features

- Added support for new WebGL extensions: - `EXT_clip_control`
- `EXT_depth_clamp`
- `EXT_polygon_offset_clamp`
- `WEBGL_polygon_mode`  (118110035)

###### Resolved Issues

- Fixed Canvas WebGL context capture to WebCodecsVideoFrame not capturing all frames.  (108459224)
- Fixed: Improved performance of MSAA rendering, including antialiased default framebuffer and fixed PBO uploads of PVRTC1 textures.  (117461678)
- Fixed WebGL OffscreenCanvas returning the previously created WebGL1 context when asking for WebGL2.  (119028794)
- Fixed WebGL to be available in nested workers.  (120279728)

##### Webkit

###### Resolved Issues

- Fixed HTML content not displaying in a Simulator, affecting projects using the web extension project template.  (121338366)

##### Webrtc

###### Resolved Issues

- Fixed media tracks obtained with `{"width":1920,"height":1080,"frameRate":24}`.  (61747755)
- Fixed triggering resolution scaling in the case of WebRTC maintain-framerate `degradationPreference`.  (121041723)
- Fixed a bug that prevented HTML canvas elements from always being marked dirty on initialization. This could cause some video effects to have choppy animations.  (121257960)

## See Also

- [Safari 17.6 Release Notes](safari-17_6-release-notes.md)
  Released July 29, 2024 — 17.6 (19618.3.11)
- [Safari 17.5 Release Notes](safari-17_5-release-notes.md)
  Released May 13, 2024 — 17.5 (19618.2.12)
- [Safari 17.3 Release Notes](safari-17_3-release-notes.md)
  Released January 22, 2024 — Version 17.3 (19617.2.4)
- [Safari 17.2 Release Notes](safari-17_2-release-notes.md)
  Released December 11, 2023 — Version 17.2 (19617.1.17)
- [Safari 17.1 Release Notes](safari-17_1-release-notes.md)
  Released October 25, 2023 — Version 17.1 (19616.2.9)
- [Safari 17 Release Notes](safari-17-release-notes.md)
  Released September 18, 2023 — Version 17 (19616.1.27)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-17_4-release-notes)*