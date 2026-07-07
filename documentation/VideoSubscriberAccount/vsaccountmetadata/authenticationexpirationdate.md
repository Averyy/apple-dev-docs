# authenticationExpirationDate

**Framework**: Video Subscriber Account  
**Kind**: property

The date when the user’s current authentication session expires.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var authenticationExpirationDate: Date? { get }
```

#### Discussion

This property is `nil` if the user doesn’t have a current authentication session with their account provider.

## See Also

- [var accountProviderIdentifier: String?](vsaccountmetadata/accountprovideridentifier.md)
  The unique identifier of the account provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadata/authenticationexpirationdate)*