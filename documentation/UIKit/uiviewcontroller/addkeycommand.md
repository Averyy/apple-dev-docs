# addKeyCommand(_:)

**Framework**: UIKit  
**Kind**: method

Associates the specified keyboard shortcut with the view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addKeyCommand(_ keyCommand: UIKeyCommand)
```

#### Discussion

This method lets you easily add key commands to the view controller without overriding the [`keyCommands`](uiresponder/keycommands.md) property. The key commands you add to a view controller are applied to the active responder chain. When the user performs a key command, UIKit searches the responder chain (starting with the first responder) for an object capable of handling the specified action.

## Parameters

- `keyCommand`: The key command to add.

## See Also

- [var keyCommands: [UIKeyCommand]?](uiresponder/keycommands.md)
  The key commands that trigger actions on this responder.
- [var performsActionsWhilePresentingModally: Bool](uiviewcontroller/performsactionswhilepresentingmodally.md)
  A Boolean value indicating whether the view controller performs menu-related actions.
- [func removeKeyCommand(UIKeyCommand)](uiviewcontroller/removekeycommand(_:).md)
  Removes the key command from the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/addkeycommand(_:))*