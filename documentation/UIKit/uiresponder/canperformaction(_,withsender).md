# canPerformAction(_:withSender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Requests the receiving responder to enable or disable the specified command in the user interface.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool
```

```objc
- (BOOL) canPerformAction:(SEL) action withSender:(id) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if the command identified by `action` should be enabled or [`false`](../../Swift/false.md) if it should be disabled. Returning [`true`](../../Swift/true.md) means that your class can handle the command in the current context.

#### Discussion

This default implementation of this method returns [`true`](../../Swift/true.md) if the responder class implements the requested action and calls the next responder if it doesn’t. Subclasses may override this method to enable menu commands based on the current state; for example, you would enable the Copy command if there’s a selection or disable the Paste command if the pasteboard didn’t contain data with the correct pasteboard representation type. If no responder in the responder chain returns [`true`](../../Swift/true.md), the menu command is disabled. Note that if your class returns [`false`](../../Swift/false.md) for a command, another responder further up the responder chain may still return [`true`](../../Swift/true.md), enabling the command.

This method might be called more than once for the same action but with a different sender each time. You should be prepared for any kind of sender including `nil`.

For information on the editing menu, see the description of the [`UIMenuController`](../uimenucontroller.md) class.

## Parameters

- `action`: A selector that identifies a method associated with a command. For the editing menu, this is one of the editing methods declared by the UIResponderStandardEditActions informal protocol (for example, `copy:`).
- `sender`: The object calling this method. For the editing menu commands, this is the shared [`UIApplication`](../uiapplication.md) object. Depending on the context, you can query the sender for information to help you determine whether a command should be enabled.

## See Also

### Building and validating commands
- [func buildMenu(with: any UIMenuBuilder)](./buildmenu%28with%29.md)
  Asks the receiving responder to add and remove items from a menu system.
- [func validate(UICommand)](./validate%28_%29.md)
  Asks the receiving responder to validate the command.
- [func target(forAction: Selector, withSender: Any?) -> Any?](./target%28foraction,withsender%29.md)
  Returns the target object that responds to an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/canperformaction(_:withsender:))*