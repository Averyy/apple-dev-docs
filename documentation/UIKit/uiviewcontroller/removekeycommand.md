# removeKeyCommand(_:)

**Framework**: UIKit  
**Kind**: method

Removes the key command from the view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeKeyCommand(_ keyCommand: UIKeyCommand)
```

#### Discussion

This method lets you easily remove key commands without overriding the [`keyCommands`](uiresponder/keycommands.md) property.

## Parameters

- `keyCommand`: The key command to remove.

## See Also

- [var keyCommands: [UIKeyCommand]?](uiresponder/keycommands.md)
  The key commands that trigger actions on this responder.
- [var performsActionsWhilePresentingModally: Bool](uiviewcontroller/performsactionswhilepresentingmodally.md)
  A Boolean value indicating whether the view controller performs menu-related actions.
- [func addKeyCommand(UIKeyCommand)](uiviewcontroller/addkeycommand(_:).md)
  Associates the specified keyboard shortcut with the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/removekeycommand(_:))*