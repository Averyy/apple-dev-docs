# accountProviderResponse

**Framework**: Videosubscriberaccount  
**Kind**: property

The response from the account provider.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- macOS ?+
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
var accountProviderResponse: VSAccountProviderResponse? { get }
```

#### Discussion

This property is `nil` if you didn’t specify any attributes in your [`VSAccountMetadataRequest`](vsaccountmetadatarequest.md) object or if the user doesn’t have a valid authentication session with the account provider.

## See Also

- [var samlAttributeQueryResponse: String?](vsaccountmetadata/samlattributequeryresponse.md)
  The SAML response from the account provider.
- [var verificationData: Data?](vsaccountmetadata/verificationdata.md)
  Data you use to verify that the response came from the account provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadata/accountproviderresponse)*