# samlAttributeQueryResponse

**Framework**: Video Subscriber Account  
**Kind**: property

The SAML response from the account provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var samlAttributeQueryResponse: String? { get }
```

#### Discussion

This property is `nil` if you didn’t specify any SAML attributes in your [`VSAccountMetadataRequest`](vsaccountmetadatarequest.md) object or if the person doesn’t have a valid authentication session with the account provider.

## See Also

- [var accountProviderResponse: VSAccountProviderResponse?](vsaccountmetadata/accountproviderresponse.md)
  The response from the account provider.
- [var verificationData: Data?](vsaccountmetadata/verificationdata.md)
  Data you use to verify that the response came from the account provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadata/samlattributequeryresponse)*