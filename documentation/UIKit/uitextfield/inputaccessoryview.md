# inputAccessoryView

**Framework**: UIKit  
**Kind**: property

The custom accessory view to display when the text field becomes the first responder.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var inputAccessoryView: UIView? { get set }
```

#### Discussion

The default value of this property is `nil`. Assigning a view to this property causes that view to be displayed above the standard system keyboard (or above the custom input view if one is provided) when the text field becomes the first responder. For example, you could use this property to attach a custom toolbar to the keyboard.

## See Also

- [var inputView: UIView?](uitextfield/inputview.md)
  The custom input view to display when the text field becomes the first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfield/inputaccessoryview)*