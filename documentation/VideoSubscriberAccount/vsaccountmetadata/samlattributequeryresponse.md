# samlAttributeQueryResponse

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The SAML response from the account provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var samlAttributeQueryResponse: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * SAMLAttributeQueryResponse;
```

#### Discussion

This property is `nil` if you didn’t specify any SAML attributes in your [`VSAccountMetadataRequest`](../vsaccountmetadatarequest.md) object or if the person doesn’t have a valid authentication session with the account provider.

## See Also

### Getting App Authentication Info
- [var accountProviderResponse: VSAccountProviderResponse?](./accountproviderresponse.md)
  The response from the account provider.
- [var verificationData: Data?](./verificationdata.md)
  Data you use to verify that the response came from the account provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadata/samlattributequeryresponse)*