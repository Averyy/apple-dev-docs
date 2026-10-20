# direction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The permitted direction of the swipe for this gesture recognizer.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var direction: UISwipeGestureRecognizer.Direction { get set }
```

```objc
@property (nonatomic) UISwipeGestureRecognizerDirection direction;
```

## Mentions

- [Handling swipe gestures](../handling-swipe-gestures.md)

#### Discussion

The default direction is [`right`](./direction-swift.struct/right.md). See descriptions of [`UISwipeGestureRecognizer.Direction`](./direction-swift.struct.md) constants for more information.

## See Also

### Related Documentation
- [Event Handling Guide for UIKit Apps](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html#//apple_ref/doc/uid/TP40009541)
### Configuring the gesture
- [var numberOfTouchesRequired: Int](./numberoftouchesrequired.md)
  The number of touches necessary for swipe recognition.
- [UISwipeGestureRecognizer.Direction](./direction-swift.struct.md)
  The direction of the swipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer/direction-swift.property)*