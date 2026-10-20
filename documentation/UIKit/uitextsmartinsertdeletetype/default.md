# UITextSmartInsertDeleteType.default

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

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

```c
UITextSmartInsertDeleteTypeDefault
```

#### Discussion

This option selectively enables the automatic deletion of one or two neighboring spaces after a cut or delete, and the insertion of an extra space after a paste. For example, this option disables the behavior for email address and password keyboards.

## See Also

### Constants
- [UITextSmartInsertDeleteType.no](./no.md)
  Disable the insertion or deletion of extra spaces.
- [UITextSmartInsertDeleteType.yes](./yes.md)
  Enable the insertion or deletion of extra spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsmartinsertdeletetype/default)*