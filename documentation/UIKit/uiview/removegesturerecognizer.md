# removeGestureRecognizer(_:)

**Framework**: UIKit  
**Kind**: method

Detaches a gesture recognizer from the receiving view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)
```

#### Discussion

This method releases `gestureRecognizer` in addition to detaching it from the view.

## Parameters

- `gestureRecognizer`: An object whose class descends from the   class.

## See Also

- [func addGestureRecognizer(UIGestureRecognizer)](uiview/addgesturerecognizer(_:).md)
  Attaches a gesture recognizer to the view.
- [var gestureRecognizers: [UIGestureRecognizer]?](uiview/gesturerecognizers.md)
  The gesture-recognizer objects currently attached to the view.
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](uiview/gesturerecognizershouldbegin(_:).md)
  Asks the view if the gesture recognizer should continue tracking touch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removegesturerecognizer(_:))*