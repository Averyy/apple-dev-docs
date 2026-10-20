# inputAssistantItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The input assistant to use when configuring the keyboard’s shortcuts bar.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 2.0+

## Declaration

```swift
var inputAssistantItem: UITextInputAssistantItem { get }
```

```objc
@property (nonatomic, strong, readonly, nonnull) UITextInputAssistantItem * inputAssistantItem;
```

#### Discussion

On iPad, the shortcuts bar above the keyboard contains typing suggestions and other controls for managing text, such as cut, copy, and paste commands. This property contains the text input assistant item you use to configure the custom bar button items that you want included in the shortcuts bar. The shortcuts bar isn’t available on iPhone or iPod Touch.

This property has special considerations in visionOS:

- In apps built for visionOS, this property isn’t available. Use [`bottomOrnament`](../../SwiftUI/toolbaritemplacement/bottomornament.md) instead.
- In compatible iPad apps running in visionOS, the shortcuts bar behaves similar to iPadOS. It contains the custom bar button items you configure using this property and system items (such as cut, copy, and paste). The shortcuts bar renders at the bottom of the app window, but it doesn’t anchor to the keyboard in visionOS.

## See Also

### Managing the text input mode
- [var textInputMode: UITextInputMode?](./textinputmode.md)
  The text input mode for this responder object.
- [var textInputContextIdentifier: String?](./textinputcontextidentifier.md)
  An identifier signifying that the responder should preserve its text input mode information.
- [class func clearTextInputContextIdentifier(String)](./cleartextinputcontextidentifier%28_%29.md)
  Clears text input mode information from the app’s user defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/inputassistantitem)*