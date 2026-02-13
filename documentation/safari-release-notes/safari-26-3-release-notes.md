# Safari 26.3 Release Notes

**Framework**: Safari Release Notes

Released February 11, 2026 — 26.3 (20623.2.7)

#### Overview

Safari 26.3 is available for iOS 26.3, iPadOS 26.3, visionOS 26.3, macOS 26.3, macOS Sequoia, and macOS Sonoma.

##### Css

###### Resolved Issues

- Fixed a style resolution loop that occurred when a `position-try` box was inside a `display: none` ancestor. (163691885)
- Fixed an issue where anchor-positioned elements repeatedly transitioning from `display: block` to `display: none` cause position jumps during animation. (163862003)
- Fixed an issue where `fixed`-positioned boxes using `position-area` were incorrectly included in the scrollable containing block calculation. (164017310)
- Fixed an issue where `text-decoration: underline` was rendered too high when `text-box-trim` was applied to the root inline box. (165945326)
- Fixed a multi-column layout issue where the `widows` and `text-indent` properties are applied cause an incorrect indent on the portion of the paragraph that flows into the next column. (165945497)
- Fixed an issue where CSS cursors like `move`, `all-scroll`, `ew-resize`, and `ns-resize` did not display correctly. (166731882)

##### Dom

###### Resolved Issues

- Fixed incorrect timestamp handling and switched to use the raw touch timestamp. (164262652)

##### Http

###### New Features

- Added support for Zstandard content encoding in Safari 26.3 for iOS, iPadOS, visionOS, and macOS 26.3.  (157682304)

##### Media

###### New Features

- Fullscreen video playback on visionOS now automatically dims your surroundings to help you focus on the content. (164032895)

###### Resolved Issues

- Fixed an issue where the fullscreen button in visionOS inline video controls did not visually indicate interactivity by extending the glow effect to all `button.circular` elements. (164259201)
- Fixed Video Viewer mode for `iframe` videos on macOS. (164484608)
- Fixed an issue where Safari could not play live videos when the `sourceBuffer` content is removed and re-added causing the seek to not complete. (165628836)

##### Rendering

###### Resolved Issues

- Fixed an issue where positioned or transformed `<img>` elements containing HDR JPEGs with gain maps would incorrectly render as SDR. (163517157)

##### Safe Browsing

###### Resolved Issues

- Fixed a bug where if Safe Browsing queried for an entry on the Public Suffix List, and a Safe Browsing vendor responded that the whole effective TLD was unsafe, the whole site would be marked as unsafe.  (168155375)

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