# addGestureRecognizer(_:)

**Framework**: UIKit  
**Kind**: method

Attaches a gesture recognizer to the view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)
```

## Mentions

- [Handling long-press gestures](handling-long-press-gestures.md)
- [Handling pinch gestures](handling-pinch-gestures.md)
- [Handling swipe gestures](handling-swipe-gestures.md)
- [Handling pan gestures](handling-pan-gestures.md)
- [Handling rotation gestures](handling-rotation-gestures.md)
- [Handling tap gestures](handling-tap-gestures.md)

#### Discussion

Attaching a gesture recognizer to a view defines the scope of the represented gesture, causing it to receive touches hit-tested to that view and all of its subviews. The view establishes a strong reference to the gesture recognizer.

## Parameters

- `gestureRecognizer`: An object whose class descends from the   class. This parameter must not be  .

## See Also

- [func removeGestureRecognizer(UIGestureRecognizer)](uiview/removegesturerecognizer(_:).md)
  Detaches a gesture recognizer from the receiving view.
- [var gestureRecognizers: [UIGestureRecognizer]?](uiview/gesturerecognizers.md)
  The gesture-recognizer objects currently attached to the view.
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](uiview/gesturerecognizershouldbegin(_:).md)
  Asks the view if the gesture recognizer should continue tracking touch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/addgesturerecognizer(_:))*