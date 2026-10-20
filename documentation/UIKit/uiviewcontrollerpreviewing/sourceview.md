# sourceView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: For more information, see [`UIViewControllerPreviewing`](../uiviewcontrollerpreviewing.md).

## Declaration

```swift
var sourceView: UIView { get }
```

```objc
@property (nonatomic, readonly) UIView * sourceView;
```

#### Discussion

Set the value of this property when you register a view controller to participate in 3D Touch. Do this in the view controller’s [`registerForPreviewing(with:sourceView:)`](../uiviewcontroller/registerforpreviewing%28with,sourceview%29.md) method.

When the user begins to press on the source view, the system blurs the surrounding area to let the user know that a preview (peek) is available. At this time, the system calls your [`previewingContext(_:viewControllerForLocation:)`](../uiviewcontrollerpreviewingdelegate/previewingcontext%28_,viewcontrollerforlocation%29.md) method to let you prepare the presentation of a preview. If the user presses more deeply, the system presents the preview defined in your delegate method.

If the user presses deeper on the preview, the system navigates to the view you’ve specified in your [`previewingContext(_:commit:)`](../uiviewcontrollerpreviewingdelegate/previewingcontext%28_,commit%29.md) method. The commit view then fills the bounds of the app’s window.

## See Also

### Related Documentation
- [var sourceRect: CGRect](./sourcerect.md)
  The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.
### Deprecated
- [var sourceRect: CGRect](./sourcerect.md)
  The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.
- [var previewingGestureRecognizerForFailureRelationship: UIGestureRecognizer](./previewinggesturerecognizerforfailurerelationship.md)
  A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures.
- [var delegate: any UIViewControllerPreviewingDelegate](./delegate.md)
  The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/sourceview)*