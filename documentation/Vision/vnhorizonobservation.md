# VNHorizonObservation

**Framework**: Vision  
**Kind**: class

The horizon angle information that an image-analysis request detects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNHorizonObservation
```

#### Overview

Instances of this class result from invoking a [`VNDetectHorizonRequest`](vndetecthorizonrequest.md), and report the [`angle`](vnhorizonobservation/angle.md) and [`transform`](vnhorizonobservation/transform.md) of the horizon in an image.

## Topics

### Evaluating the Horizon
- [var angle: CGFloat](vnhorizonobservation/angle.md)
  The angle of the observed horizon.
- [var transform: CGAffineTransform](vnhorizonobservation/transform.md)
  The transform to apply to the detected horizon.
- [func transform(forImageWidth: Int, height: Int) -> CGAffineTransform](vnhorizonobservation/transform(forimagewidth:height:).md)
  Creates an affine transform for the specified image width and height.

## Relationships

### Inherits From
- [VNObservation](vnobservation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [class VNDetectHorizonRequest](vndetecthorizonrequest.md)
  An image-analysis request that determines the horizon angle in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhorizonobservation)*