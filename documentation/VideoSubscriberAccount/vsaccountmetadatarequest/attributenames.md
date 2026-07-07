# attributeNames

**Framework**: Video Subscriber Account  
**Kind**: property

The SAML attributes that your app sends to the account provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var attributeNames: [String] { get set }
```

#### Discussion

Use this property to add an array of SAML attribute names to a SAML attribute query request.

## See Also

- [var channelIdentifier: String?](vsaccountmetadatarequest/channelidentifier.md)
  The channel identifier for the request.
- [var supportedAccountProviderIdentifiers: [String]](vsaccountmetadatarequest/supportedaccountprovideridentifiers.md)
  A list of identifiers for TV providers that your app supports.
- [var supportedAuthenticationSchemes: [VSAccountProviderAuthenticationScheme]](vsaccountmetadatarequest/supportedauthenticationschemes.md)
  A collection of authentication schemes your app supports for this request.
- [var verificationToken: String?](vsaccountmetadatarequest/verificationtoken.md)
  A token that your app sends to an account provider to identify itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/attributenames)*