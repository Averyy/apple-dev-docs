# smartQuotesType

**Framework**: UIKit  
**Kind**: property

The configuration state for smart quotes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var smartQuotesType: UITextSmartQuotesType { get set }
```

#### Discussion

Use this property to configure whether UIKit replaces straight apostrophes and quotation marks with region-specific glyphs. The default value of this property is [`UITextSmartQuotesType.default`](uitextsmartquotestype/default.md), which selectively enables smart quotes based on the keyboard type.

## See Also

- [enum UITextSmartQuotesType](uitextsmartquotestype.md)
  Constants that indicate whether to enable or disable smart quotes.
- [var smartDashesType: UITextSmartDashesType](uitextinputtraits/smartdashestype.md)
  The configuration state for smart dashes.
- [enum UITextSmartDashesType](uitextsmartdashestype.md)
  Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [var smartInsertDeleteType: UITextSmartInsertDeleteType](uitextinputtraits/smartinsertdeletetype.md)
  The configuration state for the smart insertion and deletion of space characters.
- [enum UITextSmartInsertDeleteType](uitextsmartinsertdeletetype.md)
  Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/smartquotestype)*