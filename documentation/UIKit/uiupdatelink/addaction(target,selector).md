# addAction(target:selector:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds an action with the specified target and selector to the UI update link.

**Availability**:
- iOS
- iPadOS
- tvOS
- visionOS

## Declaration

```swift
func addAction(target: Any, selector: Selector)
```

```objc
- (void) addActionWithTarget:(id) target selector:(SEL) selector;
```

#### Discussion

This method adds the action to the [`beforeCADisplayLinkDispatch`](../uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [`addAction(to:target:selector:)`](./addaction%28to,target,selector%29.md) instead.

## See Also

### Adding actions
- [func addAction(handler: (UIUpdateLink, UIUpdateInfo) -> Void)](./addaction%28handler%29.md)
  Adds an action with the specified handler to the UI update link.
- [func addAction(to: UIUpdateActionPhase, handler: (UIUpdateLink, UIUpdateInfo) -> Void)](./addaction%28to,handler%29.md)
  Adds an action with the specified handler to the UI update link for a particular UI update phase.
- [func addAction(to: UIUpdateActionPhase, target: Any, selector: Selector)](./addaction%28to,target,selector%29.md)
  Adds an action with the specified target and selector to the UI update link for a particular UI update phase.
- [class UIUpdateActionPhase](../uiupdateactionphase.md)
  An object that defines specific phases of the UI update process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(target:selector:))*