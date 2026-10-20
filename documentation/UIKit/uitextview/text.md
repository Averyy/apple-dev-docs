# text

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text that the text view displays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var text: String! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSString * text;
```

#### Discussion

In iOS 6 and later, assigning a new value to this property also replaces the value of the [`attributedText`](./attributedtext.md) property with the same text, albeit without any inherent style attributes. Instead the text view styles the new string using the [`font`](./font.md), [`textColor`](./textcolor.md), and other style-related properties of the class.

## See Also

### Specifying the text content
- [var attributedText: NSAttributedString!](./attributedtext.md)
  The styled text that the text view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/text)*