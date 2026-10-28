# validate(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the receiving responder to validate the command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func validate(_ command: UICommand)
```

```objc
- (void) validateCommand:(UICommand *) command;
```

## Discussion

Override this method in your view controller to make changes to a command before the command system renders it as a menu item.

## Parameters

- `command`: A mutable command object.

## See Also

### Building and validating commands
- [func buildMenu(with: any UIMenuBuilder)](./buildmenu%28with%29.md)
  Asks the receiving responder to add and remove items from a menu system.
- [func canPerformAction(Selector, withSender: Any?) -> Bool](./canperformaction%28_,withsender%29.md)
  Requests the receiving responder to enable or disable the specified command in the user interface.
- [func target(forAction: Selector, withSender: Any?) -> Any?](./target%28foraction,withsender%29.md)
  Returns the target object that responds to an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/validate(_:))*