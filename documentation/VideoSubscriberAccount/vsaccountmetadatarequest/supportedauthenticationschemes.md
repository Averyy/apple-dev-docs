# supportedAuthenticationSchemes

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

A collection of authentication schemes your app supports for this request.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 10.2+
- macOS
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
var supportedAuthenticationSchemes: [VSAccountProviderAuthenticationScheme] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * supportedAuthenticationSchemes;
```

#### Discussion

Use this property to check if the authentication schemes your app supports are compatible with account providers. The default is `VSAccountProviderAuthenticationSchemeSAML`.

## See Also

### Requesting App-Level Authentication
- [var attributeNames: [String]](./attributenames.md)
  The SAML attributes that your app sends to the account provider.
- [var channelIdentifier: String?](./channelidentifier.md)
  The channel identifier for the request.
- [var supportedAccountProviderIdentifiers: [String]](./supportedaccountprovideridentifiers.md)
  A list of identifiers for TV providers that your app supports.
- [var verificationToken: String?](./verificationtoken.md)
  A token that your app sends to an account provider to identify itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/supportedauthenticationschemes)*