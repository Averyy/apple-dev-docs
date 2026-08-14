# HorizonObservation

**Framework**: Vision  
**Kind**: struct

The horizon angle information that an image-analysis request detects.

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
struct HorizonObservation
```

#### Overview

Instances of this class result from invoking a [`DetectHorizonRequest`](detecthorizonrequest.md), and report the angle and transform of the horizon in an image.

## Topics

### Creating an observation
- [init(VNHorizonObservation)](horizonobservation/init(_:).md)
  Creates a horizon observation.
### Inspecting an observation
- [let angle: Measurement<UnitAngle>](horizonobservation/angle.md)
  The angle of the observed horizon.
### Getting the transform
- [let transform: CGAffineTransform](horizonobservation/transform.md)
  The transform to apply to the detected horizon.
- [func transform(for: CGSize) -> CGAffineTransform](horizonobservation/transform(for:).md)
  Creates an affine transform for the specified image width and height.

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/horizonobservation)*