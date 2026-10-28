# numberOfTouchesRequired

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number of touches necessary for swipe recognition.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var numberOfTouchesRequired: Int { get set }
```

```objc
@property (nonatomic) NSUInteger numberOfTouchesRequired;
```

## Mentions

- [Handling swipe gestures](../handling-swipe-gestures.md)

## Discussion

The default value is `1`.

## See Also

### Configuring the gesture
- [var direction: UISwipeGestureRecognizer.Direction](./direction-swift.property.md)
  The permitted direction of the swipe for this gesture recognizer.
- [UISwipeGestureRecognizer.Direction](./direction-swift.struct.md)
  The direction of the swipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer/numberoftouchesrequired)*