# addAction(handler:)

**Framework**: UIKit  
**Kind**: method

Adds an action with the specified handler to the UI update link.

**Availability**:
- iOS ?+
- iPadOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func addAction(handler: @escaping (UIUpdateLink, UIUpdateInfo) -> Void)
```

#### Discussion

This method adds the action to the [`beforeCADisplayLinkDispatch`](uiupdateactionphase/beforecadisplaylinkdispatch.md) phase. To specify a different phase, use [`addAction(to:handler:)`](uiupdatelink/addaction(to:handler:).md) instead.

## See Also

- [func addAction(to: UIUpdateActionPhase, handler: (UIUpdateLink, UIUpdateInfo) -> Void)](uiupdatelink/addaction(to:handler:).md)
  Adds an action with the specified handler to the UI update link for a particular UI update phase.
- [func addAction(target: Any, selector: Selector)](uiupdatelink/addaction(target:selector:).md)
  Adds an action with the specified target and selector to the UI update link.
- [func addAction(to: UIUpdateActionPhase, target: Any, selector: Selector)](uiupdatelink/addaction(to:target:selector:).md)
  Adds an action with the specified target and selector to the UI update link for a particular UI update phase.
- [class UIUpdateActionPhase](uiupdateactionphase.md)
  An object that defines specific phases of the UI update process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(handler:))*