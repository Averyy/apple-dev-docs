# UITouch.TouchType

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### Touch types
- [UITouch.TouchType.direct](uitouch/touchtype/direct.md)
  A touch resulting from direct contact with the screen.
- [UITouch.TouchType.indirect](uitouch/touchtype/indirect.md)
  A touch that doesn’t result from contact with the screen.
- [UITouch.TouchType.pencil](uitouch/touchtype/pencil.md)
  A touch from Apple Pencil.
- [UITouch.TouchType.indirectPointer](uitouch/touchtype/indirectpointer.md)
  A touch resulting from a button-based, indirect input device that describes the input sequence from button press to button release.
### Deprecated
- [static var stylus: UITouch.TouchType](uitouch/touchtype/stylus.md)
  A touch from a stylus.
### Initializers
- [init?(rawValue: Int)](uitouch/touchtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var tapCount: Int](uitouch/tapcount.md)
  The number of times the finger was tapped for this given touch.
- [var timestamp: TimeInterval](uitouch/timestamp.md)
  The time when the touch occurred or when it was last mutated.
- [var type: UITouch.TouchType](uitouch/type.md)
  The type of the touch.
- [var phase: UITouch.Phase](uitouch/phase-swift.property.md)
  The phase of the touch.
- [UITouch.Phase](uitouch/phase-swift.enum.md)
  The phase of a touch event.
- [var force: CGFloat](uitouch/force.md)
  The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [var maximumPossibleForce: CGFloat](uitouch/maximumpossibleforce.md)
  The maximum possible force for a touch.
- [var altitudeAngle: CGFloat](uitouch/altitudeangle.md)
  The altitude (in radians) of the stylus.
- [func azimuthAngle(in: UIView?) -> CGFloat](uitouch/azimuthangle(in:).md)
  Returns the azimuth angle (in radians) of the stylus.
- [func azimuthUnitVector(in: UIView?) -> CGVector](uitouch/azimuthunitvector(in:).md)
  Returns a unit vector that points in the direction of the azimuth of the stylus.
- [var rollAngle: CGFloat](uitouch/rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/touchtype)*