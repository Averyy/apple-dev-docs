# addAction(handler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds an action with the specified handler to the UI update link.

**Availability**:
- iOS
- iPadOS
- tvOS
- visionOS

## Declaration

```swift
func addAction(handler: @escaping (UIUpdateLink, UIUpdateInfo) -> Void)
```

```objc
- (void) addActionWithHandler:(void (^)(UIUpdateLink *updateLink, UIUpdateInfo *updateInfo)) handler;
```

## Discussion

This method adds the action to the [`beforeCADisplayLinkDispatch`](../uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [`addAction(to:handler:)`](./addaction%28to,handler%29.md) instead.

## See Also

### Adding actions
- [func addAction(to: UIUpdateActionPhase, handler: (UIUpdateLink, UIUpdateInfo) -> Void)](./addaction%28to,handler%29.md)
  Adds an action with the specified handler to the UI update link for a particular UI update phase.
- [func addAction(target: Any, selector: Selector)](./addaction%28target,selector%29.md)
  Adds an action with the specified target and selector to the UI update link.
- [func addAction(to: UIUpdateActionPhase, target: Any, selector: Selector)](./addaction%28to,target,selector%29.md)
  Adds an action with the specified target and selector to the UI update link for a particular UI update phase.
- [class UIUpdateActionPhase](../uiupdateactionphase.md)
  An object that defines specific phases of the UI update process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(handler:))*