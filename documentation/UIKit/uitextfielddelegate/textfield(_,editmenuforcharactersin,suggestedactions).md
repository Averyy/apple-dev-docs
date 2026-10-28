# textField(_:editMenuForCharactersIn:suggestedActions:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the menu to display in the text field, based on the text range and actions the system provides.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- Mac Catalyst 16.0+ - Deprecated in 27.2
- tvOS 16.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

## Declaration

```swift
optional func textField(_ textField: UITextField, editMenuForCharactersIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?
```

```objc
- (UIMenu *) textField:(UITextField *) textField editMenuForCharactersInRange:(NSRange) range suggestedActions:(NSArray<UIMenuElement *> *) suggestedActions;
```

## Return Value

Returns a menu describing the desired menu hierarchy. Return `nil` to present the default system menu.

## Discussion

The following example returns a menu that includes a “Show in Large Type” action.

```swift
func textField(_ textField: UITextField, editMenuForCharactersIn range: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu? {
    let showLargeAction = UIAction(title: "Show in Large Type", image: UIImage(systemName: "a.magnify")) { action in
            // Include "Show in Large Type" action.
    }

    var actions = suggestedActions
    actions.append(showLargeAction)
    return UIMenu(children: actions)
}
```

## Parameters

- `textField`: The text field requesting the menu.
- `range`: The character range the menu is presenting for.
- `suggestedActions`: The actions and commands the system suggests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:editmenuforcharactersin:suggestedactions:))*