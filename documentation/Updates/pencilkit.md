# PencilKit updates

**Framework**: Updates

Learn about important changes to PencilKit.

#### Overview

Browse notable changes in [`PencilKit`](https://developer.apple.com/documentation/PencilKit).

#### June 2026

##### Strokes

- Access and assign a stable identity to strokes and stroke paths using the `id` property on [`PKStroke`](https://developer.apple.com/documentation/PencilKit/PKStroke-swift.struct) and [`PKStrokePath`](https://developer.apple.com/documentation/PencilKit/PKStrokePath-swift.struct), which conform to `Identifiable`.
- Select strokes programmatically and respond to selection changes using the [`selection`](https://developer.apple.com/documentation/PencilKit/PKCanvasView/selection) property and the [`canvasViewSelectionDidChange(_:)`](https://developer.apple.com/documentation/PencilKit/PKCanvasViewDelegate/canvasViewSelectionDidChange(_:)) delegate method.
- Erase portions of a drawing along a path using [`erasePath(_:mask:transform:)`](https://developer.apple.com/documentation/PencilKit/PKDrawing-swift.struct/erasePath(_:mask:transform:)-shn), or get a new drawing with the erasure applied using [`erasingPath(_:mask:transform:)`](https://developer.apple.com/documentation/PencilKit/PKDrawing-swift.struct/erasingPath(_:mask:transform:)-9dpi9).
- Convert a stroke path to a `CGPath` using the [`bezierRepresentation`](https://developer.apple.com/documentation/PencilKit/PKStrokePathReference/bezierRepresentation) property, or create a stroke path from a bezier path using [`init(bezierPath:creationDate:pointProvider:)`](https://developer.apple.com/documentation/PencilKit/PKStrokePath-swift.struct/init(bezierPath:creationDate:pointProvider:)).

##### Handwriting Recognition

- Recognize handwritten text, search within ink, and generate indexable string content using [`PKStrokeRecognizer`](https://developer.apple.com/documentation/PencilKit/PKStrokeRecognizer).

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/pencilkit)*