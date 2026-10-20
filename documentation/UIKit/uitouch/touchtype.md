# UITouch.TouchType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The type of touch received.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum TouchType
```

```c
enum UITouchType : NSInteger;
```

## Topics

### Touch types
- [UITouch.TouchType.direct](./touchtype/direct.md)
  A touch resulting from direct contact with the screen.
- [UITouch.TouchType.indirect](./touchtype/indirect.md)
  A touch that doesn’t result from contact with the screen.
- [UITouch.TouchType.pencil](./touchtype/pencil.md)
  A touch from Apple Pencil.
- [UITouch.TouchType.indirectPointer](./touchtype/indirectpointer.md)
  A touch resulting from a button-based, indirect input device that describes the input sequence from button press to button release.
### Deprecated
- [static var stylus: UITouch.TouchType](./touchtype/stylus.md)
  A touch from a stylus.
### Initializers
- [init?(rawValue: Int)](./touchtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting touch attributes
- [var tapCount: Int](./tapcount.md)
  The number of times the finger was tapped for this given touch.
- [var timestamp: TimeInterval](./timestamp.md)
  The time when the touch occurred or when it was last mutated.
- [var type: UITouch.TouchType](./type.md)
  The type of the touch.
- [var phase: UITouch.Phase](./phase-swift.property.md)
  The phase of the touch.
- [UITouch.Phase](./phase-swift.enum.md)
  The phase of a touch event.
- [var force: CGFloat](./force.md)
  The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [var maximumPossibleForce: CGFloat](./maximumpossibleforce.md)
  The maximum possible force for a touch.
- [var altitudeAngle: CGFloat](./altitudeangle.md)
  The altitude (in radians) of the stylus.
- [func azimuthAngle(in: UIView?) -> CGFloat](./azimuthangle%28in%29.md)
  Returns the azimuth angle (in radians) of the stylus.
- [func azimuthUnitVector(in: UIView?) -> CGVector](./azimuthunitvector%28in%29.md)
  Returns a unit vector that points in the direction of the azimuth of the stylus.
- [var rollAngle: CGFloat](./rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/touchtype)*