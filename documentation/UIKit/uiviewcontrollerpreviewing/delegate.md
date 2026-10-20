# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: For more information, see [`UIViewControllerPreviewing`](../uiviewcontrollerpreviewing.md).

## Declaration

```swift
var delegate: any UIViewControllerPreviewingDelegate { get }
```

```objc
@property (nonatomic, readonly) id<UIViewControllerPreviewingDelegate> delegate;
```

#### Discussion

Set a previewing view controller’s 3D Touch delegate when you register the view controller by calling its [`registerForPreviewing(with:sourceView:)`](../uiviewcontroller/registerforpreviewing%28with,sourceview%29.md) method.

For information on the methods the delegate can implement, read [`UIViewControllerPreviewingDelegate`](../uiviewcontrollerpreviewingdelegate.md).

## See Also

### Deprecated
- [var sourceRect: CGRect](./sourcerect.md)
  The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.
- [var previewingGestureRecognizerForFailureRelationship: UIGestureRecognizer](./previewinggesturerecognizerforfailurerelationship.md)
  A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures.
- [var sourceView: UIView](./sourceview.md)
  A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/delegate)*