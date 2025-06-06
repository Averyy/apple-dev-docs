# buildMenu(with:)

**Framework**: UIKit  
**Kind**: method

Asks the receiving responder to add and remove items from a menu system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func buildMenu(with builder: any UIMenuBuilder)
```

#### Discussion

Override this method in your app delegate or view controller to receive a [`UIMenuBuilder`](uimenubuilder.md) object. Use the builder to add and remove [`UIMenuElement`](uimenuelement.md) objects such as [`UIMenu`](uimenu.md), [`UIAction`](uiaction.md), and [`UICommand`](uicommand.md) from your app’s menu bar or context menus.

> **Note**:  The menu bar is available in Mac apps built with Mac Catalyst.

 The menu bar is available in Mac apps built with Mac Catalyst.

Where you override this method determines the menu system that the builder updates. To add and remove items from the menu bar using the [`main`](uimenusystem/main.md) menu system, override [`buildMenu(with:)`](uiresponder/buildmenu(with:).md) in your app delegate. To build a [`context`](uimenusystem/context.md) menu using the context system, override this method in your view controller.

## Parameters

- `builder`: An object that you use to modify a menu system for your app.

## See Also

- [func validate(UICommand)](uiresponder/validate(_:).md)
  Asks the receiving responder to validate the command.
- [func canPerformAction(Selector, withSender: Any?) -> Bool](uiresponder/canperformaction(_:withsender:).md)
  Requests the receiving responder to enable or disable the specified command in the user interface.
- [func target(forAction: Selector, withSender: Any?) -> Any?](uiresponder/target(foraction:withsender:).md)
  Returns the target object that responds to an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/buildmenu(with:))*