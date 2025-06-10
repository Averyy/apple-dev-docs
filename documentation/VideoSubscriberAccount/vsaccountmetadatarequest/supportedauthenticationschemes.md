# supportedAuthenticationSchemes

**Framework**: Video Subscriber Account  
**Kind**: property

A collection of authentication schemes your app supports for this request.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- macOS ?+
- tvOS 10.1+
- visionOS 1.0+

## Declaration

```swift
var supportedAuthenticationSchemes: [VSAccountProviderAuthenticationScheme] { get set }
```

#### Discussion

Use this property to check if the authentication schemes your app supports are compatible with account providers. The default is `VSAccountProviderAuthenticationSchemeSAML`.

## See Also

- [var attributeNames: [String]](vsaccountmetadatarequest/attributenames.md)
  The SAML attributes that your app sends to the account provider.
- [var channelIdentifier: String?](vsaccountmetadatarequest/channelidentifier.md)
  The channel identifier for the request.
- [var supportedAccountProviderIdentifiers: [String]](vsaccountmetadatarequest/supportedaccountprovideridentifiers.md)
  A list of identifiers for TV providers that your app supports.
- [var verificationToken: String?](vsaccountmetadatarequest/verificationtoken.md)
  A token that your app sends to an account provider to identify itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/supportedauthenticationschemes)*