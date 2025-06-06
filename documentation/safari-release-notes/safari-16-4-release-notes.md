# Safari 16.4 Release Notes

**Framework**: Safari Release Notes

Released March 27, 2023 — Version 16.4 (18615.1.26)

#### Overview

Safari 16.4 beta is available for macOS Big Sur, macOS Monterey, macOS Ventura, iPadOS 16.4 beta, and iOS 16.4 beta.

##### Browser Changes

###### New Features

- Added dark mode support for plain text files.
- Added fingerprinting countermeasures for querying the permission state of the Notifications API.

##### Css

###### New Features

- Added support for `currentColor` with `color-mix()`.
- Added support for `margin-trim`.
- Added support for `outline` following the curve of `border-radius`.
- Added support for CSS Properties and Values API with support for `@property`.
- Added support for CSS relative color syntax.
- Added support for new named colors to match CSS Color Level 4.
- Added support for the `:dir()` pseudo-class.
- Added support for the `:modal` pseudo-class to match fullscreen elements.
- Added support for the `lh` and `rlh` units.
- Added support for the range syntax and boolean logic from Media Queries level 4.
- Added support for the unprefixed `:fullscreen` pseudo-class.
- Added support for the unprefixed absolute size keyword `xxx-large`.

###### Resolved Issues

- Fixed `-webkit-mask-box-image: initial` to set the correct initial value.
- Fixed `-webkit-radial-gradient` parsing accidentally treating several mandatory commas as optional.
- Fixed `::placeholder` to not support `writing-mode`, `direction`, or `text-orientation`.
- Fixed `:has()` pseudo-class invalidation for `:lang`, `:playing`, `:paused`, `:seeking`, `:muted`, `:volume-locked`, `:picture-in-picture`, `:buffering`, and `:stalled` pseudo-classes.
- Fixed `@supports` to not work if `not`, `or`, or `and` isn’t followed by a space.
- Fixed `background-repeat` not getting correctly exposed through inline styles.
- Fixed `baseline-shift` to allow length or percentage, but not numbers.
- Fixed `contain: inline-size` for replaced elements.
- Fixed `CSSPerspective.toMatrix()` to throw a TypeError if its length is incompatible with the `px` unit.
- Fixed `cx`, `cy`, `x`, and `y` CSS properties to allow length or percentage, but not numbers.
- Fixed `filter: blur` on an absolutely positioned image losing `overflow: hidden`.
- Fixed `font-face` to accept ranges in reverse order, and reverse them for computed styles.
- Fixed `font-style: oblique` must allow angles equal to 90deg or -90deg.
- Fixed `font-style: oblique` with `calc()` to allow out-of-range angles and clamp them for computed style.
- Fixed `font-weight` to clamp to 1 as a minimum.
- Fixed `font` shorthand to reject out-of-range angles for `font-style`.
- Fixed `font` shorthand to reset more longhand properties.
- Fixed `overflow-x: clip` causing a sibling image to not load.
- Fixed `overflow: clip` not working on SVG elements.
- Fixed `stroke-dasharray` parsing to align with standards.
- Fixed `stroke-width` and `stroke-dashoffset` parsing to align with standards.
- Fixed `text-decoration-thickness` property not repainting when changed.
- Fixed allowing `calc()` that combines percentages and lengths for `line-height`.
- Fixed an issue where using `box-sizing: border-box` causes the calculated aspect-ratio to create negative content sizes.
- Fixed an issue with a monospace font on a parent causing children with a sans-serif font using `rem` or `rlh` units to grow to a larger size.
- Fixed behavior of `cursor: auto` over links.
- Fixed buttons with auto width and height to not set intrinsic margins.
- Fixed calculating block size to use the correct box-sizing with aspect ratio.
- Fixed cells overflowing their contents when a table cell has inline children which change `writing-mode`.
- Fixed clipping `perspective` `calc()` values to 0.
- Fixed font shorthand to not reject values that happen to have CSS-wide keywords as non-first identifiers in a font family name.
- Fixed hit testing for double-click selection on overflowing inline content.
- Fixed honoring the content block size minimum for a `<fieldset>` element with `aspect-ratio` applied.
- Fixed incorrectly positioned line break in contenteditable with tabs.
- Fixed invalidation for class names within `:nth-child()` selector lists.
- Fixed omitting the `normal` value for `line-height` from the `font` shorthand in the specified style, not just the computed style.
- Fixed pseudo-elements to not be treated as ASCII case-insensitive.
- Fixed rejecting a selector argument for `:nth-of-type` or `:nth-last-of-type`.
- Fixed serialization order for `contain`.
- Fixed strings not wrapped at zero width spaces when `word-break: keep-all` is set.
- Fixed supporting `<string>` as an unprefixed keyframe name.
- Fixed the `:has()` pseudo-selector parsing to be unforgiving.
- Fixed the `font-face` `src` descriptor format to allow only specified formats, others are a parse error.
- Fixed the `tz` component not accounting for zoom when creating a `matrix3d`() value.
- Fixed the computed value for `stroke-dasharray` to be in `px`.
- Fixed the effect of the writing-mode property not getting removed when the property is removed from the root element.
- Fixed the position of `text-shadow` used with `text-combine-upright`.
- Fixed the title of a style element with an invalid type to never be added to preferred stylesheet set.
- Fixed the transferred min/max sizes to be constrained by defined sizes for aspect ratio.
- Fixed the user-agent stylesheet to align hidden elements, `abbr`,  `acronym`,  `marquee`, and `fieldset` with HTML specifications.
- Fixed to always use percentages for computed values of `font-stretch`, never keywords.
- Fixed to not require whitespace between `of` and the selector list in `:nth-child` or `:nth-last-child`.

##### Css Api

###### New Features

- Added support for CSS Typed OM.
- Added support for constructible and adoptable CSSStyleSheet objects.
- Added support for input validation for `CSSColorValues` as part of CSS Typed OM.

###### Resolved Issues

- Fixed `CSS.supports` returning false for custom properties.
- Fixed `CSS.supports` whitespace handling with `!important`.
- Fixed forgiving selectors to not be reported as supported with `CSS.supports("selector(...)")`.
- Fixed `getComputedStyle()` to return a function list for the transform property.
- Fixed `linear-gradient` keyword values not getting converted to their `rgb()` equivalents for `getComputedStyle()`.

##### Content Security Policy

###### Resolved Issues

- Fixed updating the Content Security Policy when a new header is sent as part of a 304 response.

##### Custom Elements

###### New Features

- Added support for Declarative Shadow DOM.
- Added support for ElementInternals.
- Added support for form-associated custom elements.
- Added support for Imperative Slot API.

##### Forms

###### New Features

- Added a thumbnail of the selected file for `<input type="file">` on macOS.
- Added support for the `cancel` event on `<input type="file">`.

###### Resolved Issues

- Fixed `<input type="submit">`, `<input type="reset">,` and `<input type="button">` to honor `font-size`, `padding`, `height`, and work with multi-line values.
- Fixed firing the `change` event for `<input type="file">` when a different file with the same name is selected.
- Fixed preventing a disabled `<fieldset>` element from getting focus.
- Fixed the `:out-of-range` pseudo class matching for empty `input[type=number]`.

##### Javascript

###### New Features

- Added support for RegExp lookbehind assertions.
- Added support for `Array.fromAsync`.
- Added support for `Array#group` and `Array#groupToMap`.
- Added support for `Atomics.waitAsync` .
- Added support for `import.meta.resolve()`.
- Added support for `Intl.DurationFormat`.
- Added support for `String#isWellFormed` and `String#toWellFormed`.
- Added support for class static initialization blocks.
- Added support for growable SharedArrayBuffer.
- Added support for Import Maps.
- Added support for resizable ArrayBuffer.
- Added support for using `Symbols` in `WeakMap` and `WeakSet`.

###### Resolved Issues

- Fixed `Array.prototype.indexOf` constant-folding to account for a non-numeric index.
- Fixed `Intl.NumberFormat` `useGrouping` handling to match updated specs.
- Fixed `Intl.NumberFormat` ignoring `maximumFractionDigits` with compact notation.
- Fixed `String.prototype.includes` incorrectly returning false when the string is empty and the position is past end of the string.
- Fixed `toLocaleLowerCase` and `toLocaleUpperCase` to throw an exception on an empty string.

##### Html

###### New Features

- Added support for lazy loading iframes.

###### Resolved Issues

- Fixed aligning the parsing of `<body link vlink alink>` to follow standards.
- Fixed `<legend>` to accept more `display` property values than `display: block`.

##### Intelligent Tracking Prevention

###### Resolved Issues

- Fixed user initiated cross-domain link navigations getting counted as Top Frame Redirects.

##### Images

###### New Features

- Added support for AVIF on macOS Monterey and macOS Big Sur.

###### Resolved Issues

- Fixed ensuring the `<picture>` element works with AVIF.
- Fixed some display issues with HDR AVIF images.
- Fixed the accept header to correctly indicate AVIF support.

##### Loading

###### New Features

- Added prevention of redirects to `data:` or `about:` URLs.

##### Lockdown Mode

###### New Restrictions

- Disabled binary fonts in the CSS Font Loading API.
- Disabled Cache API.
- Disabled CacheStorage API.
- Disabled ServiceWorkers.
- Disabled SVG fonts.
- Disabled the WebLocks API.
- Disabled WebSpeech API.
- Fixed common cases of missing glyphs due to custom icon fonts.

##### Media

###### New Features

- Added improvements to audio quality for web video conferencing.
- Added support for a subset of the AudioSession Web API.
- Added support for AVCapture virtual cameras.
- Added support for inbound rtp `trackIdentifier` stat field.
- Added support for VTT-based extended audio descriptions.
- Added support to allow a site to provide an “alternate” URL to be used during AirPlay.
- Added video-only support for Web Codecs.

###### Resolved Issues

- Fixed `enumerateDevices` may return filtered devices even if page is capturing.
- Fixed `MediaRecorder.stop()` firing an additional `dataavailable` event with bytes after `MediaRecorder.pause()`.
- Fixed duplicate `timeupdate` events.
- Fixed limiting DOMAudioSession to third-party iframes with microphone access.
- Fixed MSE to not seek with no seekable range.
- Fixed mute microphone capture if capture fails to start because microphone is used by a high priority application.
- Fixed not allowing text selection to start on an HTMLMediaElement.
- Fixed only requiring a transient user activation for Web Audio rendering.
- Fixed screen capture to fail gracefully if the window or screen selection takes too long.
- Fixed switching to alternate `<source>` element for AirPlay when necessary.
- Fixed the local WebRTC video element pausing after bluetooth `audioinput` is disconnected.
- Fixed trying to use low latency for WebRTC HEVC encoder when available.
- Fixed unmuting a TikTok video pauses it.
- Fixed WebVTT styles not applied with in-band tracks.

##### Rendering

###### Resolved Issues

- Ensured negative letter-spacing does not pull content oustisde of the inline box
- Fixed `<div>` with `border-radius` not painted correctly while using jQuery’s `.slideToggle()`.
- Fixed `border-radius` clipping on composited layers.
- Fixed `box-shadow` to paint correctly on inline elements.
- Fixed box-shadow invalidation on inline boxes.
- Fixed calculating the width of an inline text box using simplified measuring to handle fonts with `Zero Width Joiner`, `Zero Width Non-Joner`, or `Zero Width No-Break Space`.
- Fixed clearing floats added dynamically to previous siblings.
- Fixed clipping the source image when the source rectangle is outside of the source image in canvas.
- Fixed CSS keyframes names to not allow CSS wide keywords.
- Fixed elements with negative margins not avoiding floats when appropriate.
- Fixed floating boxes overlapping with their margin boxes.
- Fixed HTMLImageElement width and height to update layout to return styled dimensions not the image attributes.
- Fixed ignoring `nowrap` on `<td nowrap="nowrap">` when an absolute width is specified.
- Fixed incorrect clipping when a layer is present between the column and the content layer.
- Fixed incorrect static position of absolute positioned elements inside relative positioned containers.
- Fixed layout for fixed position elements relative to a transformed container.
- Fixed layout overflow rectangle overflows interfering with the scrollbar.
- Fixed negative shadow repaint issue.
- Fixed preventing a focus ring from being painted for anonymous block continuations.
- Fixed recalculating intrinsic widths in the old containing block chain when an object goes out of flow.
- Fixed rendering extreme `border-radius` values.
- Fixed specified hue interpolation method for hues less than 0 or greater than 360.
- Fixed tab handling in right-to-left editing.
- Fixed text selection on flex and grid box items.
- Fixed the position and thickness of underlines to be device pixel aligned.
- Fixed transforms for table sections.
- Fixed transition ellipsis box from “being a display box on the line” to “being an attachment” of the line box.
- Fixed unexpected overlapping selection with tab in right-to-left context.
- Fixed updating table rows during simplified layout.
- Fixed: improved balancing for border, padding, and empty block content.

##### Safari Extensions

###### New Features

- Added `MAX_NUMBER_OF_DYNAMIC_AND_SESSION_RULES` property to `declarativeNetRequest`.
- Added support for `:has()` selector in Safari Content Blocker rules.
- Added support for `declarativeNetRequest.setExtensionActionOptions`.
- Added support for `requestDomains` to `declarativeNetRequest` rules.
- Added support for `toggleReaderMode` to the `tabs` API.
- Added support for additional `browser.scripting` APIs including: `scripting.registerContentScript`, `scripting.getRegisteredContentScripts`, `scripting.unregisterContentScripts`, and `scripting.updateContentScripts`.
- Added support for modules in background service workers.
- Added support for SVG images as web extension icons.
- Added support for the `modifyHeaders` action type of `declarativeNetRequest`.
- Added support to allow extensions to store data in memory using the `browser.storage.session` API.
- Safari Web Extensions are now turned off upon update if the new version requests more host permissions.

###### Resolved Issues

- Extensions that request the `unlimitedStorage` permission no longer need to also request `storage`.
- Fixed `browser.declarativeNetRequest` namespace is now available when an extension has the `declarativeNetRequestWithHostAccess` permission.
- Fixed `isUrlFilterCaseSensitive` `declarativeNetRequest` rule condition to be false by default.
- Fixed `tabs.onUpdated` getting called on tabs that were already closed.
- Fixed background service worker failing to import scripts.
- Fixed content scripts not injecting into subframes when extension accesses the page after a navigation.
- Fixed CORS issue when doing fetch requests from a background service worker.
- Fixed declarativeNetRequest errors not appearing correctly in the extension’s pane of Safari Settings.
- Fixed display of extension cookie storage in Web Inspector. Now the extension name is shown instead of a UUID.
- Fixed declarativeNetRequest rules not loading when an extension is turned off and then on.
- Fixed result of `getMatchedRules()` to match other browsers.
- Fixed `browser.webNavigation` events firing for hosts where the extension did not have access.
- Removed Keyboard Shortcut conflict warnings for `browser.commands` when there are multiple commands without keyboard shortcuts assigned.

##### Scrolling

###### New Features

- Added support for smooth key-driven scrolling on macOS.

###### Resolved Issues

- Fixed `overscroll-behavior: none` to prevent overscroll when the page is too small to scroll.

##### Svg

###### Resolved Issues

- Fixed `<svg:text>` to not auto-wrap.
- Fixed `preserveAspectRatio` to stop accepting `defer`.
- Fixed `SVG.currentScale` to only set the page zoom for a standalone SVG.
- Fixed `svgElement.setCurrentTime` to restrict floats to finite values.
- Fixed applying changes to `fill` with `currentColor` to other colors via CSS.
- Fixed changes to the `filter` property getting ignored.
- Fixed CSS and SVG filters resulting in a low quality, pixelated image.
- Fixed focusability even when tab-to-links is enabled for `<svg:a>`.
- Fixed handling animation freezes when `repeatDur` is not a multiple of `dur`.
- Fixed making sure computed values for `baseline-shift` CSS property use `px` unit for lengths.

##### Tables

###### Resolved Issues

- Fixed not forcing `display: table-cell`, `display: inline-table`, `display: table`, and `float: none` on table cell elements when in quirks mode.
- Fixed removing the visual border when the table border attribute is removed.

##### Text

###### New Features

- Added support for `font-size-adjust`.

###### Resolved Issues

- Fixed `font-optical-sizing: auto` having no effect in Safari 16.
- Fixed directionality of the `<bdi>` and `<input>` elements to align with HTML specifications.
- Fixed handling an invalid `dir` attribute to not affect directionality.
- Fixed the default oblique angle from `20deg` to `14deg`.
- Fixed the handling of `<bdo>`.
- Fixed the order of how `@font-palette-values` `override-colors` are applied.

##### Webassembly

###### New Features

- Added support for WASM SIMD.

##### Web Animations

###### New Features

- Added animation support for `align-tracks` and `justify-tracks`.
- Added support for `KeyframeEffect.iterationComposite`.
- Added support for animating custom properties.
- Added support for blending of mismatched filter lists.

###### Resolved Issues

- Fixed `@keyframes` rules using an `inherit` value to update the resolved value when the parent style changes.
- Fixed `Animation.commitStyles()` triggering a mutation even when the styles are unchanged.
- Fixed `Animation.startTime` and `Animation.currentTime` setters support for CSSNumberish values.
- Fixed `baseline-shift` animation.
- Fixed `baselineShift` inherited changes.
- Fixed `commitStyles()` failing to commit a relative `line-height` value.
- Fixed `getKeyframes()` serialization of CSS values for an `onkeyframe` sequence.
- Fixed `rotate: x` and `transform: rotate(x)` to yield the same behavior with SVGs.
- Fixed `word-spacing` to support animating between percentage and fixed values.
- Fixed accounting for non-inherited CSS variables getting interpolated for standard properties on the same element.
- Fixed accumulating and clamping filter values when blending with `"none"`.
- Fixed accumulation support for the `filter` property.
- Fixed additivity support for the `filter` property.
- Fixed animation of color list custom properties with `iterationComposite`.
- Fixed blend transform when iterationComposite is set to `accumulate`.
- Fixed blending to account for `iterationComposite`.
- Fixed Calculating computed keyframes for shorthand properties.
- Fixed composite animations to compute blended additive or accumulative keyframes for in-between keyframes.
- Fixed computing the `keyTimes` index correctly for discrete values animations.
- Fixed CSS animations participation in the cascade.
- Fixed custom properties to support interpolation with a single keyframe.
- Fixed filter values containing a `url()` should animate discretely.
- Fixed interpolating custom properties to take `iterationComposite` into account.
- Fixed jittering when animating a rotated image.
- Fixed keyframes to be recomputed if a custom property registration changes.
- Fixed keyframes to be recomputed if the CSS variable used is changed.
- Fixed keyframes to be recomputed when `bolder` or `lighter` is used on a `font-weight` property.
- Fixed keyframes to be recomputed when a parent element changes value for a custom property set to `inherit`.
- Fixed keyframes to be recomputed when a parent element changes value for a non-inherited property set to `inherit`.
- Fixed keyframes to be recomputed when the `currentcolor` value is used on a custom property.
- Fixed keyframes to be recomputed when the `currentcolor` value is used.
- Fixed opacity to use unclamped values for `from` and `to` keyframes with `iterationComposite`.
- Fixed running a transition on an inherited CSS variable getting reflected on a standard property using that variable as a value.
- Fixed seamlessly updating the playback rate of an animation.
- Fixed setting `iterationComposite` should invalidate the effect.
- Fixed setting the `transition-property` to `none` does not disassociate the CSS Transition from owning the element.
- Fixed the composite operation of implicit keyframes for CSS Animations to return `"replace"`.
- Fixed the timing model for updating animations and sending events.
- Fixed updating timing to invalidate the effect.

##### Web Api

###### New Features

- Added support for 2D-only OffscreenCanvas.
- Added support for `gamepad.vibrationActuator`.
- Added support for a submitter parameter in the FormData constructor.
- Added support for COEP violation reporting.
- Added support for COOP/COEP navigation violation reporting.
- Added support for Fetch Initiator.
- Added support for Fetch Metadata Request Headers.
- Added support for importing compressed EC keys in WebCrypto.
- Added support for loading scripts for nested workers.
- Added support for non-autofill credential type for the `autocomplete` attribute.
- Added support for revoking Blob URLs across same-origin contexts.
- Added support for Scroll to Text Fragment
- Added support for Service Workers and Shared Workers to the Permissions API.
- Added support for the `isComposing` attribute on InputEvent.
- Added support for the Compression Streams API.
- Added support for the Notification API in dedicated workers.
- Added support for the Reporting API.
- Added support for the Screen Wake Lock API.
- Added support for the UserActivation API.
- Added support for `ScreenOrientation.type`, `ScreenOrientation.angle`, and `ScreenOrientation.onchange`.
- Added support for the termination of nested workers.
- Added support for the unprefixed Fullscreen API on macOS and iPadOS.
- Added support for transfer size metrics for first parties in `ServerTiming` and `PerformanceResourceTiming`.
- Added support to the Permissions API for dedicated workers.
- Added support for the `messageerror` event.

###### Resolved Issues

- Fixed `-webkit-user-select: none` allowing text to be copied to clipboard.
- Fixed `contentEditable` caret getting left aligned instead of centered when the `:before` pseudo-element is used.
- Fixed `Cross-Origin-Embedder-Policy` incorrectly blocking scripts on cache hit.
- Fixed `CSSRule.type` to not return values greater than 15.
- Fixed `document.open()` to abort all loads when the document is navigating.
- Fixed `document.open()` to remove the initial `about:blank`-ness of the document.
- Fixed `Element.querySelectorAll` not obeying element scope with ID.
- Fixed `FileSystemSyncAccessHandle` write operation to be quota protected.
- Fixed `getBoundingClientRect()` returning the wrong value for `<tr>`, `<td>`, and its descendants for a vertical table.
- Fixed `HTMLOutputElement.htmlFor` to make it settable.
- Fixed `queryCommandValue("stylewithcss")` to always return an empty string.
- Fixed `StorageEvent.initStorageEvent()` to align with HTML specifications.
- Fixed `textContent` leaving dir=auto content in the wrong direction.
- Fixed `user-select: initial` content within `user-select: none` should be copied
- Fixed `WorkerGlobalScope.isSecureContext` to be based on the owner’s top URL, not the owner’s URL.
- Fixed a bug where `mousedown` without `mouseup` in a frame prevents a click event in another frame.
- Fixed a sometimes incorrect location after exiting mouse hover.
- Fixed accepting `image/jpg` for compatibility.
- Fixed adding a non-breaking space, instead of a plain space, when it is inserted before an empty text node.
- Fixed behavior of nested click event on a label element with a checkbox.
- Fixed BroadcastChannel in a SharedWorker when hosted in a cross-origin iframe.
- Fixed calculation of direction for text form control elements with `dir="auto"`.
- Fixed canvas fallback content focusability computation.
- Fixed deleting a button element leaving the button’s style in a `contenteditable` element.
- Fixed disconnected `<fieldset>` elements sometimes incorrectly matching `:valid` or `:invalid` selectors.
- Fixed dragging the mouse over a `user-select: none` node can begin selection in another node.
- Fixed ensuring nested workers get controlled if matching a service worker registration.
- Fixed errors caught and reported for `importScripts()`.
- Fixed escaping “&” in JavaScript URLs for `innerHTML` and `outerHTML`.
- Fixed EventSource to stop allowing trailing data when parsing a retry delay.
- Fixed Fetch Request object to keep its Blob URL alive.
- Fixed filled text on a canvas with a web font refreshing or disappearing.
- Fixed find on page failing to show results in PDFs.
- Fixed firing an error event when link preload fails synchronously.
- Fixed form submissions to cancel JavaScript URL navigations.
- Fixed handing the `onerror` content attribute on body and frameset elements.
- Fixed handling opaque origin Blob URLs.
- Fixed handling text documents to align to modern HTML specifications.
- Fixed handling the onerror content attribute on `<body>` and `<frameset>` elements.
- Fixed HTMLTemplateElement to have a `shadowRootMode` attribute.
- Fixed including alternate stylesheets in `document.styleSheets`.
- Fixed incorrect caret movement in some right-to-left `contenteditable` elements.
- Fixed incorrect color for videos loaded in a canvas.
- Fixed incorrect image `srcset` candidate chosen for `<img>` cloned from `<template>`.
- Fixed incorrectly ignored `X-Frame-Options` HTTP headers with an empty value.
- Fixed lazy loading images sometimes not loading.
- Fixed link elements to be able to fire more than one `load` or `error` event.
- Fixed loading Blob URLs with a fragment from opaque, unique origins.
- Fixed maintaining the original `Content-Type` header on a 303 HTTP redirect.
- Fixed module scripts to always decode using UTF-8.
- Fixed MouseEventInit to take `movementX` and `movementY`.
- Fixed not dispatching a `progress` event when reading an empty file or blob using the FileReader API.
- Fixed not replacing the current history item when navigating a cross-origin iframe to the same URL.
- Fixed overriding the mimetype for an XHR.
- Fixed parsing of negative age values in CORS prefetch responses.
- Fixed pasting of the first newline into text area.
- Fixed preventing selection for generated counters in ordered lists.
- Fixed Safari frequently using stale cached resources despite using Reload Page From Origin.
- Fixed scheduling a navigation to a Blob URL to keep the URL alive until the navigation occurs.
- Fixed sending Basic authentication via XHR using `setRequestHeader()` when there is an existing session.
- Fixed setting `style=""` to destroy the element’s inline style.
- Fixed setting the `tabIndex` of a non-focusable HTMLElement.
- Fixed system colors not respecting inherited `color-scheme` values.
- Fixed textarea placeholder text not disappearing when text is inserted without a user gesture.
- Fixed the `event.keyIdentifier` value for F10 and F11 keys.
- Fixed the click event to not get suppressed on textarea resize.
- Fixed the computed value for the `transform` property with `SkewY`.
- Fixed the initialization of color properties.
- Fixed timing of ResizeObserver and IntersectionObserver to match other browsers.
- Fixed toggling a details element when a summary element receives a `click()`.
- Fixed updating Text node children of an option element to not reset the selection of the select element.
- Fixed using NFC Security Key on iOS.
- Fixed using WebAuthn credentials registered on iOS 15 if iCloud Keychain is disabled.
- Fixed WebAuthn sending Attestation as None when requested as Direct.
- Fixed XHR aborting to align with standards specification
- Fixed XHR error events to return 0 for loaded and total.
- Fixed: Made all FileSystemSyncAccessHandle methods synchronous.
- Fixed: Removed a gray border while loading images with `loading="lazy"`.
- Fixed: Removed the `precision="float"` attribute on `<input type="range">`.

##### Web Apps

###### New Features

- Added support for Web Push in web apps saved to the home screen on iOS.
- Added support for the `"id"` member in Web App Manifest files.
- Added support for the Badging API.
- Added support for third-party browsers to offer Add to Home Screen from the Share menu.

##### Webgl

###### New Features

- Added support for `display-p3` wide-gamut color space in WebGL canvas.
- Added support for `WEBGL_clip_cull_distance`.

###### Resolved Issues

- Fixed video textures set to repeat.

##### Web Inspector

###### New Features

- Added a Badges button to control what badges are shown in the Elements Tab.
- Added a Path column to the Network Tab.
- Added a setting to turn off dimming nodes that aren’t visible on the page in the Settings Tab.
- Added alphabetic sorting of headers in the Network Tab.
- Added Event badges for nodes that have event listeners in the Elements Tab.
- Added OpenGL object IDs in the Canvas inspector of the Graphics Tab.
- Added Scroll badges for scrollable elements in the Elements Tab.
- Added showing relevant special breakpoints in the Pause Reason section of the Sources Tab.
- Added support for user preference overrides in the Elements Tab.
- Added support for console snippets in the Console Tab.
- Added support for editing `@media`, `@container`, and `@supports` rules in the Styles panel of the Elements Tab.
- Added support for editing font variation axes in the Elements Tab.
- Added support for function breakpoints and tracepoints.
- Added support for inline breakpoints in the Sources Tab.
- Added support for nodes that aren’t visible on the page to appear dimmed in the DOM tree of the Elements Tab.
- Added support for per-page network throttling in the Network Tab.
- Added support for showing warnings for synthesized bold or oblique in the Font details sidebar of the Elements Tab.
- Added support for symbolic breakpoints in the Sources Tab
- Added using the Shift key to highlight the initiator or initiated resources in the Network Tab.

###### Resolved Issues

- Fixed “Inspect Element” not highlighting the element.
- Fixed capturing async stack traces for `queueMicrotask`.
- Fixed clicking coalesced events in the timeline selecting the wrong event.
- Fixed event breakpoints to support case-insensitive and RegExp matching.
- Fixed sending `Console.StackTrace` instead of an array of `Console.CallFrame`.
- Fixed slow search with a lot of files in the Open Resource dialog.
- Fixed sorting prefixed properties below non-prefixed properties in the Computed panel of the Elements Tab.
- Fixed the always empty Attributes section in the Node panel of the Elements Tab.
- Fixed the Computed Tab scrolling to the top when a `<style>` is added to the page.
- Fixed URL breakpoints to also pause when HTML attributes are set that trigger loads.
- fixed: Improved the visual hierarchy of the Layout sidebar in the Elements Tab.

##### Webdriver

###### New Features

- Added support for generateTestReport.
- Added support for shadow roots.
- Added support for the “Get Computed Role” and “Get Computed Label” commands.
- Added support for the `SameSite` cookie attribute.
- Added support for typing characters that are represented by multiple code points, including emoji.

###### Resolved Issues

- Fixed “Get Element Rect” to not round to integer values.
- Fixed automation sessions terminating during navigation.
- Fixed click element failing on iPad when Stage Manager is disabled.
- Fixed HTTP GET requests with a body failing.
- Fixed the Shift modifier key not applying to typed text.

##### Wkwebview

###### New Features

- Added WKPreferences `shouldPrintBackgrounds` API to allow clients to specify if a page’s background should be included when printing.

## See Also

- [Safari 16.6 Release Notes](safari-16_6-release-notes.md)
  Released July 24, 2023 — Version 16.6 (18615.3.12)
- [Safari 16.5 Release Notes](safari-16_5-release-notes.md)
  Released May 18, 2023 — Version 16.5 (18615.2.9)
- [Safari 16.3 Release Notes](safari-16_3-release-notes.md)
  Released January 23, 2023 — Version 16.3 (18614.4.6)
- [Safari 16.2 Release Notes](safari-16_2-release-notes.md)
  Released December 13, 2022 — Version 16.2 (18614.3.7)
- [Safari 16.1 Release Notes](safari-16_1-release-notes.md)
  Released October 24, 2022 — Version 16.1 (18614.2.9)
- [Safari 16 Release Notes](safari-16-release-notes.md)
  Released September 12, 2022 — Version 16 (18614.1.25)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes)*