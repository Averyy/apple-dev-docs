# delegate

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var delegate: any UIViewControllerPreviewingDelegate { get }
```

#### Discussion

Set a previewing view controller’s 3D Touch delegate when you register the view controller by calling its [`registerForPreviewing(with:sourceView:)`](uiviewcontroller/registerforpreviewing(with:sourceview:).md) method.

For information on the methods the delegate can implement, read [`UIViewControllerPreviewingDelegate`](uiviewcontrollerpreviewingdelegate.md).

## See Also

- [var sourceView: UIView](uiviewcontrollerpreviewing/sourceview.md)
  A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/delegate)*