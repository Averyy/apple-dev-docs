# sourceView

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var sourceView: UIView { get }
```

#### Discussion

Set the value of this property when you register a view controller to participate in 3D Touch. Do this in the view controller’s [`registerForPreviewing(with:sourceView:)`](uiviewcontroller/registerforpreviewing(with:sourceview:).md) method.

When the user begins to press on the source view, the system blurs the surrounding area to let the user know that a preview (peek) is available. At this time, the system calls your [`previewingContext(_:viewControllerForLocation:)`](uiviewcontrollerpreviewingdelegate/previewingcontext(_:viewcontrollerforlocation:).md) method to let you prepare the presentation of a preview. If the user presses more deeply, the system presents the preview defined in your delegate method.

If the user presses deeper on the preview, the system navigates to the view you’ve specified in your [`previewingContext(_:commit:)`](uiviewcontrollerpreviewingdelegate/previewingcontext(_:commit:).md) method. The commit view then fills the bounds of the app’s window.

## See Also

- [var sourceRect: CGRect](uiviewcontrollerpreviewing/sourcerect.md)
  The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.
- [var delegate: any UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewing/delegate.md)
  The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/sourceview)*