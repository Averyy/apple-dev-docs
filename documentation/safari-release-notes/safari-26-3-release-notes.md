# Safari 26.3 Beta Release Notes

**Framework**: Safari Release Notes

Released December 15, 2025 — 26.3 (20623.2.2)

#### Overview

Safari 26.3 beta is available for iOS 26.3 beta, iPadOS 26.3 beta, visionOS 26.3 beta, macOS 26.3 beta, macOS Sequoia, and macOS Sonoma.

##### Css

###### Resolved Issues

- Fixed a style resolution loop that occurred when a `position-try` box was inside a `display: none` ancestor. (163691885)
- Fixed an issue where anchor-positioned elements repeatedly transitioning from `display: block` to `display: none` cause position jumps during animation. (163862003)
- Fixed an issue where `fixed`-positioned boxes using `position-area` were incorrectly included in the scrollable containing block calculation. (164017310)
- Fixed an issue where `text-decoration: underline` was rendered too high when `text-box-trim` was applied to the root inline box. (165945326)

##### Media

###### New Features

- Fullscreen video playback on visionOS now automatically dims your surroundings to help you focus on the content. (164032895)

###### Resolved Issues

- Fixed Video Viewer mode for `iframe` videos on macOS. (164484608)

##### Rendering

###### Resolved Issues

- Fixed an issue where positioned or transformed `<img>` elements containing HDR JPEGs with gain maps would incorrectly render as SDR. (163517157)

##### Web Api

###### New Features

- Added support for firing an `AbortSignal` when a `NavigateEvent` is aborted. (164125292)

## See Also

- [Safari 26.2 Release Notes](safari-26_2-release-notes.md)
  Released December 12, 2025 — 26.2 (20623.1.14)
- [Safari 26.1 Release Notes](safari-26_1-release-notes.md)
  Released November 3, 2025 — 26.1 (20622.2.11)
- [Safari 26.0 Release Notes](safari-26-release-notes.md)
  Released September 15, 2025 — 26.0 (20622.1.22)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-26_3-release-notes)*