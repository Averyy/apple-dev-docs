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

## See Also

- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagetranslationalignmentobservation)*