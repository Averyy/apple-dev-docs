# Safari 27.2 Release Notes

**Framework**: Safari Release Notes  
**Role**: Article

Released October 26, 2026 — 27.2 (20625.2.8)

## Overview

Safari 27.2 is available for iOS 27.2, iPadOS 27.2, visionOS 27.2, macOS 27.2, macOS 26, and macOS Sequoia.

### Accessibility

#### Resolved Issues

- Fixed list, table, tree, and canvas content being omitted from the accessible name or description when the containing element is referenced by `aria-labelledby` or `aria-describedby`. (186015032)
- Fixed VoiceOver repeating text it had already announced when a page streams content by re-rendering an `aria-live` region instead of appending to it. (186766347)
- Fixed an issue where VoiceOver did not identify `<input type="date">`, `<input type="time">`, and `<input type="color">` controls as pop-up buttons on iOS. (187788949)

### Animations

#### Resolved Issues

- Fixed `animation-range-start` and `animation-range-end` resolving incorrectly when `zoom` is applied, including when the value is inherited from an element with a different zoom factor. (185760120)

### CSS

#### Resolved Issues

- Fixed an issue where an anchor-positioned element inside a modal `<dialog>` could be laid out offscreen and become invisible when the page was scrolled. (187933878)

#### Deprecations

- Renamed the `flow-tolerance` property to `fit-tolerance` for `display: grid-lanes`, keeping `flow-tolerance` as a deprecated alias that Web Inspector now flags. (185816680)

### Forms

#### New Features

- Allow combining `safe` and `unsafe` keywords with `normal` alignment, and change `safe` behavior for absolutely (and fixed positioned) boxes to keep the box within their original containing block (the viewport). Fixed an issue where a large picker for a base-appearance `<select>` could render outside the viewport, by applying `safe` alignment to keep it within its original containing block. (186812035)
- Added `::field-content` to `<select>` to allow styling of the selected option text when `<selectedcontent>` is not provided. Updated alignment of `appearance: base-select` `<select>` buttons to more reliably vertically center its contents. Updated `appearance: base-select` `<select>` buttons to inherit `text-overflow` from the `<select>` to the selected option text. Adjusted `appearance: base-select` `<select>` buttons to use `flex: 1` rather than `::picker-icon { margin-inline-start: auto; }` to manage spacing, ensuring that the picker icon is always visible even when `<selectedcontent>` is not provided.  (187617020)

#### Resolved Issues

- Fixed: Switched default `content` for `appearance: base-select` `<select>` `::picker-icon` to render with a glyph that does not require negative margins to align correctly.  (187411081)

### HTML

#### Resolved Issues

- Fixed the window `load` event never being dispatched when a `readystatechange` handler starts a new load. (186475302)

### JavaScript

#### Resolved Issues

- Fixed `for await...of` over an async generator skipping the `Promise.prototype.constructor` lookup required by `PromiseResolve` when that property is replaced. (183960626)

### Media

#### Resolved Issues

- Fixed an issue where `AudioContext.decodeAudioData()` failed with an `EncodingError` on valid AAC/M4A audio files. (183474728)
- Fixed video showing a black screen while audio continued to play after the video decoder was invalidated. (184041554)
- Fixed `ManagedMediaSource` not firing the `startstreaming` event when seeking to a time that is not buffered, which could stall playback. (185166787)
- Fixed an issue where a media element’s `play()` promise was not resolved when a `SourceBuffer` contained clear, unencrypted content. (188022510)
- Fixed an issue where the WebCodecs `VideoEncoder` could stall and produce no output for H.264 Main and High profiles. (188201298)

### Networking

#### Resolved Issues

- Fixed cookies set by a top-level navigation’s own response being capped to a seven day lifetime when the site’s hostname is CNAMEd to a different registrable domain. (183787115)

### SVG

#### Resolved Issues

- Fixed dynamic changes to a `<foreignObject>` element’s `x` and `y` values having no effect. (184273832)

### Safari MCP

#### Resolved Issues

- Fixed Safari taking keyboard focus from other apps when creating tabs or capturing screenshots under Safari MCP control.  (182558329)

### Web API

#### Resolved Issues

- Fixed an issue where transient activation could be incorrectly discarded, causing APIs gated on user activation (such as the Clipboard API) to fail on the first attempt. (187872193)

### Web Extensions

#### Resolved Issues

- Fixed a significant delay before web extension content is injected when Safari is cold launched. (185268822)

### WebGPU

#### Resolved Issues

- Fixed a severe frame rate drop when calling `executeBundles()` with render bundles that contain `drawIndirect()` or `drawIndexedIndirect()`. (186099290)

### WebRTC

#### Resolved Issues

- Fixed an issue where `getUserMedia()` requests for audio permanently failed with `NotAllowedError` after the system audio service was reset. (186939802)

## See Also

### Version 27
- [Safari 27.1 Release Notes](./safari-27_1-release-notes.md)
  Released October 23, 2026 — 27.1 (20625.1.29)
- [Safari 27 Release Notes](./safari-27-release-notes.md)
  Released September 14, 2026 — 27.0 (20625.1.29)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes)*