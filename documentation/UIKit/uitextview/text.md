# text

**Framework**: UIKit  
**Kind**: property

The text that the text view displays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var text: String! { get set }
```

#### Discussion

In iOS 6 and later, assigning a new value to this property also replaces the value of the [`attributedText`](uitextview/attributedtext.md) property with the same text, albeit without any inherent style attributes. Instead the text view styles the new string using the [`font`](uitextview/font.md), [`textColor`](uitextview/textcolor.md), and other style-related properties of the class.

## See Also

- [var attributedText: NSAttributedString!](uitextview/attributedtext.md)
  The styled text that the text view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/text)*