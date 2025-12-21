# Safari 18.0 Release Notes

**Framework**: Safari Release Notes

Released September 16, 2024 — 18.0 (20619.1.26)

#### Overview

Safari 18.0 is available for iOS 18, iPadOS 18, visionOS 2, macOS 15, macOS Sonoma, and macOS Ventura.

##### Accessibility

###### New Features

- Added support for `<input type="datetime">`, `<input type="datetime-local">`, and `<time>` elements.  (118180250)
- Added support for `ariaBrailleLabel` and `ariaBrailleRoleDescription` element reflection properties.  (123926949)

###### Resolved Issues

- Fixed role assignment for `<header>` inside `<main>` and sectioning elements.  (48370244)
- Fixed range input not firing an input event when incremented or decremented via accessibility APIs.  (85707481)
- Fixed setting `aria-hidden` on a slot not hiding the slot’s assigned nodes.  (108762653)
- Fixed VoiceOver to read hidden associated labels.  (113631557)
- Fixed comboboxes to expose their linked objects correctly.  (121242926)
- Fixed VoiceOver support for `aria-activedescendant` on macOS.  (122590052)
- Fixed time input accessibility by adding labels to subfields.  (122590568)
- Fixed `aria-hidden=true` to be ignored on the `<body>` and `<html>` elements.  (123049663)
- Fixed `datetime` values being exposed to assistive technologies in the wrong timezone.  (123522296)
- Fixed wrong `datetime` value being exposed to assistive technologies for `datetime-local` inputs.  (123803281)
- Fixed ignored CSS content property replacement text when it is an empty string.  (123919677)
- Fixed the computed role for these elements: `dd`, `details`, `dt`, `em`, `hgroup`, `option`, `s`, and `strong`.  (124641956)
- Fixed hidden elements targeted by `aria-labelledby` to expose their entire subtree text, not just their direct child text.  (125634439)
- Fixed accessible name computation for elements with `visibility: visible` inside a container with `visibility: hidden`.  (125738704)
- Fixed updating table accessibility text when its caption dynamically changes.  (127263464)
- Fixed updating `aria-describedby` text after the targeted element changes its subtree.  (127390465)

##### Animations

###### Resolved Issues

- Fixed the `transition` property to produce the shortest serialization.  (119822401)
- Fixed the `animation` property to produce the shortest serialization.  (120439368)

##### Apple Pay

###### New Features

- Added support for funds transfer.  (104115471)

###### Resolved Issues

- Fixed arbitrary 8 digit limit on a line item’s total amount.  (112078798)

##### Authentication

###### New Features

- Implemented conditional credential creation.  (113573376)
- Added support for the WebAuthn PRF extension.  (119057355)
- Added support for using passkeys across related origins.  (121477346)

###### Resolved Issues

- Fixed `navigator.credentials.create()` rejects with “NotAllowedError: Operation Failed” after a conditional UI request is aborted.  (109936742)
- Fixed setting the cancel flag once the cancel completes regardless of a subsequent request occurring.  (124727713)

##### Canvas

###### New Features

- Added support for `willReadFrequently`.  (126739379)
- Added support for resolving a nested `currentcolor` used in `color-mix` or a relative color.  (128027026)

###### Resolved Issues

- Fixed `drawImage(detachedOffscreenCanvas)` to throw an exception.  (120451062)
- Fixed OffscreenCanvas failing to render to the placeholder with nested workers.  (126069375)
- Fixed losing the contents layer of the placeholder canvas of OffscreenCanvas when switching off the tab.  (126070648)
- Fixed `drawImage` to not alter the input source or the destination rectangles.  (127982607)
- Fixed toggling the visibility on a canvas parent undoing the effect of `clearRect()`.  (128226178)
- Fixed the Canvas `drawImage()` API to throw an exception when the image is in broken state.  (128588063)
- Fixed a detached OffscreenCanvas to not transfer an ImageBuffer.  (129270155)

###### Deprecations

- Removed support for OffscreenCanvasRenderingContext2D’s `commit()` method.  (126758254)

##### Cookies

###### Resolved Issues

- Fixed treating the lack of an explicit “SameSite” attribute as “SameSite=Lax”.  (96026173)

##### Css

###### New Features

- Added support for `currentColor` and system color keywords to Relative Color Syntax.  (100981965)
- Added support for `(prefers-contrast: custom)`.  (103658875)
- Added support for `content-visibility`.  (117156105)
- Added support for animating the `display` property.  (121662911)
- Added support for CSS Style Container Queries.  (122800215)
- Added support for View Transitions.  (123128491)
- Added support for the unprefixed `backdrop-filter`.  (123523441)
- Added support for the `:active-view-transition` pseudo-class.  (129851076)

###### Resolved Issues

- Fixed setting `white-space` to a non-default value dynamically on a whitespace or a new line.  (92559818)
- Fixed custom counter styles `disclosure-open` and `disclosure-closed` to point to the correct direction in right-to-left.  (109014745)
- Fixed `backface-visibility` to create a stacking context and containing block.  (114732608)
- Fixed `getComputedStyle()` to work with functional pseudo-elements like `::highlight()`.  (117864743)
- Fixed: Aliased `:-webkit-full-screen` pseudo-class to `:fullscreen`.  (120335917)
- Fixed: Aliased `:-webkit-any-link` to `:any-link` and `:matches()` to `:is()`.  (120337922)
- Fixed `getComputedStyle()` pseudo-element parsing to support the full range of CSS syntax.  (120471227)
- Fixed `@supports` to correctly handle support for some `-webkit` prefixed pseudo-elements that were incorrectly treated as unsupported.  (120577690)
- Fixed updating media-query sensitive meta tags after style changes.  (120854167)
- Fixed changing color scheme to update gradients with system colors or `light-dark()`.  (121285450)
- Fixed incorrect inline element size when using `font-variant-caps: all-small-caps` with `font-synthesis`.  (121314557)
- Fixed `:empty` selector to work with animations.  (122838142)
- Fixed preserving whitespace when serializing custom properties.  (123491915)
- Fixed updating style correctly for non-inherited custom property mutations.  (123645196)
- Fixed element removed by parent to end up losing the last remembered size.  (123975513)
- Fixed an incorrect difference between implicit and explicit initial values for custom properties.  (124573975)
- Fixed the contrast of Menu and MenuText system colors.  (125270664)
- Fixed keeping the shorthand value for CSS `gap` as-is in serialized and computed values.  (125335787)
- Fixed the style adjuster for `@starting-style` incorrectly invoking with a null element.  (125837628)
- Fixed excluding `-apple-pay-button` from applying to any element that supports `appearance: auto` and is not a button.  (126107516)
- Fixed missing color interpretation methods added to CSS color specifications.  (126444371)
- Fixed `hsl()` and `hsla()` implementation to match the latest spec changes.  (126722229)
- Fixed the implementation of `rgb()` and `rgba()` to match the latest spec.  (126830606)
- Fixed the `hwb()` implementation to match the latest spec.  (126924645)
- Fixed the remaining color types to be synced with the latest spec changes.  (127077683)
- Fixed carrying analogous components forward when interpolating colors.  (127170141)
- Fixed applying the fill layer pattern for `mask-mode`.  (127999241)
- Fixed `backdrop-filter: blur` to render for elements not present when the page is loaded.  (129517679)
- Fixed: Improved large Grid performance.  (130728344)
- Fixed some CSS properties causing quotes to be reset.  (132585704)

###### Deprecations

- Removed `WEBKIT_KEYFRAMES_RULE` and `WEBKIT_KEYFRAME_RULE` in CSSRule.  (97084520)
- Removed `:-webkit-full-screen-ancestor` pseudo-class.  (100782937)
- Removed `-webkit-alt` and `alt` properties.  (120051066)
- Removed the non-standard `resize: auto` rule.  (120138995)
- Removed `:-webkit-animating-full-screen-transition` pseudo-class.  (121302758)
- Removed `:-khtml-drag` pseudo-class.  (121303391)
- Removed `:-webkit-full-screen-controls-hidden` pseudo-class.  (121323330)
- Removed `:-webkit-full-page-media` pseudo-class.  (121752962)
- Removed `:-webkit-full-screen-document` pseudo-class.  (121816310)

##### Editing

###### New Features

- Added `writingsuggestions` attribute to HTML elements to opt into multiword text completions.  (114989563)

###### Resolved Issues

- Fixed an issue where input method editing would sporadically drop the composition range.  (130020224)
- Fixed dictation UI no longer showing up when beginning dictation after focusing an empty text field.  (131534054) (FB14277296)

##### Forms

###### New Features

- Added haptic feedback for `<input type=checkbox switch>` on iOS.  (125474921)
- Added support for partially transparent accent colors.  (130599744)

###### Resolved Issues

- Fixed displayed `datalist` dropdown to sync its `options` elements after a DOM update.  (54690831)
- Fixed input elements to use the `[value]` as the first fallback step base.  (107721910)
- Fixed `<select multiple>` scrollbars to match the used color scheme.  (123807167)
- Fixed updating the input value when selecting an `<option>` from a `<datalist>` element.  (124784204) (FB13688998)
- Fixed the value attribute not getting displayed in an `input` element with `type="email"` and the `multiple` attribute.  (125221858)
- Fixed the iOS animation for `<input type=checkbox switch>`.  (125563501)
- Fixed form controls drawing with an active appearance when the window is inactive.  (127391198)
- Fixed constructed FormData object to not include entries for the image button submitter by default.  (128176811)

##### History

###### Resolved Issues

- Fixed the properties of `History` to throw a SecurityError when not in a fully active Document.  (118750576)

##### Html

###### Resolved Issues

- Fixed “about:blank” `document.referrer` initialization.  (97689906)
- Fixed parsing a self-closing SVG script element. It now successfully executes.  (121887875)

##### Images

###### Deprecations

- Removed support for JPEG2000.  (35161822)

##### Javascript

###### New Features

- Added support for the `v` flag with `RegExp.prototype[Symbol.matchAll]`.  (126017731)
- Added support for Unicode 15.1.0 characters in RegExp.  (126863692)

###### Resolved Issues

- Fixed `RegExp.prototype.@@split` to update the following legacy RegExp static properties: `RegExp.input`, `RegExp.lastMatch`, `RegExp.lastParen`, `RegExp.leftContext`, `RegExp.rightContext`, and `RegExp.$1, ... RegExp.$9`.  (99865597)
- Fixed `String.prototype.replace` to not take the fast path if the pattern is RegExp Object and the `lastIndex` is not numeric.  (101122567)
- Fixed spec compliance for Async / Await, Generators, Async Functions, and Async Generators.  (113884730)
- Fixed async functions and generators to properly handle promises with throwing “constructor” getter.  (119734587)
- Fixed` return` in async generators to correctly `await` its value.  (119834751)
- Fixed `Symbol.species` getters to not share a single JS Function.  (120416817)
- Fixed throwing a `RangeError` if `Set` methods are called on an object with negative `size` property.  (121310940)
- Fixed `eval()` function from another realm to not cause a direct `eval` call.  (121546048)
- Fixed `eval()` call with `...spread` syntaxt to be a direct call.  (121547890)
- Fixed try/catch to not intercept errors originated in `[[Construct]]` of derived class.  (121959506)
- Fixed several issues: - direct `eval()` in a default value expression inside a rest parameter creates a variable in the environment of the function rather than the separate one of the parameters;
- a ReferenceError is thrown when accessing a binding, which is defined inside rest parameter, in `eval()`, or a closure created in a default value expression of a preceding parameter, but only if there is a `var` binding by the same name;
- a closure, created in the default value expression inside a rest parameter, is created in a different VariableEnvironment of the function than its counterparts in preceding parameters which causes the incorrect environment to be consulted when querying or modifying parameter names that are “shadowed” by `var` bindings.  (121961421)
- Fixed TypedArray sorting methods to have a special-case for camparator returning `false`.  (122093956)
- Fixed programming style for bitwise and in setExpectionPorts.  (122138733)
- Fixed `emitReturn()` to load `this` value from arrow function lexical environment prior to the TDZ check.  (122430056)
- Fixed NFKC normalization to work with Latin-1 characters.  (123328161)
- Fixed parsing of private names with Unicode start characters.  (123425805)
- Fixed `instanceof` to not get RHS prototype when LHS is primitive.  (123629166)
- Fixed bracket update expression to resolve property key at most once.  (123872374)
- Fixed bracket compound assignement to resolve the property key at most once.  (124420301)
- Fixed `Object.groupBy` and `Map.groupBy` to work for non-objects.  (125485685)
- Fixed `Array.fromAsync` to not call the Array constructor twice.  (125509304)
- Fixed inconsistent output of `Function.prototype.toString` for accessor properties.  (125739577)
- Fixed `Set#symmetricDifference` to call `this.has` in each iteration.  (126526845)
- Fixed logical assignment expressions to throw a syntax error when the left side of the assignment is a function call.  (126540636)
- Fixed throwing a syntax error for nested duplicate-named capturing groups in RegEx.  (126863735)
- Fixed `ArrayBuffer` and `SharedArrayBuffer` constructor to check length before creating an instance.  (126971134)
- Fixed Intl implementation to ensure canonicalizing “GMT” to “UTC” based on a spec update.  (127061600)
- Fixed RegEx lookbehinds differing from v8.  (127440248)
- Fixed `fractionalDigits` of `Intl.DurationFormat` to be treated as at most 9 digits if it is omitted.  (129145390)
- Fixed optimized TypedArrays giving incorrect results.  (129303210)
- Fixed `Intl.DurationFormat` for `numeric` and `2-digit`.  (130279541)

###### Deprecations

- Removed `[[VarNames]]` from the global object to reflect changes in the specification.  (130438575)

##### Loading

###### Resolved Issues

- Fixed `navigator.cookieEnabled` to return `false` when cookies are blocked.  (121284878)

##### Media

###### New Features

- Added support for WebRTC HEVC RFC 7789 RTP Payload Format.  (112001659)
- Added support for Viewer on macOS, a full window video watching mode for web pages with a prominent video element.  (114218891)
- Added support for MSE in workers.  (123052315)

###### Resolved Issues

- Fixed MediaSession to determine the best size artwork to use when the `sizes` metadata attribute is provided.  (81160539) (FB9409169)
- Fixed video sound coming from another window after changing tabs in the Tab Bar in visionOS.  (120018549)
- Fixed playback for MSE videos on some sites.  (123528095)
- Fixed allowing a video’s `currentTime` to be further than the gap’s start time.  (124186726)
- Fixed broken audio playback for a WebM file with a Vorbis track.  (124880261)
- Fixed `sampleRate` and `numberOfChannels` to be required and non-zero in a valid AudioEncoderConfig.  (125107934)
- Fixed media elements appending the same media segment twice.  (125386530)
- Fixed an issue where Safari audio may be emitted from the wrong window in visionOS.  (127009932)
- Fixedrejecting valid NPT strings if ‘hours’ is defined using 1 digit.  (128318772)
- Fixed picture-in-picture when hiding the `<video>` element while in Viewer.  (131786564)
- Fixed the return button not working after the video is paused and played in picture-in-picture.  (131791367)

###### Deprecations

- Removed non-standard `VTTRegion.track`.  (123172214)

##### Networking

###### Resolved Issues

- Fixed upgrading inactive or passive subresource requests and fetches in would-be mixed security contexts to match standards.  (101678657)
- Fixed incorrect `Sec-Fetch-Site` value for navigation of a nested document.  (109358563)
- Fixed loading WebArchives with a non-persistent datastore.  (122290562)
- Fixed `Timing-Allow-Origin` to not apply to an HTTP 302 response.  (126531139)

##### Pdf

###### Resolved Issues

- Fixed print buttons with a print action implementation.  (123850236)
- Fixed Open in Preview for a PDF with a space in its name.  (127379128)
- Fixed “Open with Preview” context menu item to work with locked PDF documents.  (132033502)

##### Rendering

###### Resolved Issues

- Fixed Greek uppercase transforms failing for some characters.  (90364897)
- Fixed resizing a `<textarea>` element with `1rem` padding.  (90639221)
- Fixed the color correctness of the color matrix filter.  (120795573)
- Fixed `backdrop-filter` to apply to the border area of an element with a `border-radius`.  (122295068)
- Fixed intrinsic inline size calculators to account for whitespace before an empty child with nonzero margins.  (122586712)
- Fixed overlapping elements with flex box when `height: 100%` is applied on nested content.  (125572851)
- Fixed incorrect grid item positioning with out-of-flow sibling.  (126207467)
- Fixed `break-word` with a float discarding text.  (126309547)
- Fixed `min-content` calculation for unstyled `only-child` inlines elements.  (128348427)
- Fixed ellipsis rendering multiple times when `position: relative` and `top` are used.  (128394449)
- Fixed a bug for inline elements inserted in reverse order after a block in a continuation.  (128826228)
- Fixed the flash of a page background-colored bar in the footer when the window is resized.  (128940179)
- Fixed garbled bold text caused by glyph lookup using the wrong font’s glyph IDs when multiple installed fonts have the same name.  (129891005) (FB13909556)
- Fixed selecting Japanese text annotated with `ruby` in a `vertical-rl` writing mode table.  (130974783)
- Fixed support for border, padding, and margin on `mfrac` and `mspace` elements in MathML.  (131119823)

##### Safari Extensions

###### New Features

- Added support for Safari Web Extensions and Content Blockers in web apps on macOS.  (99755515)
- Added support for Device Management of extension enabled state, private browsing state, and website access on Managed Devices.  (113051857)

##### Scrolling

###### Resolved Issues

- Fixed the cursor not updating as content scrolls under it on some pages.  (122347347)

##### Security

###### Resolved Issues

- Fixed stripping the scroll-to-text fragment from the URL to prevent exposing the fragment to the page.  (124717009)
- Fixed CORS bypass on private localhost domain using 0.0.0.0 host and mode “no-cors”.  (125913679)
- Fixed blocking cross-origin redirect downloads in an iframe.  (130901951)
- Fixed blocked cross-origin redirect downloads to attempt rendering the page instead.  (131962658)

##### Spatial Web

###### New Features

- Added support for docking fullscreen videos into the current Environment in visionOS.  (91364019)
- Added support for interaction regions in SVGs that have a `cursor: pointer` set.  (117642184) (FB13310281)
- Added interaction region support for CSS `clip-path`.  (119124300)
- Added support for Spatial and Panoramic images.  (125913434)

##### Storage

###### Deprecations

- Removed support for AppCache.  (113343269)

##### Svg

###### Resolved Issues

- Fixed the SVG parser to interpret “form feed” as white space.  (95488677)
- Fixed error handling for invalid filter primitive references.  (104262208)
- Fixed displaying an SVG element inside a `<switch>` element.  (120732837)
- Fixed SVG title to have `display: none` as the default UA style rule.  (122185838)
- Fixed the UA stylesheet for links in SVGs to apply `cursor: pointer` matching standards.  (122715957)
- Fixed returning the initial value for the SVG gradient `stop-color` if it is not rendered in the page.  (123262508)
- Fixed the SVG marker segment calculations if the marker path consists of sub-paths.  (123434203)
- Fixed `SVGLength` to sync with the WebIDL specification.  (129169603)

###### Deprecations

- Removed non-standard `getTransformToElement` from SVGGraphicsElement  (122435702)
- Removed the `SVGAnimateColorElement` interface.  (122586568)

##### Text

###### Resolved Issues

- Fixed disclosure counter styles to consider `writing-mode`.  (130468537)

##### Web Animations

###### Resolved Issues

- Fixed percentage transform animations when `width` and `height` are animated.  (63309680)
- Fixed updating an animation when changing the value of a `transform` property while that property is animated with an implicit keyframe.  (126126617)
- Fixed `display` transition to `none`.  (130857338)

##### Web Api

###### New Features

- Added support for `URL.parse()`.  (125376520)
- Added support for `shadowRootDelegatesFocus` and `shadowRootClonable` to `<template>`.  (125401993)
- Added support for serializing shadow roots through `getHTML()` as well as the corresponding shadow root `serializable` feature.  (125513986)
- Added support for PopStateEvent’s `hasUAVisualTransition`.  (125849073)
- Added support for subresource integrity in imported module scripts.  (127038535)
- Added support for feature detecting text fragments by exposing `document.fragmentDirective`.  (127650843)
- Added support for the `bytes()` method to Request and Response.  (128407577)
- Added support for `bytes()` to Blob and PushMessageData.  (128418858)

###### Resolved Issues

- Fixed `cssText `setter to change the `style` attribute when the serialization differs.  (29861252) (FB5535475)
- Fixed `history.pushState()` and `history.replaceState()` to ignore the `title` argument.  (75695791)
- Fixed URL text fragment directives not fully stripped from JavaScript.  (107326333)
- Fixed `showPicker()` method to trigger suggestions from a `datalist`.  (116017782)
- Fixed `lang` attribute in no namespace to only apply to HTML and SVG elements.  (117795695)
- Fixed unnecessarily unsetting the iframe fullscreen flag.  (120052751)
- Fixed DOM Range to correctly account for CDATASection nodes.  (122608224)
- Fixed `getGamepads()` to no longer trigger an insecure contexts warning.  (123039555)
- Fixed inserting a `<picture>` element displaying the same image twice.  (123795045)
- Fixed throwing exceptions in navigation methods if in a detached state.  (123898636)
- Fixed a minor issue in URL’s host setter.  (124363495)
- Fixed cloning of ShadowRoot nodes following a DOM Standard clarification.  (125917138)
- Fixed GeolocationCoordinates to expose a `toJSON()` method.  (126183686)
- Fixed IntersectionObserver notifications that sometimes fail to fire.  (126238865)
- Fixed GeolocationPosition to expose a `toJSON()` method.  (126247408)
- Fixed setting `CustomEvent.target` when dispatching an event.  (126369768)
- Fixed `navigator.language` only returning the system language in iOS 17.4.  (126765790)
- Fixed: Removed presentational hints from the `width` attribute for `<hr>`.  (128647444)
- Fixed an issue when inserting writing suggestions into an editable `display: grid` container.  (129366300)
- Fixed the warning message for `window.styleMedia`.  (131005713)

###### Deprecations

- Removed support for `KeyboardEvent.altGraphKey`.  (102980723)
- Removed AES-CFB support from WebCrypto.  (120000331)
- Removed the non-standard `KeyboardEvent.keyLocation`.  (121564228)
- Removed `HashChangeEvent`’s non-standard `initHashChangeEvent()` method.  (124736521)

##### Web Apps

###### New Features

- Added support for opening links directly in web apps on macOS.  (113034778)

###### Resolved Issues

- Fixed resolving `www.` sub-domain for Associated Domains for all web apps.  (121216556)

##### Web Assembly

###### Resolved Issues

- Fixed initialization of portable reference typed globals.  (119397603)

##### Web Extensions

###### Resolved Issues

- Fixed getting an empty key from storage.  (99440265) (FB11427769)
- Fixed Service Workers not appearing in the Develop menu or remote Web Inspector menu.  (130712941)
- Fixed web extensions unable to start due to an issue parsing declarativeNetRequest rules.  (130861213) (FB14145801)

##### Web Inspector

###### New Features

- Added support for fuzzy search code completion in the CSS source editor.  (125030691)

###### Resolved Issues

- Fixed font sizes in the Audits tab.  (76162927)
- Fixed expanded sections of Storage to not collapse.  (107687975)
- Fixed Web Inspector to show nested workers.  (108322385)
- Fixed CSS font property values marked `!important` not getting overridden when using the interactive editing controls.  (112080113)
- Fixed an issue where the Web Inspector viewport might appear cut off.  (117272735)
- Fixed runtimes to be aligned in the Audit tab.  (121810292)
- Fixed remembering the message type selection in the Console tab.  (122924275)
- Fixed autocomplete for the `text-indent` property suggesting prefixed properties instead of `each-line` or `hanging`.  (123240715)
- Fixed `background` autocompletion suggestion to include `repeating-conic-gradient`.  (123428709)
- Fixed the list of breakpoints in the Sources tab disappearing when Web Inspector is reloaded.  (123641994)
- Fixed console clearing unexpectedly when Web Inspector reopens.  (124171190)
- Fixed console code completion to be case-insensitive.  (124544458)
- Fixed `overflow: scroll` elements to scroll as expected when highlighting an element from the DOM tree.  (124554999)
- Fixed showing additional Safari tabs from an iOS device in the Develop menu.  (124876362)
- Fixed Console and code editor completion not auto-scrolling the suggestion into view.  (124979790)
- Fixed search in the DOM tree view unexpectedly chaning the text display.  (125797803)
- Fixed clicking the “goto” arrow for computed CSS when “show independent Styles sidebar” is disabled.  (127025520)
- Fixed inspectable tabs from Safari in the visionOS Simulator don’t appear in Developer menu on the host macOS.  (127259433)
- Fixed Accessibility inspector for switch controls to report “State: on/off” instead of “Checked: true/false”.  (128952449)

##### Web Views

###### New Features

- Added WKWebView API support for Text Assistant.  (126585826)
- Added WKWebView API to control adaptive image glyph insertion.  (126585881)

###### Resolved Issues

- Fixed Gamepad API in WKWebView.  (123310472)
- Fixed repainting HTML elements when their width or height change in legacy WebView.  (124564409)

##### Webdriver

###### Resolved Issues

- Fixed retrieving titles containing multibyte characters.  (123987149)

##### Webgl

###### New Features

- Enabled support for the following approved extensions: - `EXT_texture_mirror_clamp_to_edge`
- `WEBGL_render_shared_exponent`
- `WEBGL_stencil_texturing`
- `EXT_render_snorm`
- `OES_sample_variables`
- `OES_shader_multisample_interpolation` (121835897)  (126863775)

##### Webrtc

###### New Features

- Added support for MediaStreamTrack processing in a dedicated worker.  (114213842)
- Added support for additional WebRTC stats.  (121594743)

###### Resolved Issues

- Fixed RTCEncodedVideoFrame and RTCEncodedAudioFrame to match the WebIDL specification.  (118607685)
- Fixed VideoTrackGenerator writer to close when its generator track (and all its clones) are stopped.  (121835553)
- Fixed WebRTC AV1 HW decoding on iPhone 15 Pro.  (123449229)
- Fixed black stripes with screen sharing windows.  (123492622)
- Fixed black stripes with getDisplayMedia captured windows when the window is resized.  (124131045)

##### Webview

###### Deprecations

- Deprecated some legacy WebKit notification names including: - `WebViewDidBeginEditingNotification`
- `WebViewDidChangeNotification`
- `WebViewDidEndEditingNotification`
- `WebViewDidChangeTypingStyleNotification`
- `WebViewDidChangeSelectionNotification`  (130033164)

##### Webxr

###### New Features

- Added support for immersive WebXR in visionOS.  (125631316)

## See Also

- [Safari 18.6 Release Notes](safari-18_6-release-notes.md)
  Released July 29, 2025 — 18.6 (20621.3.11)
- [Safari 18.5 Release Notes](safari-18_5-release-notes.md)
  Released May 12, 2025 — 18.5 (20621.2.5)
- [Safari 18.4 Release Notes](safari-18_4-release-notes.md)
  Released March 31, 2025 — 18.4 (20621.1.15)
- [Safari 18.3 Release Notes](safari-18_3-release-notes.md)
  Released January 27, 2025 — 18.3 (20620.2.4)
- [Safari 18.2 Release Notes](safari-18_2-release-notes.md)
  Released December 11, 2024 — 18.2 (20620.1.16)
- [Safari 18.1 Release Notes](safari-18_1-release-notes.md)
  Released October 28, 2024 — 18.1 (20619.2.8)
- [Safari 18.0.1 Release Notes](safari-18_0_1-release-notes.md)
  Released October 3, 2024 — 18.0.1 (20619.1.26.30)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-18-release-notes)*