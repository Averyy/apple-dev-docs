# Safari 18.2 Release Notes

**Framework**: Safari Release Notes

Released December 11, 2024 — 18.2 (20620.1.16)

#### Overview

Safari 18.2 is available for iOS 18.2, iPadOS 18.2, visionOS 2.2, macOS 15.2, macOS Sonoma, and macOS Ventura.

##### Accessibility

###### Resolved Issues

- Fixed `text-transform: full-size-kana` to not affect speech output.  (115504070)
- Fixed element reflection attributes to be able to retrieve a disconnected element.  (133693674)
- Fixed VoiceOver focus to activate PDF form fields when it lands on them.  (134522935)
- Fixed tree updates becoming broken when children change for a dynamically ignored element and its unignored ancestor is in the same tree update cycle.  (137876593)
- Fixed handling dynamically-created and nested `aria-modal` dialogs.  (137883473)
- Fixed the accessibility tree to update when a text selection is cleared.  (137960839)

##### Browser

###### New Features

- Added contextual menu support for generating text fragment links.  (131712706)

###### Resolved Issues

- Fixed windows not getting restored after updating macOS.  (138413468)

##### Canvas

###### Resolved Issues

- Fixed CanvasRenderingContext2D `globalAlpha` property getting ignored for some values of `globalCompositeOperation`.  (134840885)

##### Css

###### New Features

- Added support for cross-document View Transitions.  (133994557)
- Added support for View Transition Classes.  (129849286)
- Added support for View Transition Types.  (132051697)
- Added support for `view-transition-name: auto`.  (137788958)
- Added support for `ruby-align`.  (133656625)
- Added support for `ruby-overhang`.  (135058411)
- Added support for unprefixed `ruby-position`.  (86128259)
- Added support for `text-box-edge`.  (133834296)
- Added support for `text-box-trim`.  (133947582)
- Added support for the `text-box` shorthand.  (133942602)
- Added support for `text-underline-position: left` and  `text-underline-position: right`.  (130621143)
- Added support for `background-clip: border-area`.  (133788384)
- Added support for `scrollbar-gutter`.  (111918434)
- Added support for `scrollbar-width`.  (133019206)
- Added support for `@page` margin descriptors.  (118773100)
- Added support for `jis-b4` and `jis-b5` sizes for `@page`.  (133138325)
- Added support for `:is(:host)`.  (118582384)
- Added support for `closest-corner` and `farthest-corner` in circle and ellipse shapes.  (132936677)
- Added support for `@property` `<string>` syntax.   (133250776)
- Added support for `::target-text`.  (134010063)
- Updated `calc()` to the most recent web standard, including support for dividing by numbers with additional units.  (134446246)

###### Resolved Issues

- Fixed backgrounds applied to a table row repeating in every table cell.  (11446455)
- Fixed the `size` property of `@page` to parse as a descriptor, not a global CSS property.  (92963022)
- Fixed `background-clip: text` to correctly paint text decorations.  (93823895)
- Fixed `font-variant: small-caps normal;` to be invalid syntax.  (102679841)
- Fixed `-webkit-line-clamp: none` to be parsable.  (103158259)
- Fixed `text-underline-offset` to support percentages.  (117246233)
- Fixed `text-decoration-thickness` to work in buttons.  (118320835)
- Fixed the `lh` unit sometimes getting computed before `line-height` is resolved.  (118983248)
- Fixed `touch-action` to use `pan-x pan-y` order when serializing.  (125349558)
- Fixed serialization of `place-content`, `place-items`, and `place-self` properties.  (125415088)
- Fixed: Updated CSS Nesting to remove the hoisting behavior.  (130094168)
- Fixed: Improved scrollbar styling support for interoperability.  (131515907)
- Fixed contrast between `ButtonFace` and `ButtonText` system colors in dark mode.  (131996608)
- Fixed: Disallow matching of `:has()` in CSS Nesting.  (132102543)
- Fixed defaults for text underline position and text emphasis marks in CJK languages.  (132444497)
- Fixed attribute `initial-value` makes the `@property` rule invalid for `[var(--x)]`.  (134317319)
- Fixed invalidating attribute values when programmatically mutated so that page attribute selectors work as expected.  (137228504)
- Fixed CSS Nested declarations inside a `@scope` to behave like `:where(:scope)`.  (137307934)

##### Editing

###### Resolved Issues

- Fixed aligning with the standardized version of the `autocorrect` attribute, which does not support Email, URL, and Password fields and does not treat the empty string value in a special way.  (101036922)

##### Forms

###### New Features

- Added support for `input type=week` on iOS, iPadOS, and visionOS.  (10854201)

###### Resolved Issues

- Fixed `HTMLSelectElement.prototype.add` with `optgroup` elements.  (120553757)

##### History

###### Resolved Issues

- Fixed using Cross-Origin-Opener-Policy HTTP header disabling the back-forward cache.  (128678196)

##### Javascript

###### New Features

- Implemented Float16Array.  (109883982)
- Added support for `Uint8Array.prototype.toBase64` and `Uint8Array.prototype.toHex`.  (129045737)
- Added support for `Uint8Array.fromBase64` and `Uint8Array.prototype.setFromBase64`.  (131509586)
- Added support for `firstDayOfWeek` for `Intl.Locale` info API.  (132731533)
- Added support for `Promise.try` and `RegExp.escape`.  (132952304)
- Enabled Base64 and Hex features.  (133312461)
- Added support for type reflection for `WebAssembly.Module.imports` and `WebAssembly.Module.exports`.  (133429946)
- Added support for `Iterator.prototype.constructor` and  `Iterator.prototype[@@toStringTag]`.  (134598491)
- Added support for `Iterator.from` from Iterator Helpers Proposal.  (135065388)

###### Resolved Issues

- Fixed class field initializers to disallow `yield` and `await` expressions.  (119044881)
- Fixed DestructuringAssignmentTarget to be evaluated prior to calling `[[Get]]` or a stepping iterator.  (121960976)
- Fixed throwing an exception for negative exponent in BigInt in the JIT compiler.  (131051084)
- Fixed RegExp range quantifier to allow 2^53 - 1.  (131710011)
- Fixed `Uint8Array#setFromBase64` to decode and write chunks which occur prior to bad data.  (132198988)
- Fixed: Disallow `yield` and `await` expressions in class field initializers.  (132338331)
- Fixed TimeZone without Time to be rejected in ISO8601 strings.  (133988956)
- Fixed `Object.keys(global)` including non-enumerable properties unless deleted first.  (134121649)
- Fixed duration format’s nanoseconds calculation ordering.  (134526619)
- Fixed TimeZoneAnnotation to disallow sub-minute.  (134541964)
- Fixed: Improved the TypeError message when a WeakMap constructor takes an iterable that yields invalid entry.  (135333331)
- Fixed incorrect SyntaxError when destructuring `let`.  (135353378)

##### Loading

###### Resolved Issues

- Fixed `javascript:` URL navigation to another browsing context created from `window.open` not checking the source’s Content Security Policy.  (137941234)

##### Media

###### New Features

- Added support for viewing Spatial Photos in Safari in visionOS.  (130545126)
- Added a fallback image to Now Playing when a website doesn’t specify one in MediaSession metadata.  (131185836)
- Added support for allowing websites to override the system-default accessibility caption styling.  (134265139)
- Added support for Spatial Video in Safari in visionOS.  (138482091)

###### Resolved Issues

- Fixed fullscreen error handling to include error messages.  (103073510)
- Fixed `audioTrack.configuration()` values for WebM files.  (133545263)

##### Networking

###### New Features

- Added support for Document render-blocking with `<link rel=expect>`.  (122797243)
- Added support for `NavigationActivation.finished` handling.  (133220864)

##### Pdf

###### Resolved Issues

- Fixed a hang that could occur using the Select All keyboard shortcut ⌘A (Command-A) on a PDF causing all pages to be blank.  (125375518)

##### Rendering

###### New Features

- Added support for `blocking=render` attribute for `<script>` and `<style>`.  (121008856)

###### Resolved Issues

- Fixed non-separable blend modes in `mix-blend-mode` to workon elements in compositing layers.  (49387130)
- Fixed MathML to layout invalid markup as an `<mrow>`.  (99335890)
- Fixed: Improved grid track sizing by adding support for wrapped column flex containers, multi-column containers, and items with aspect ratios that depend on row size.  (113984672)
- Fixed margins used for grid items on relayout.  (113984882)
- Fixed grid areas to be considered in layout overflow.  (113985286)
- Fixed grid area overflow to include inline end and block end padding.  (113985683)
- Fixed items that span multiple tracks with optimizations.  (132435056)
- Fixed rendering image content with percentage height in a container with `height: auto`.  (132438040)
- Fixed an extra wrap when a table with mixed `white-space` values applied to the table and table content.  (132633448)
- Fixed repeating `background-image` sized to the `content-box` failing to fill the viewport in an iframe.  (133952319)
- Fixed rendering tick marks of the range input type when the page zoom is less than 1.  (134282707)

##### Security

###### New Features

- Added a warning when connecting to a website over an insecure connection.  (99348736)
- Added support for automatic fallback to HTTP if an HTTPS connection or request fails.  (114286729)
- Changed to prefer HTTPS navigations by default.  (133799554)

###### Resolved Issues

- Fixed an empty origin in the location permission prompt for a `blob://` resource.  (134369448)

##### Svg

###### Resolved Issues

- Fixed correctly applying `clip-path` to the SVG element.  (80516912)
- Fixed zooming in or out of an SVG with `transform-origin`.  (96318505)
- Fixed an issue for `getPointAtLength` to throw an exception when `path` is empty.  (122574451)
- Fixed `fill` to not be considered a presentation attribute on animation elements.  (128896937)
- Fixed script elements in XHTML documents to work when trusted types are enforced.  (128935225)

###### Deprecations

- Removed non-standard `hasExtension`.  (123734641)

##### Web Animations

###### Resolved Issues

- Fixed `alignment-baseline` and `buffered-rendering` to support discrete animation.  (94613679)
- Fixed `hanging-punctuation` to support discrete animation.  (94614108)
- Fixed `scroll-snap-` properties to support discrete animation.  (94614257)
- Fixed `column-span` to support discrete animation.  (96082973)
- Fixed `appearance` to support discrete animation.  (96082999)
- Fixed `hyphenate-character` to support discrete animation.  (132698836)
- Fixed `font-optical-sizing` to support discrete animation.  (132699150)
- Fixed `image-rendering` to support discrete animation.  (132707652)
- Fixed: Improved animation support for shorthands.  (132752305)
- Fixed the `mask-border-*` properties to be animatable.  (132783274)
- Fixed `stroke-color` to be animatable.  (132784589)
- Fixed transform animations that jump back and forth instead of animating continuously.  (135743482)

##### Web Api

###### New Features

- Added `auxclick` event support to `PointerEvent`.  (25988904)
- Updated `click`, `contextmenu`,  and `click()` to use PointerEvent, providing the `pointerType` property to these events.  (71202646)
- Implemented new dialog initial focus algorithm to match specification changes.  (104667732)
- Added support for the `getPredictedEvents` API to `PointerEvent`.  (117767174)
- Added support for `altitudeAngle` and `azimuthAngle` to `PointerEvent`.  (131974392)
- Added support for the `getCoalescedEvents` API to `PointerEvent`.  (132210576)
- Added support for the `pageswap` and `pagereveal` events for View Transitions.  (133025306)

###### Resolved Issues

- Fixed: Aligned `oncuechange` event handler handling with other event handlers.  (98254058)
- Fixed the Pointer Lock API to work when Fullscreen API is enabled.  (125924062)
- Fixed `popovertarget` to work on buttons in a form.  (131042177)
- Fixed pointer events generated from platform mouse events to use the platform event’s timestamp.  (132051812)
- Fixed popover tab navigation.  (132129060)
- Fixed the directionality of non-HTML elements.  (132210868)
- Fixed setting `.value =` to update `dir=auto` inputs.  (132214207)
- Fixed two `mousemove` events dispatched when the mouse enters a web view window instead of a single one.  (132251320)
- Fixed Pointer Events created for pointer capture to be trusted and composed.  (133259027)
- Fixed `XMLSerializer.serializeToString()` not serializing the children of `<img>` and also not closing the `<img>` if it has children.  (133404338)
- Fixed the directionality of shadow trees.  (133549820)
- Fixed text highlights when selecting large text that ends with a common phrase.  (133786985)
- Fixed copying a link to a common term in an article resulting in an incorrect part of the page being highlighted.  (134882107)
- Fixed: Moved `onbeforeinput` to `GlobalEventHandlers`.  (134943272)
- Fixed `scrollIntoView(...)` for SVG elements.  (135265918)
- Fixed non-modal popover dialog blocking interaction on the content behind it.  (137879216)
- Fixed `pushManager.subscribe` returning an empty endpoint.  (138489579)
- Fixed checking against the “active document” of the pointer when setting the pointer capture.  (139216227)

###### Deprecations

- Removed support for the non-standard “overflow” event.  (71129110)

##### Web Apps

###### Resolved Issues

- Fixed Web Application Manifest parsing to trim all ASCII whitespace.  (134336817)

##### Web Assembly

###### New Features

- Added support for Wasm garbage collection.  (126103011)
- Added support for Wasm Tail Calls.  (131410516)

##### Web Inspector

###### New Features

- Added support for blackboxing ranges within a file.  (130387125)
- Added support for sourcemaps to be blackboxed.  (133731737)
- Added support for showing `boundThis` for arrow functions in the console.  (134268331)

###### Resolved Issues

- Fixed parising attributes added when editing the tag name.  (131607290)
- Fixed an issue where multi-line content in the Console prompt was not scrollable.  (131756916)

##### Webdriver

###### New Features

- Added support for using a persistent website data store.  (132757844)

###### Resolved Issues

- Fixed an issue where all script evaluation was unconditionally performed with user activation.  (111970701)
- Fixed WebDriver sometimes taking screenshots with a transparent grey line at the top and no rounded corners.  (116020785)
- Fixed WebDriver to use pointer origin rather than viewport origin for state location resolution.  (128668986)
- Fixed chorded mouse interactions by ensuring input dispatch logic correctly interprets successive `mousepress` or `mouserelease` actions with different `button` values.  (128669517)

##### Webxr

###### New Features

- Added support to re-project WebXR content converting depth from forward-Z to reverse-Z.  (125862366)
- Added support for `XRSession.enabledFeatures`.  (132890511)

###### Resolved Issues

- Fixed audio not audible during an immersive session in visionOS.  (132038279)

##### Wkwebview

###### New Features

- Added support for Genmoji on iOS and iPadOS. WKWebView also includes support for the `NSAdaptiveImageGlyph` API.  (116789598)
- Added support for `WKDownload.originatingFrame` and `WKDownload.userInitiated` API.  (120389237)
- Added support for `WKWebpagePreferences.UpgradeToHTTPSPolicy` in  WKWebView.  (138349588)

###### Resolved Issues

- Fixed `-[WKWebViewConfiguration writingToolsBehavior]` not available when using a deployment target lower than iOS 18.  (136830527) (FB15297419)
- Fixed apps crashing intermittently crashing at launch.  (137595340)
- Fixed text editing corruption after `[NSInputAnalytics didInsertText:]` is called without a session beginning.  (137901213)

## See Also

- [Safari 18.6 Release Notes](safari-18_6-release-notes.md)
  Released July 29, 2025 — 18.6 (20621.3.11)
- [Safari 18.5 Release Notes](safari-18_5-release-notes.md)
  Released May 12, 2025 — 18.5 (20621.2.5)
- [Safari 18.4 Release Notes](safari-18_4-release-notes.md)
  Released March 31, 2025 — 18.4 (20621.1.15)
- [Safari 18.3 Release Notes](safari-18_3-release-notes.md)
  Released January 27, 2025 — 18.3 (20620.2.4)
- [Safari 18.1 Release Notes](safari-18_1-release-notes.md)
  Released October 28, 2024 — 18.1 (20619.2.8)
- [Safari 18.0.1 Release Notes](safari-18_0_1-release-notes.md)
  Released October 3, 2024 — 18.0.1 (20619.1.26.30)
- [Safari 18.0 Release Notes](safari-18-release-notes.md)
  Released September 16, 2024 — 18.0 (20619.1.26)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-18_2-release-notes)*