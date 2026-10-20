# attributeNames

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The SAML attributes that your app sends to the account provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var attributeNames: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * attributeNames;
```

#### Discussion

Use this property to add an array of SAML attribute names to a SAML attribute query request.

## See Also

### Requesting App-Level Authentication
- [var channelIdentifier: String?](./channelidentifier.md)
  The channel identifier for the request.
- [var supportedAccountProviderIdentifiers: [String]](./supportedaccountprovideridentifiers.md)
  A list of identifiers for TV providers that your app supports.
- [var supportedAuthenticationSchemes: [VSAccountProviderAuthenticationScheme]](./supportedauthenticationschemes.md)
  A collection of authentication schemes your app supports for this request.
- [var verificationToken: String?](./verificationtoken.md)
  A token that your app sends to an account provider to identify itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/attributenames)*