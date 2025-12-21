# ImageHomographicAlignmentObservation

**Framework**: Vision  
**Kind**: struct

An object that represents a perspective warp transformation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct ImageHomographicAlignmentObservation
```

#### Overview

This type of observation results from a [`TrackHomographicImageRegistrationRequest`](trackhomographicimageregistrationrequest.md), informing the [`warpTransform`](imagehomographicalignmentobservation/warptransform.md) performed to align the input images.

## Topics

### Creating an observation
- [init(VNImageHomographicAlignmentObservation)](imagehomographicalignmentobservation/init(_:).md)
  Creates a homographic alignment observation.
### Inspecting an observation
- [let warpTransform: matrix_float3x3](imagehomographicalignmentobservation/warptransform.md)
  The warp transform matrix to morph the floating image into the reference image.
### Applying a transform
- [func applyTransform(to: CIImage) -> CIImage](imagehomographicalignmentobservation/applytransform(to:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagehomographicalignmentobservation)*