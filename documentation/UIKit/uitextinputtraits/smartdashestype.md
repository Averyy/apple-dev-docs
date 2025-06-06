# smartDashesType

**Framework**: UIKit  
**Kind**: property

The configuration state for smart dashes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var smartDashesType: UITextSmartDashesType { get set }
```

#### Discussion

Use this property to configure whether UIKit converts two hyphens into an en-dash and three hyphens into an em-dash automatically. The default value of this property is [`UITextSmartDashesType.default`](uitextsmartdashestype/default.md), which selectively enables smart dashes based on the keyboard type.

## See Also

- [var smartQuotesType: UITextSmartQuotesType](uitextinputtraits/smartquotestype.md)
  The configuration state for smart quotes.
- [enum UITextSmartQuotesType](uitextsmartquotestype.md)
  Constants that indicate whether to enable or disable smart quotes.
- [enum UITextSmartDashesType](uitextsmartdashestype.md)
  Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [var smartInsertDeleteType: UITextSmartInsertDeleteType](uitextinputtraits/smartinsertdeletetype.md)
  The configuration state for the smart insertion and deletion of space characters.
- [enum UITextSmartInsertDeleteType](uitextsmartinsertdeletetype.md)
  Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/smartdashestype)*