# Safari 15.5 Release Notes

**Framework**: Safari Release Notes

Released May 16, 2022 — Version 15.5 (17613.2.7)

#### Overview

Safari 15.5 ships with iOS & iPadOS 15.5 and macOS 12.4.

##### Html

###### New Features

- Added support for the `inert` attribute.

###### Resolved Issues

- Fixed SVG tags behind modal dialogs to not be clickable.
- Fixed the Dialog element only animating once.
- Fixed rendering a USDZ loaded as the main resource.
- Fixed uploading Pages files to file inputs accepting Pages and JPEG files.

##### Web Api

###### Resolved Issues

- Fixed BroadcastChannel to prevent communicating across distinct opaque origins.
- Fixed respecting website policies during COOP-based process swaps.
- Fixed `PointerEvent.movementX` always being 0.
- Fixed resolving a fetch promise when a page enters page cache.
- Fixed pointer events to perform a hit test only if there isn’t a pointer capture target override.
- Fixed computing the site for cookies when the document is created by `window.open`.
- Fixed `Element.focus({preventScroll: true})` to correctly prevent scrolling on iOS.

##### Css

###### Resolved Issues

- Fixed `background-clip: text` to work with `display: flex`.
- Fixed rendering for many `position: sticky` elements.
- Fixed `position: sticky` elements moving incorrectly while scrolling.
- Fixed text contents in `<span>` with opacity not updating when a sibling element has `will-change: transform`.
- Fixed `:focus-visible` matching on the wrong element when focused via script.
- Fixed `text-shadow` getting clipped.
- Fixed the behavior of a `position: sticky` element within `contain: paint`.
- Fixed `aspect-ratio` with percentage widths.
- Fixed returning the default computed style for elements without the `transition` or `animation` shorthands.

##### Authentication

###### Resolved Issues

- Fixed WebAuthn implementation to match specifications to use the default `pubKeyCredParams` list if the list in `makeCredential` is empty.

##### Content Security Policy

###### New Features

- Added support for the `worker-src` Content Security Policy directive.
- Updated Content Security Policy console logging in Web Inspector.

###### Resolved Issues

- Fixed blocking image content in object elements.
- Fixed sending violation reports to the document for a detached element.
- Fixed nonce hiding from the DOM.
- Fixed Content Security Policy handling of JavaScript URLs.

##### Media

###### Resolved Issues

- Fixed key rotation for single key audio in a modern encrypted media extension (EME) paired with a native HTTP Live Streaming (HLS) player.
- Fixed disabled Control Center spatial control when playing a video in Safari.
- Fixed loading a model in QuickLook when passing extra parameters.
- Fixed muted video that sometimes becomes paused when taken to full screen.
- Fixed video playback on iPhone 7.
- Fixed video playback for HEVC content encodings that generate many B-frames with a wide sliding window.
- Fixed HLS stream `currentTime` sometimes jumping backwards.
- Fixed clicking on the progress bar often pausing a YouTube video.
- Fixed blob videos slowing to pause.
- Fixed audio echo after the camera is paused or unpaused.
- Fixed playback of HTML5 embedded audio with unbounded range requests.
- Fixed the video poster disappearing prematurely on play, leaving a transparent video element.

##### Webrtc

###### Resolved Issues

- Fixed incorrect label returned by `getUserMedia` regardless of language selected.
- Fixed perceived audio latency.

##### Rendering

###### Resolved Issues

- Fixed text wrapping for windows that exceed a certain width.
- Fixed a Korean webfont rendering issue.
- Fixed a flash of missing text content with transform-related animations.
- Fixed to use `colgroup` for table sizing when it comes after `thead`, `tbody`, `tfoot`, or `tr` elements.
- Fixed two Bopomofo tone marks to move to the correct place in vertical text with a particular Bopomofo font.

##### Apple Pay

###### Resolved Issues

- Fixed the Apple Pay sheet to return `billingContact` on iOS.

##### Webgl

###### Resolved Issues

- Fixed WebGL rendering when using `preserveDrawingBuffer` on iOS.
- Fixed a number of issues related to multisampling that were breaking WebGL content.
- Fixed handling `TypedArray` with `AllowShared` to be accepted.
- Fixed `WEBGL_multi_draw` validation.

##### Web Inspector

###### Resolved Issues

- Fixed large message handling from remote devices.
- Fixed an issue with repeated opening and closing.

##### Compatibility

###### Resolved Issues

- Fixed launching Microsoft Teams from Safari.

##### Wkwebview

###### New Features

- Added `minimumViewportInset` and `maximumViewportInset` API to support small (`svw`, `svh`, `svi`, `svb`, `svmin`, `svmax`), large (`lvw`, `lvh`, `lvi`, `lvb`, `lvmin`, `lvmax`), dynamic (`dvw`, `dvh`, `dvi`, `dvb`, `dvmin`, `dvmax`), and logical (`vi`, `vb`) viewport units.

##### Sfsafariviewcontroller

###### Resolved Issues

- Fixed a noticeable delay in playback when rotating a full-screen YouTube video.

##### Safari Extensions

###### New Features

- Added support for `optional_host_permissions` for Safari Web Extensions.

###### Resolved Issues

- Fixed a crash when clicking on Safari App Extension toolbar items.
- Fixed an issue where `SFContentBlockerManager.getStateOfContentBlocker()` could return an incorrect value on iOS.

## See Also

- [Safari 15.6 Release Notes](safari-15_6-release-notes.md)
  Released July 20, 2022 — Version 15.6 (17613.3.9)
- [Safari 15.4 Release Notes](safari-15_4-release-notes.md)
  Released March 14, 2022 — Version 15.4 (17613.1.17)
- [Safari 15.2 Release Notes](safari-15_2-release-notes.md)
  Released December 13, 2021 — Version 15.2 (17612.3.6)
- [Safari 15 Release Notes](safari-15-release-notes.md)
  Released September 20, 2021 — Version 15 (17612.1.27)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-15_5-release-notes)*