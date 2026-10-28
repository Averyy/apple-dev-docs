# VSUserAccount.AccountType

**Framework**: Video Subscriber Account  
**Kind**: enum  
**Role**: Enumeration

Constants that represent whether a user has access to paid content.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS

## Declaration

```swift
enum AccountType
```

## Overview

The default is [`VSUserAccount.AccountType.free`](./accounttype-swift.enum/free.md).

## Topics

### Account types
- [VSUserAccount.AccountType.free](./accounttype-swift.enum/free.md)
  A constant that indicates a user has access to free content.
- [VSUserAccount.AccountType.paid](./accounttype-swift.enum/paid.md)
  A constant that indicate a user has access to paid content.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating user accounts
- [init(accountType: VSUserAccount.AccountType, updateURL: URL?)](./init%28accounttype,updateurl%29.md)
  Creates a user account object with a URL for account update requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccount-swift.struct/accounttype-swift.enum)*