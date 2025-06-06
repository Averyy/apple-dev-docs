# verificationData

**Framework**: Videosubscriberaccount  
**Kind**: property

Data you use to verify that the response came from the account provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var verificationData: Data? { get }
```

#### Discussion

Use the data in this property to cryptographically verify that [`samlAttributeQueryResponse`](vsaccountmetadata/samlattributequeryresponse.md) came from the account provider.

## See Also

- [var accountProviderResponse: VSAccountProviderResponse?](vsaccountmetadata/accountproviderresponse.md)
  The response from the account provider.
- [var samlAttributeQueryResponse: String?](vsaccountmetadata/samlattributequeryresponse.md)
  The SAML response from the account provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadata/verificationdata)*