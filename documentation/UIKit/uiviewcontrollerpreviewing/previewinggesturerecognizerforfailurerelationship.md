# previewingGestureRecognizerForFailureRelationship

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var previewingGestureRecognizerForFailureRelationship: UIGestureRecognizer { get }
```

#### Discussion

Use this gesture recognizer by implementing a delegate object for it that conforms to the [`UIGestureRecognizerDelegate`](uigesturerecognizerdelegate.md) protocol. The protocol methods let you prevent a preview (peek) press from interfering with an app’s other supported gestures. For example, you could delay a preview’s presentation until after other gestures fail, or you could allow simultaneous recognition of a press and other gestures during a preview’s presentation.

For more information, see the [`gestureRecognizer(_:shouldBeRequiredToFailBy:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:).md) and [`gestureRecognizer(_:shouldRequireFailureOf:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md) methods in [`UIGestureRecognizerDelegate`](uigesturerecognizerdelegate.md).

## See Also

- [var sourceRect: CGRect](uiviewcontrollerpreviewing/sourcerect.md)
  The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/previewinggesturerecognizerforfailurerelationship)*