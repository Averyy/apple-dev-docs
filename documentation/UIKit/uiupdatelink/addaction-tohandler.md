# addAction(to:handler:)

**Framework**: UIKit  
**Kind**: method

Adds an action with the specified handler to the UI update link for a particular UI update phase.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func addAction(to phase: UIUpdateActionPhase, handler: @escaping (UIUpdateLink, UIUpdateInfo) -> Void)
```

## See Also

- [func addAction(handler: (UIUpdateLink, UIUpdateInfo) -> Void)](uiupdatelink/addaction(handler:).md)
  Adds an action with the specified handler to the UI update link.
- [func addAction(target: Any, selector: Selector)](uiupdatelink/addaction(target:selector:).md)
  Adds an action with the specified target and selector to the UI update link.
- [func addAction(to: UIUpdateActionPhase, target: Any, selector: Selector)](uiupdatelink/addaction(to:target:selector:).md)
  Adds an action with the specified target and selector to the UI update link for a particular UI update phase.
- [class UIUpdateActionPhase](uiupdateactionphase.md)
  An object that defines specific phases of the UI update process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiupdatelink/addaction(to:handler:))*