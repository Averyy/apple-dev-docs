# VNHorizonObservation

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNHorizonObservation : VNObservation
```

## Overview

Instances of this class result from invoking a [`VNDetectHorizonRequest`](./vndetecthorizonrequest.md), and report the [`angle`](./vnhorizonobservation/angle.md) and [`transform`](./vnhorizonobservation/transform.md) of the horizon in an image.

## Topics

### Evaluating the Horizon
- [var angle: CGFloat](./vnhorizonobservation/angle.md)
  The angle of the observed horizon.
- [var transform: CGAffineTransform](./vnhorizonobservation/transform.md)
  The transform to apply to the detected horizon.
- [func transform(forImageWidth: Int, height: Int) -> CGAffineTransform](./vnhorizonobservation/transform%28forimagewidth,height%29.md)
  Creates an affine transform for the specified image width and height.

## Relationships

### Inherits From
- [VNObservation](./vnobservation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [VNRequestRevisionProviding](./vnrequestrevisionproviding.md)

## See Also

### Horizon detection
- [class VNDetectHorizonRequest](./vndetecthorizonrequest.md)
  An image-analysis request that determines the horizon angle in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhorizonobservation)*