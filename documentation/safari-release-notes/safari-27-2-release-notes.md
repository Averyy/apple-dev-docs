# Safari 27.2 Beta Release Notes

**Framework**: Safari Release Notes

Released September 16, 2026 — 27.2 beta (20625.2.4)

#### Overview

Safari 27.2 beta is available for iOS 27.2 beta, iPadOS 27.2 beta, visionOS 27.2 beta, macOS 27.2 beta, macOS 26, and macOS Sequoia.

##### Accessibility

###### Resolved Issues

- Fixed list, table, tree, and canvas content being omitted from the accessible name or description when the containing element is referenced by `aria-labelledby` or `aria-describedby`. (186015032)
- Fixed VoiceOver repeating text it had already announced when a page streams content by re-rendering an `aria-live` region instead of appending to it. (186766347)

##### Animations

###### Resolved Issues

- Fixed `animation-range-start` and `animation-range-end` resolving incorrectly when `zoom` is applied, including when the value is inherited from an element with a different zoom factor. (185760120)

##### Css

###### Deprecations

- Renamed the `flow-tolerance` property to `fit-tolerance` for `display: grid-lanes`, keeping `flow-tolerance` as a deprecated alias that Web Inspector now flags. (185816680)

##### Forms

###### New Features

- Added support for `safe` and `unsafe` overflow alignment with `normal`, and for `safe` alignment on fixed position boxes so they stay in view even when that means overflowing their `position-area`. Also, applied `safe` alignment to `::picker(select)`, which keeps base appearance `<select>` pickers fully in view. (186812035)

###### Resolved Issues

- Fixed: Updated the default styling for `appearance: base-select` to center-align items, use `lh` units for padding, and reset all font properties on ::picker-icon and ::checkmark. (184843832)

##### Html

###### Resolved Issues

- Fixed the window `load` event never being dispatched when a `readystatechange` handler starts a new load. (186475302)

##### Javascript

###### Resolved Issues

- Fixed `for await...of` over an async generator skipping the `Promise.prototype.constructor` lookup required by `PromiseResolve` when that property is replaced. (183960626)

##### Media

###### Resolved Issues

- Fixed `AudioContext.decodeAudioData()` failing with an `EncodingError` for valid AAC and M4A files whose file brand is not `mp4`. (183474728)
- Fixed video showing a black screen while audio continued to play after the video decoder was invalidated. (184041554)
- Fixed `ManagedMediaSource` not firing the `startstreaming` event when seeking to a time that is not buffered, which could stall playback. (185166787)

##### Networking

###### Resolved Issues

- Fixed cookies set by a top-level navigation’s own response being capped to a seven day lifetime when the site’s hostname is CNAMEd to a different registrable domain. (183787115)

##### Svg

###### Resolved Issues

- Fixed dynamic changes to a `<foreignObject>` element’s `x` and `y` values having no effect. (184273832)

##### Safari Mcp

###### Resolved Issues

- Fixed Safari taking keyboard focus from other apps when creating tabs or capturing screenshots under Safari MCP control.  (182558329)

##### Web Extensions

###### Resolved Issues

- Fixed a significant delay before web extension content is injected when Safari is cold launched. (185268822)

##### Webgpu

###### Resolved Issues

- Fixed a severe frame rate drop when calling `executeBundles()` with render bundles that contain `drawIndirect()` or `drawIndexedIndirect()`. (186099290)

##### Webrtc

###### Resolved Issues

- Fixed an issue where `getUserMedia()` requests for audio permanently failed with `NotAllowedError` after the system audio service was reset. (186939802)

## See Also

- [Safari 27 Release Notes](safari-27-release-notes.md)
  Released September 14, 2026 — 27.0 (20625.1.29)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes)*