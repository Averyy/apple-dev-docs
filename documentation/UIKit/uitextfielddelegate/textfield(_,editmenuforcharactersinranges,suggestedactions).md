# textField(_:editMenuForCharactersInRanges:suggestedActions:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional func textField(_ textField: UITextField, editMenuForCharactersInRanges ranges: [NSValue], suggestedActions: [UIMenuElement]) -> UIMenu?
```

```objc
- (UIMenu *) textField:(UITextField *) textField editMenuForCharactersInRanges:(NSArray<NSValue *> *) ranges suggestedActions:(NSArray<UIMenuElement *> *) suggestedActions;
```

## Return Value

Return a UIMenu describing the desired menu hierarchy. Return @c nil to present the default system menu.

## Discussion

Asks the delegate for the menu to be shown for the specified `ranges`.

## Parameters

- `textField`: The text field requesting the menu.
- `ranges`: The text ranges for which the menu is presented for.
- `suggestedActions`: The actions and commands that the system suggests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:editmenuforcharactersinranges:suggestedactions:))*