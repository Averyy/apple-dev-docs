# Safari 26.1 Release Notes

**Framework**: Safari Release Notes

Released November 3, 2025 — 26.1 (20622.2.11)

#### Overview

Safari 26.1 is available for iOS 26.1, iPadOS 26.1, visionOS 26.1, macOS 26.1, macOS Sequoia, and macOS Sonoma.

##### Accessibility

###### Resolved Issues

- Fixed hit testing for scrolled iframe content by adjusting for the frame’s scroll position, ensuring accurate element detection across assistive technologies. (158233884)
- Fixed an issue where VoiceOver reports the wrong radio count with a dynamically inserted radio option.  (159937173)
- Fixed exposing content within dynamically expanded details elements in the accessibility tree.  (159937257)
- Fixed the target of `aria-labelledby` not updating its accessibility label after dynamic `innerHTML` change in the label.  (160691619)

##### Css

###### New Features

- Added support for remembering the last successful `position-try` fallback in CSS anchor positioning to reduce layout jumps when styles change. (158452223)

###### Resolved Issues

- Fixed anchor positioning to handle fragmented multicolumn flows. (156958568)
- Fixed anchor positioning fallbacks to respond to scrolling. (158451016)
- Fixed `@media print` styles to work when used inside a nested rule. (158608834)
- Fixed an issue where container queries doesn’t work with `position-try` element. (158880410)
- Fixed: Improved the performance of `:has(> .changed) .subject` selectors.  (159257003)
- Fixed pseudo-class invalidation performance by creating separate `RuleSets` for attribute selectors like `:has([attr=value])` to avoid using universal invalidation. (159257022)
- Fixed an issue where changing the `ruby-overhang` property did not trigger a layout update, ensuring proper rendering when overhang values change. (159573050)
- Fixed anchor positioning to account for a left-hand scrollbar in right-to-left and `vertical-rl` containing blocks. (160723993)
- Fixed `offsetParent` to return the fixed-position element’s containing block when it is not the viewport, such as a transformed element. (160892685)
- Fixed handling inline containing blocks for CSS Anchor Positioning. (160892829)
- Fixed an issue where anchor-positioned elements failed to update their position when the default anchor changed. (160892850)
- Fixed `<select>` fallback styling by removing the outdated background and updating the dropdown arrow. (161104364)
- Fixed an issue where transitioning an element to `display: none` with `transition-behavior: allow-discrete` and CSS Anchor Positioning would repeatedly restart the transition. (161421046)
- Fixed `position-area` for the initial containing block to include the in-flow scrollable area, improving alignment for typical overflow cases. (161997622)

##### Forms

###### Resolved Issues

- Fixed native text inputs so that their background colors update when autofilled. (159014135)
- Fixed checkboxes and radio buttons missing borders in the filled state when “Increased Contrast” is enabled on macOS. (159379948)

##### Pdf

###### Resolved Issues

- Fixed VoiceOver not recognizing the password form in encrypted documents.  (159240531)

##### Rendering

###### Resolved Issues

- Fixed a bottom gap appearing on layouts with viewport-sized fixed containers on iOS. (158055568)
- Fixed `position-visibility: anchors-visible` visibility heuristic when anchor is clipped by an ancestor container.  (160060564)
- Fixed an issue on iOS where Safari extension popups and some websites could scroll or flicker unexpectedly. (160216319)
- Fixed list markers overlapping text in certain situations. (160892820)
- Fixed an issue that caused cropped flexbox elements to render incorrectly. (161218029)
- Fixed string search freezing when subject has large number (>1000). (161421015)

##### Svg

###### New Features

- Added support for relative units in SVG. (160883553)

###### Resolved Issues

- Fixed absolutely positioned SVGs so that their size correctly accounts for the padding of the containing block when the SVG root is out-of-flow. (160727702)

##### Security

###### Resolved Issues

- Fixed Safari ignoring the `style-src-elem` Content Security Policy directive ensuring it is checked before falling back to `style-src`, in line with CSP3 specifications. (157298407)

##### Web Api

###### Resolved Issues

- Fixed an issue on iOS 26 where pressing the B button on a gamepad could make a page appear to lose `gamepad` focus by bypassing the system’s automatic navigation behavior. (159125095)

##### Web Inspector

###### Resolved Issues

- Fixed issue where searching on certain text fails to find matches.  (159897282)

##### Webgpu

###### Resolved Issues

- Fixed an issue where `GPUQueue.copyExternalImageToTexture` could not handle SVG images. (158442476)
- Fixed an issue where video playback using the WebGPU renderer in WebCodecs could display a black screen. (158442539)
- Fixed an issue where WebGPU video textures failed to load in Three.js panoramas. (159918934)

##### Webkit Api

###### Resolved Issues

- Fixed a crash when an app uses `WKWebView::loadRequest` API on background threads.  (162225842)

##### Webrtc

###### Resolved Issues

- Fixed `getUserMedia()` on iOS incorrectly firing `devicechange` events when there was no actual change to available microphones or default devices. (157693528)

## See Also

- [Safari 26.3 Beta Release Notes](safari-26_3-release-notes.md)
  Released December 15, 2025 — 26.3 (20623.2.2)
- [Safari 26.2 Release Notes](safari-26_2-release-notes.md)
  Released December 12, 2025 — 26.2 (20623.1.14)
- [Safari 26.0 Release Notes](safari-26-release-notes.md)
  Released September 15, 2025 — 26.0 (20622.1.22)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-26_1-release-notes)*