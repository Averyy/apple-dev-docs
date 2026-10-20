# UISwipeGestureRecognizer.Direction

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The direction of the swipe.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct Direction
```

```c
enum UISwipeGestureRecognizerDirection : NSUInteger;
```

## Topics

### Constants
- [static var right: UISwipeGestureRecognizer.Direction](./direction-swift.struct/right.md)
  The touch or touches swipe to the right.
- [static var left: UISwipeGestureRecognizer.Direction](./direction-swift.struct/left.md)
  The touch or touches swipe to the left.
- [static var up: UISwipeGestureRecognizer.Direction](./direction-swift.struct/up.md)
  The touch or touches swipe upward.
- [static var down: UISwipeGestureRecognizer.Direction](./direction-swift.struct/down.md)
  The touch or touches swipe downward.
### Initializers
- [init(rawValue: UInt)](./direction-swift.struct/init%28rawvalue%29.md)
  Creates a swipe direction structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring the gesture
- [var direction: UISwipeGestureRecognizer.Direction](./direction-swift.property.md)
  The permitted direction of the swipe for this gesture recognizer.
- [var numberOfTouchesRequired: Int](./numberoftouchesrequired.md)
  The number of touches necessary for swipe recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer/direction-swift.struct)*