# attributedText

**Framework**: UIKit  
**Kind**: property

The styled text that the text view displays.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var attributedText: NSAttributedString! { get set }
```

#### Discussion

Assigning a new value to this property also replaces the value of the [`text`](uitextview/text.md) property with the same string data, albeit without any formatting information. In addition, the [`font`](uitextview/font.md), [`textColor`](uitextview/textcolor.md), and [`textAlignment`](uitextview/textalignment.md) properties are updated to reflect the typing attributes of the text view.

## See Also

- [var text: String!](uitextview/text.md)
  The text that the text view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/attributedtext)*