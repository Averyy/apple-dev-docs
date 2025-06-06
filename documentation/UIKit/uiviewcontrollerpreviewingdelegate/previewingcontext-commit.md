# previewingContext(_:commit:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Called to let you prepare the presentation of a commit (pop) view from your commit view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func previewingContext(_ previewingContext: any UIViewControllerPreviewing, commit viewControllerToCommit: UIViewController)
```

#### Discussion

Implement this method to configure and present the commit (pop) view controller, in a way that is appropriate for your app.

For example, to present the commit view controller’s view in a navigation controller, call the navigation controller’s [`show(_:sender:)`](uinavigationcontroller/show(_:sender:).md) method; to present the view modally, you could call the [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method.

## Parameters

- `previewingContext`: The context object for the previewing view controller.
- `viewControllerToCommit`: The view controller whose view your implementation of this method is moving into place as a commit (pop) view.

## See Also

- [func previewingContext(any UIViewControllerPreviewing, viewControllerForLocation: CGPoint) -> UIViewController?](uiviewcontrollerpreviewingdelegate/previewingcontext(_:viewcontrollerforlocation:).md)
  Called when the user has pressed a source view in a previewing view controller, thereby obtaining a surrounding blur to indicate that a preview (peek) is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate/previewingcontext(_:commit:))*