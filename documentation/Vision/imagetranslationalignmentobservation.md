# ImageTranslationAlignmentObservation

**Framework**: Vision  
**Kind**: struct

Affine transform information that an image-alignment request produces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+ (Beta)

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
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagetranslationalignmentobservation)*