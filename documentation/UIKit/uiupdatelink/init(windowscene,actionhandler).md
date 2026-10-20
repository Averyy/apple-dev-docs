# init(windowScene:actionHandler:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a UI update link for the specified window using the specified action handler.

**Availability**:
- iOS
- iPadOS
- tvOS
- visionOS

## Declaration

```swift
init(windowScene: UIWindowScene, actionHandler handler: @escaping (UIUpdateLink, UIUpdateInfo) -> Void)
```

```objc
+ (UIUpdateLink *) updateLinkForWindowScene:(UIWindowScene *) windowScene actionHandler:(void (^)(UIUpdateLink *updateLink, UIUpdateInfo *updateInfo)) handler;
```

#### Discussion

This initializer adds the action to the [`beforeCADisplayLinkDispatch`](../uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [`addAction(to:handler:)`](./addaction%28to,handler%29.md) or [`addAction(to:target:selector:)`](./addaction%28to,target,selector%29.md) instead.

## See Also

### Creating a UI update link
- [init(view: UIView)](./init%28view%29.md)
  Creates a UI update link for the specified view.
- [init(view: UIView, actionHandler: (UIUpdateLink, UIUpdateInfo) -> Void)](./init%28view,actionhandler%29.md)
  Creates a UI update link for the specified view using the specified action handler.
- [init(view: UIView, actionTarget: Any, selector: Selector)](./init%28view,actiontarget,selector%29.md)
  Creates a UI update link for the specified view using the specified target and action.
- [init(windowScene: UIWindowScene)](./init%28windowscene%29.md)
  Creates a UI update link for the specified window.
- [init(windowScene: UIWindowScene, actionTarget: Any, selector: Selector)](./init%28windowscene,actiontarget,selector%29.md)
  Creates a UI update link for the specified window using the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/init(windowscene:actionhandler:))*