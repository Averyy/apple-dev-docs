# ImageHomographicAlignmentObservation

**Framework**: Vision  
**Kind**: struct

An object that represents a perspective warp transformation.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagehomographicalignmentobservation)*