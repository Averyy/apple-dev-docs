# init(accountType:updateURL:)

**Framework**: Videosubscriberaccount  
**Kind**: init

Creates a user account object with a URL for account update requests.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+

## Declaration

```swift
init(accountType: VSUserAccount.AccountType = .free, updateURL: URL?)
```

## Parameters

- `accountType`: A constant that represents whether a user has access to paid content.
- `updateURL`: A URL that points to the application’s JavaScript endpoint for update requests.

## See Also

- [VSUserAccount.AccountType](vsuseraccount-swift.struct/accounttype-swift.enum.md)
  Constants that represent whether a user has access to paid content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccount-swift.struct/init(accounttype:updateurl:))*