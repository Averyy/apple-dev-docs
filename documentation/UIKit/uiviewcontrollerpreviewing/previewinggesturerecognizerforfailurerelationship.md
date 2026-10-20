# previewingGestureRecognizerForFailureRelationship

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: For more information, see [`UIViewControllerPreviewing`](../uiviewcontrollerpreviewing.md).

## Declaration

```swift
var previewingGestureRecognizerForFailureRelationship: UIGestureRecognizer { get }
```

```objc
@property (nonatomic, readonly) UIGestureRecognizer * previewingGestureRecognizerForFailureRelationship;
```

#### Discussion

Use this gesture recognizer by implementing a delegate object for it that conforms to the [`UIGestureRecognizerDelegate`](../uigesturerecognizerdelegate.md) protocol. The protocol methods let you prevent a preview (peek) press from interfering with an app’s other supported gestures. For example, you could delay a preview’s presentation until after other gestures fail, or you could allow simultaneous recognition of a press and other gestures during a preview’s presentation.

For more information, see the [`gestureRecognizer(_:shouldBeRequiredToFailBy:)`](../uigesturerecognizerdelegate/gesturerecognizer%28_,shouldberequiredtofailby%29.md) and [`gestureRecognizer(_:shouldRequireFailureOf:)`](../uigesturerecognizerdelegate/gesturerecognizer%28_,shouldrequirefailureof%29.md) methods in [`UIGestureRecognizerDelegate`](../uigesturerecognizerdelegate.md).

## See Also

### Deprecated
- [var sourceRect: CGRect](./sourcerect.md)
  The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.
- [var delegate: any UIViewControllerPreviewingDelegate](./delegate.md)
  The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers.
- [var sourceView: UIView](./sourceview.md)
  A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/previewinggesturerecognizerforfailurerelationship)*