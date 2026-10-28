# removeGestureRecognizer(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Detaches a gesture recognizer from the receiving view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)
```

```objc
- (void) removeGestureRecognizer:(UIGestureRecognizer *) gestureRecognizer;
```

## Discussion

This method releases `gestureRecognizer` in addition to detaching it from the view.

## Parameters

- `gestureRecognizer`: An object whose class descends from the [`UIGestureRecognizer`](../uigesturerecognizer.md) class.

## See Also

### Managing gesture recognizers
- [func addGestureRecognizer(UIGestureRecognizer)](./addgesturerecognizer%28_%29.md)
  Attaches a gesture recognizer to the view.
- [var gestureRecognizers: [UIGestureRecognizer]?](./gesturerecognizers.md)
  The gesture-recognizer objects currently attached to the view.
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](./gesturerecognizershouldbegin%28_%29.md)
  Asks the view if the gesture recognizer should continue tracking touch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removegesturerecognizer(_:))*