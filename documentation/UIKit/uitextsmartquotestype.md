# UITextSmartQuotesType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate whether to enable or disable smart quotes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum UITextSmartQuotesType
```

```c
enum UITextSmartQuotesType : NSInteger;
```

## Topics

### Constants
- [UITextSmartQuotesType.default](./uitextsmartquotestype/default.md)
  Use the default smart quote behavior.
- [UITextSmartQuotesType.no](./uitextsmartquotestype/no.md)
  Disable smart quotes.
- [UITextSmartQuotesType.yes](./uitextsmartquotestype/yes.md)
  Enable smart quotes.
### Initializers
- [init?(rawValue: Int)](./uitextsmartquotestype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the autoformatting behaviors
- [var smartQuotesType: UITextSmartQuotesType](./uitextinputtraits/smartquotestype.md)
  The configuration state for smart quotes.
- [var smartDashesType: UITextSmartDashesType](./uitextinputtraits/smartdashestype.md)
  The configuration state for smart dashes.
- [enum UITextSmartDashesType](./uitextsmartdashestype.md)
  Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [var smartInsertDeleteType: UITextSmartInsertDeleteType](./uitextinputtraits/smartinsertdeletetype.md)
  The configuration state for the smart insertion and deletion of space characters.
- [enum UITextSmartInsertDeleteType](./uitextsmartinsertdeletetype.md)
  Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsmartquotestype)*