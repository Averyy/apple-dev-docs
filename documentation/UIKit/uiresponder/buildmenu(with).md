# buildMenu(with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the receiving responder to add and remove items from a menu system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func buildMenu(with builder: any UIMenuBuilder)
```

```objc
- (void) buildMenuWithBuilder:(id<UIMenuBuilder>) builder;
```

#### Discussion

Override this method in your app delegate or view controller to receive a [`UIMenuBuilder`](../uimenubuilder.md) object. Use the builder to add and remove [`UIMenuElement`](../uimenuelement.md) objects such as [`UIMenu`](../uimenu.md), [`UIAction`](../uiaction.md), and [`UICommand`](../uicommand.md) from your app’s menu bar or context menus.

> **Note**:  The menu bar is available in Mac apps built with Mac Catalyst.

Where you override this method determines the menu system that the builder updates. To add and remove items from the menu bar using the [`main`](../uimenusystem/main.md) menu system, override [`buildMenu(with:)`](./buildmenu%28with%29.md) in your app delegate. To build a [`context`](../uimenusystem/context.md) menu using the context system, override this method in your view controller.

## Parameters

- `builder`: An object that you use to modify a menu system for your app.

## See Also

### Building and validating commands
- [func validate(UICommand)](./validate%28_%29.md)
  Asks the receiving responder to validate the command.
- [func canPerformAction(Selector, withSender: Any?) -> Bool](./canperformaction%28_,withsender%29.md)
  Requests the receiving responder to enable or disable the specified command in the user interface.
- [func target(forAction: Selector, withSender: Any?) -> Any?](./target%28foraction,withsender%29.md)
  Returns the target object that responds to an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/buildmenu(with:))*