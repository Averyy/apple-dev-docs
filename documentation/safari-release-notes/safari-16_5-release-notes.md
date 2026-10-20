# Safari 16.5 Release Notes

**Framework**: Safari Release Notes

Released May 18, 2023 — Version 16.5 (18615.2.9)

#### Overview

Safari 16.5 is available for macOS Big Sur, macOS Monterey, macOS Ventura, iPadOS 16.5, and iOS 16.5.

#### Apple Pay

##### New Features

- Added support for pre-orders and deferred payments.

#### Css

##### New Features

- Added support for CSS Nesting.
- Added support for `:user-valid` and `:user-invalid`.

##### Resolved Issues

- Fixed Scroll to Text Fragment sometimes scrolling to the top after reloading the page.
- Fixed support for `x` resolution unit in `calc()`.
- Fixed reflecting trimmed `block-start`, `block-end`, `inline-start`, and `inline-end` margins for grid or flex items in computed styles.
- Fixed the top offset of self collapsing children at the end of a block container with `block-end` margin trim.
- Fixed triggering layout when changing `margin-trim` value.
- Fixed increasing `column-count` above 2 not updating the layout.
- Fixed CSS custom properties not applying to an SVG `use` element’s shadow tree.
- Fixed new CSS property unexpectedly dropped from an empty CSS rule when tabbing through or editing a selector.
- Fixed: Made `-webkit-image-set()` an alias of `image-set()`.

#### Editing Forms

##### Resolved Issues

- Fixed hairline on the selection of bidi text.
- Fixed photo library picker showing videos for `accept="image/*"`.

#### Javascript

##### Resolved Issues

- Updated digital display in `Intl.DurationFormat` to match spec changes.

#### Layout

##### Resolved Issues

- Fixed text wrapping for bidi text when line-breaking.

#### Lockdown Mode

##### New Restrictions

- Disabled WebCodecs API

#### Media

##### Resolved Issues

- Fixed non-audible AudioContext preventing the audio session to change from play-and-record after stopping capture.
- Fixed handling video streams containing a `CodecDelay` value that caused an audible pop at the beginning of video playback.
- Fixed video freezing in a video conference when removing AirPods Pro during the call.

#### Scrolling

##### Resolved Issues

- Fixed snapping to the last snap position when performing layout when scroll snapping occurs with a physical mouse wheel.
- Fixed pinch-to-zoom when toggling on and off scroll snapping.
- Fixed scroll snapping jumping to the previous page when swiping to the next page.
- Fixed scroll snapping to work with a physical scroll wheel on a mouse.

#### Rendering

##### Resolved Issues

- Fixed form controls rendering.
- Fixed visual updates for `content: counter()` when `position: absolute` is set.
- Fixed an unexpected visible first frame of a `transform` animation when `!important` style overrides the animated value.

#### Web Api

##### Resolved Issues

- Fixed filling metadata headers for preflight requests.
- Fixed OffscreenCanvas WebGL to fire the context lost event.
- Fixed `getFileHandle()` to return a TypeMismatchError on unexpected entry type.

#### Web Apps

##### Resolved Issues

- Fixed “Untitled” label on the back to previous app button when opening a web app via a link.

#### Web Assembly

##### Resolved Issues

- Fixed WASM SIMD breaking WebP decoding applications.

#### Web Inspector

##### New Features

- Added initial support for `color-mix` CSS values.

##### Resolved Issues

- Fixed element `::backdrop` rules showing up without a backdrop.
- Fixed “Selected element” console entry filling an entire row.
- Fixed an issue causing the mini console to always opens when choosing “Inspect Element”, even if it was previously closed.

## See Also

- [Safari 16.6 Release Notes](safari-16_6-release-notes.md)
  Released July 24, 2023 — Version 16.6 (18615.3.12)
- [Safari 16.4 Release Notes](safari-16_4-release-notes.md)
  Released March 27, 2023 — Version 16.4 (18615.1.26)
- [Safari 16.3 Release Notes](safari-16_3-release-notes.md)
  Released January 23, 2023 — Version 16.3 (18614.4.6)
- [Safari 16.2 Release Notes](safari-16_2-release-notes.md)
  Released December 13, 2022 — Version 16.2 (18614.3.7)
- [Safari 16.1 Release Notes](safari-16_1-release-notes.md)
  Released October 24, 2022 — Version 16.1 (18614.2.9)
- [Safari 16 Release Notes](safari-16-release-notes.md)
  Released September 12, 2022 — Version 16 (18614.1.25)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-16_5-release-notes)*