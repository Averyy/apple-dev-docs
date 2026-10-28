# attributedText

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The styled text that the text view displays.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var attributedText: NSAttributedString! { get set }
```

```objc
@property (copy, null_resettable) NSAttributedString * attributedText;
```

## Discussion

Assigning a new value to this property also replaces the value of the [`text`](./text.md) property with the same string data, albeit without any formatting information. In addition, the [`font`](./font.md), [`textColor`](./textcolor.md), and [`textAlignment`](./textalignment.md) properties are updated to reflect the typing attributes of the text view.

## See Also

### Specifying the text content
- [var text: String!](./text.md)
  The text that the text view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/attributedtext)*