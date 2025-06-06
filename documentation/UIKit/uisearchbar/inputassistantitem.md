# inputAssistantItem

**Framework**: UIKit  
**Kind**: property

The input assistant to use for configuring the keyboard’s shortcuts bar.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var inputAssistantItem: UITextInputAssistantItem { get }
```

#### Discussion

When search is engaged on iPad, the shortcuts bar above the keyboard contains typing suggestions and may contain other controls for managing text. This property contains the object you use to configure the custom bar button items above the keyboard. The shortcuts bar is not available on iPhone or iPod Touch.

For more information about how to configure shortcut items, see [`UITextInputAssistantItem`](uitextinputassistantitem.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/inputassistantitem)*