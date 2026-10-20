# verificationData

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

Data you use to verify that the response came from the account provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var verificationData: Data? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSData * verificationData;
```

#### Discussion

Use the data in this property to cryptographically verify that [`samlAttributeQueryResponse`](./samlattributequeryresponse.md) came from the account provider.

## See Also

### Getting App Authentication Info
- [var accountProviderResponse: VSAccountProviderResponse?](./accountproviderresponse.md)
  The response from the account provider.
- [var samlAttributeQueryResponse: String?](./samlattributequeryresponse.md)
  The SAML response from the account provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadata/verificationdata)*