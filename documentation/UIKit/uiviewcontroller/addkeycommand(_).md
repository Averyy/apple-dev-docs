# addKeyCommand(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Associates the specified keyboard shortcut with the view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addKeyCommand(_ keyCommand: UIKeyCommand)
```

```objc
- (void) addKeyCommand:(UIKeyCommand *) keyCommand;
```

## Discussion

This method lets you easily add key commands to the view controller without overriding the [`keyCommands`](../uiresponder/keycommands.md) property. The key commands you add to a view controller are applied to the active responder chain. When the user performs a key command, UIKit searches the responder chain (starting with the first responder) for an object capable of handling the specified action.

## Parameters

- `keyCommand`: The key command to add.

## See Also

### Related Documentation
- [var keyCommands: [UIKeyCommand]?](../uiresponder/keycommands.md)
  The key commands that trigger actions on this responder.
### Accessing the available key commands
- [var performsActionsWhilePresentingModally: Bool](./performsactionswhilepresentingmodally.md)
  A Boolean value indicating whether the view controller performs menu-related actions.
- [func removeKeyCommand(UIKeyCommand)](./removekeycommand%28_%29.md)
  Removes the key command from the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/addkeycommand(_:))*