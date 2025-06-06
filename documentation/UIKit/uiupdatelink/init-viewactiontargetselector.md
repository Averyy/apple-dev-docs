# init(view:actionTarget:selector:)

**Framework**: UIKit  
**Kind**: init

Creates a UI update link for the specified view using the specified target and action.

**Availability**:
- iOS ?+
- iPadOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
init(view: UIView, actionTarget target: Any, selector: Selector)
```

#### Discussion

This initializer adds the action to the [`beforeCADisplayLinkDispatch`](uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [`addAction(to:handler:)`](uiupdatelink/addaction(to:handler:).md) or [`addAction(to:target:selector:)`](uiupdatelink/addaction(to:target:selector:).md) instead.

## See Also

- [init(view: UIView)](uiupdatelink/init(view:).md)
  Creates a UI update link for the specified view.
- [init(view: UIView, actionHandler: (UIUpdateLink, UIUpdateInfo) -> Void)](uiupdatelink/init(view:actionhandler:).md)
  Creates a UI update link for the specified view using the specified action handler.
- [init(windowScene: UIWindowScene)](uiupdatelink/init(windowscene:).md)
  Creates a UI update link for the specified window.
- [init(windowScene: UIWindowScene, actionHandler: (UIUpdateLink, UIUpdateInfo) -> Void)](uiupdatelink/init(windowscene:actionhandler:).md)
  Creates a UI update link for the specified window using the specified action handler.
- [init(windowScene: UIWindowScene, actionTarget: Any, selector: Selector)](uiupdatelink/init(windowscene:actiontarget:selector:).md)
  Creates a UI update link for the specified window using the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/init(view:actiontarget:selector:))*