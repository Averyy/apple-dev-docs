# init(view:actionTarget:selector:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a UI update link for the specified view using the specified target and action.

**Availability**:
- iOS
- iPadOS
- tvOS
- visionOS

## Declaration

```swift
init(view: UIView, actionTarget target: Any, selector: Selector)
```

```objc
+ (UIUpdateLink *) updateLinkForView:(UIView *) view actionTarget:(id) target selector:(SEL) selector;
```

## Discussion

This initializer adds the action to the [`beforeCADisplayLinkDispatch`](../uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [`addAction(to:handler:)`](./addaction%28to,handler%29.md) or [`addAction(to:target:selector:)`](./addaction%28to,target,selector%29.md) instead.

## See Also

### Creating a UI update link
- [init(view: UIView)](./init%28view%29.md)
  Creates a UI update link for the specified view.
- [init(view: UIView, actionHandler: (UIUpdateLink, UIUpdateInfo) -> Void)](./init%28view,actionhandler%29.md)
  Creates a UI update link for the specified view using the specified action handler.
- [init(windowScene: UIWindowScene)](./init%28windowscene%29.md)
  Creates a UI update link for the specified window.
- [init(windowScene: UIWindowScene, actionHandler: (UIUpdateLink, UIUpdateInfo) -> Void)](./init%28windowscene,actionhandler%29.md)
  Creates a UI update link for the specified window using the specified action handler.
- [init(windowScene: UIWindowScene, actionTarget: Any, selector: Selector)](./init%28windowscene,actiontarget,selector%29.md)
  Creates a UI update link for the specified window using the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/init(view:actiontarget:selector:))*