# ImageTranslationAlignmentObservation

**Framework**: Vision  
**Kind**: struct

Affine transform information that an image-alignment request produces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct ImageTranslationAlignmentObservation
```

#### Overview

This type of observation results from a [`TrackTranslationalImageRegistrationRequest`](tracktranslationalimageregistrationrequest.md), informing the [`alignmentTransform`](imagetranslationalignmentobservation/alignmenttransform.md) performed to align the input images.

## Topics

### Creating an observation
- [init(VNImageTranslationAlignmentObservation)](imagetranslationalignmentobservation/init(_:).md)
  Creates a translation alignment observation.
### Inspecting an observation
- [let alignmentTransform: CGAffineTransform](imagetranslationalignmentobservation/alignmenttransform.md)
  The alignment transform to align the floating image with the reference image.
### Applying a transform
- [func applyTransform(to: CIImage) -> CIImage](imagetranslationalignmentobservation/applytransform(to:).md)
  Applies the transform to an image.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagetranslationalignmentobservation)*