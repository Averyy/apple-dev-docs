# init(windowScene:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a UI update link for the specified window.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(windowScene: UIWindowScene)
```

```objc
+ (UIUpdateLink *) updateLinkForWindowScene:(UIWindowScene *) windowScene;
```

## See Also

### Creating a UI update link
- [init(view: UIView)](./init%28view%29.md)
  Creates a UI update link for the specified view.
- [init(view: UIView, actionHandler: (UIUpdateLink, UIUpdateInfo) -> Void)](./init%28view,actionhandler%29.md)
  Creates a UI update link for the specified view using the specified action handler.
- [init(view: UIView, actionTarget: Any, selector: Selector)](./init%28view,actiontarget,selector%29.md)
  Creates a UI update link for the specified view using the specified target and action.
- [init(windowScene: UIWindowScene, actionHandler: (UIUpdateLink, UIUpdateInfo) -> Void)](./init%28windowscene,actionhandler%29.md)
  Creates a UI update link for the specified window using the specified action handler.
- [init(windowScene: UIWindowScene, actionTarget: Any, selector: Selector)](./init%28windowscene,actiontarget,selector%29.md)
  Creates a UI update link for the specified window using the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/init(windowscene:))*