# Safari 27.1 Release Notes

**Framework**: Safari Release Notes  
**Role**: Article

Released October 23, 2026 — 27.1 (20625.1.29)

## Overview

Safari 27.1 is available for iOS 27.1.

### PDF

#### New Features

- Added support for automatically showing PDFs as two pages side by side when a foldable device is partially folded into a book pose, and switching back to a single page when the device is unfolded.  (170353889)

### Web API

#### New Features

- Added support for the Device Posture API behind a feature flag, so websites can respond when a device is folded. `navigator.devicePosture.type` returns `continuous` or `folded`, and the `change` event fires on `navigator.devicePosture` when the posture changes.

  The `device-posture` media query matches `continuous` or `folded`. Note that without a document, `navigator.devicePosture.type` defaults to `continuous`.  (170005463)
- Added support for the Viewport Segments API behind a feature flag, so websites can lay out content around a fold between the separate areas of the screen.

  The `horizontal-viewport-segments` and `vertical-viewport-segments` media queries match the number of segments. The `env()` variables `viewport-segment-width`, `viewport-segment-height`, `viewport-segment-top`, `viewport-segment-right`, `viewport-segment-bottom`, and `viewport-segment-left` take horizontal and vertical index arguments to return the dimensions and position of each segment.  (176426722)

## See Also

### Version 27
- [Safari 27.2 Release Notes](./safari-27_2-release-notes.md)
  Released October 26, 2026 — 27.2 (20625.2.8)
- [Safari 27 Release Notes](./safari-27-release-notes.md)
  Released September 14, 2026 — 27.0 (20625.1.29)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes)*