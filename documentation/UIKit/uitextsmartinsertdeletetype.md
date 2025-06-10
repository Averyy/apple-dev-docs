# UITextSmartInsertDeleteType

**Framework**: UIKit  
**Kind**: enum

Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum UITextSmartInsertDeleteType
```

## Topics

### Constants
- [UITextSmartInsertDeleteType.default](uitextsmartinsertdeletetype/default.md)
  Use the default behavior for inserting and deleting space characters.
- [UITextSmartInsertDeleteType.no](uitextsmartinsertdeletetype/no.md)
  Disable the insertion or deletion of extra spaces.
- [UITextSmartInsertDeleteType.yes](uitextsmartinsertdeletetype/yes.md)
  Enable the insertion or deletion of extra spaces.
### Initializers
- [init?(rawValue: Int)](uitextsmartinsertdeletetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var smartQuotesType: UITextSmartQuotesType](uitextinputtraits/smartquotestype.md)
  The configuration state for smart quotes.
- [enum UITextSmartQuotesType](uitextsmartquotestype.md)
  Constants that indicate whether to enable or disable smart quotes.
- [var smartDashesType: UITextSmartDashesType](uitextinputtraits/smartdashestype.md)
  The configuration state for smart dashes.
- [enum UITextSmartDashesType](uitextsmartdashestype.md)
  Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [var smartInsertDeleteType: UITextSmartInsertDeleteType](uitextinputtraits/smartinsertdeletetype.md)
  The configuration state for the smart insertion and deletion of space characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsmartinsertdeletetype)*