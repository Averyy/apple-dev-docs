# UITextSmartInsertDeleteType.default

**Framework**: UIKit  
**Kind**: case

Use the default behavior for inserting and deleting space characters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case `default`
```

#### Discussion

This option selectively enables the automatic deletion of one or two neighboring spaces after a cut or delete, and the insertion of an extra space after a paste. For example, this option disables the behavior for email address and password keyboards.

## See Also

- [UITextSmartInsertDeleteType.no](uitextsmartinsertdeletetype/no.md)
  Disable the insertion or deletion of extra spaces.
- [UITextSmartInsertDeleteType.yes](uitextsmartinsertdeletetype/yes.md)
  Enable the insertion or deletion of extra spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsmartinsertdeletetype/default)*