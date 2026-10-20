# addAction(to:target:selector:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds an action with the specified target and selector to the UI update link for a particular UI update phase.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func addAction(to phase: UIUpdateActionPhase, target: Any, selector: Selector)
```

```objc
- (void) addActionToPhase:(UIUpdateActionPhase *) phase target:(id) target selector:(SEL) selector;
```

## See Also

### Adding actions
- [func addAction(handler: (UIUpdateLink, UIUpdateInfo) -> Void)](./addaction%28handler%29.md)
  Adds an action with the specified handler to the UI update link.
- [func addAction(to: UIUpdateActionPhase, handler: (UIUpdateLink, UIUpdateInfo) -> Void)](./addaction%28to,handler%29.md)
  Adds an action with the specified handler to the UI update link for a particular UI update phase.
- [func addAction(target: Any, selector: Selector)](./addaction%28target,selector%29.md)
  Adds an action with the specified target and selector to the UI update link.
- [class UIUpdateActionPhase](../uiupdateactionphase.md)
  An object that defines specific phases of the UI update process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(to:target:selector:))*