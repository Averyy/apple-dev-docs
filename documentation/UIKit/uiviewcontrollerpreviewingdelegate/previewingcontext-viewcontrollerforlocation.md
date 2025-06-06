# previewingContext(_:viewControllerForLocation:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Called when the user has pressed a source view in a previewing view controller, thereby obtaining a surrounding blur to indicate that a preview (peek) is available.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func previewingContext(_ previewingContext: any UIViewControllerPreviewing, viewControllerForLocation location: CGPoint) -> UIViewController?
```

#### Return Value

The view controller whose view you want to provide as the preview (peek), or `nil` to disable preview..

#### Discussion

Implement this method to return the preview view controller.

To indicate that a particular portion of the source view is responding to the user’s force touch, set the context object’s [`sourceRect`](uiviewcontrollerpreviewing/sourcerect.md) property to the desired rectangle. For example, if the context object’s [`sourceView`](uiviewcontrollerpreviewing/sourceview.md) property is a table view, you can set the [`sourceRect`](uiviewcontrollerpreviewing/sourcerect.md) property to the frame of the row indicated by the `location` parameter’s value. When the system presents the preview (peek), it appears to originate from the selected row.

You can disable preview by returning `nil` from this method.

## Parameters

- `previewingContext`: The context object for the previewing view controller.
- `location`: The location of the touch in the source view’s coordinate system.

## See Also

- [func previewingContext(any UIViewControllerPreviewing, commit: UIViewController)](uiviewcontrollerpreviewingdelegate/previewingcontext(_:commit:).md)
  Called to let you prepare the presentation of a commit (pop) view from your commit view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate/previewingcontext(_:viewcontrollerforlocation:))*