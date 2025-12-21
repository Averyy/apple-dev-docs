# HorizonObservation

**Framework**: Vision  
**Kind**: struct

The horizon angle information that an image-analysis request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/horizonobservation)*