# inputView

**Framework**: UIKit  
**Kind**: property

The custom input view to display when the text view becomes the first responder.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var inputView: UIView? { get set }
```

#### Discussion

If the value in this property is `nil`, the text view displays the standard system keyboard when it becomes first responder. Assigning a custom view to this property causes that view to be presented instead.

The default value of this property is `nil`.

## See Also

- [var inputAccessoryView: UIView?](uitextview/inputaccessoryview.md)
  The custom accessory view to display when the text view becomes the first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/inputview)*