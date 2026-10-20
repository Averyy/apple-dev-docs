# PencilKit updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to PencilKit.

#### Overview

Browse notable changes in [PencilKit](../PencilKit/PencilKit.md).

#### June 2026

##### Strokes

- Access and assign a stable identity to strokes and stroke paths using the `id` property on [`PKStroke`](../PencilKit/pkstroke-swift.struct.md) and [`PKStrokePath`](../PencilKit/pkstrokepath-swift.struct.md), which conform to `Identifiable`.
- Select strokes programmatically and respond to selection changes using the [`selection`](../PencilKit/pkcanvasview/selection.md) property and the [`canvasViewSelectionDidChange(_:)`](../PencilKit/pkcanvasviewdelegate/canvasviewselectiondidchange%28_%29.md) delegate method.
- Erase portions of a drawing along a path using [`erasePath(_:mask:transform:)`](../PencilKit/pkdrawing-swift.struct/erasepath%28_,mask,transform%29-shn.md), or get a new drawing with the erasure applied using [`erasingPath(_:mask:transform:)`](../PencilKit/pkdrawing-swift.struct/erasingpath%28_,mask,transform%29-9dpi9.md).
- Convert a stroke path to a `CGPath` using the [`bezierRepresentation`](../PencilKit/pkstrokepathreference/bezierrepresentation.md) property, or create a stroke path from a bezier path using [`init(bezierPath:creationDate:pointProvider:)`](../PencilKit/pkstrokepath-swift.struct/init%28bezierpath,creationdate,pointprovider%29.md).

##### Handwriting recognition

- Recognize handwritten text, search within ink, and generate indexable string content using [`PKStrokeRecognizer`](../PencilKit/pkstrokerecognizer.md).

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/pencilkit)*