# gestureRecognizers

**Framework**: UIKit  
**Kind**: property

The gesture-recognizer objects currently attached to the view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var gestureRecognizers: [UIGestureRecognizer]? { get set }
```

#### Discussion

Each of these objects is an instance of a subclass of the abstract base class [`UIGestureRecognizer`](uigesturerecognizer.md). The default value of this property is `nil`. If you add a gesture recognizer and then remove it, the value of the property is an empty array.

## See Also

- [func addGestureRecognizer(UIGestureRecognizer)](uiview/addgesturerecognizer(_:).md)
  Attaches a gesture recognizer to the view.
- [func removeGestureRecognizer(UIGestureRecognizer)](uiview/removegesturerecognizer(_:).md)
  Detaches a gesture recognizer from the receiving view.
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](uiview/gesturerecognizershouldbegin(_:).md)
  Asks the view if the gesture recognizer should continue tracking touch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/gesturerecognizers)*