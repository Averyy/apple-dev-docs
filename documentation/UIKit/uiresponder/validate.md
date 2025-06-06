# validate(_:)

**Framework**: UIKit  
**Kind**: method

Asks the receiving responder to validate the command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func validate(_ command: UICommand)
```

#### Discussion

Override this method in your view controller to make changes to a command before the command system renders it as a menu item.

## Parameters

- `command`: A mutable command object.

## See Also

- [func buildMenu(with: any UIMenuBuilder)](uiresponder/buildmenu(with:).md)
  Asks the receiving responder to add and remove items from a menu system.
- [func canPerformAction(Selector, withSender: Any?) -> Bool](uiresponder/canperformaction(_:withsender:).md)
  Requests the receiving responder to enable or disable the specified command in the user interface.
- [func target(forAction: Selector, withSender: Any?) -> Any?](uiresponder/target(foraction:withsender:).md)
  Returns the target object that responds to an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/validate(_:))*