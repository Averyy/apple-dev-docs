# verificationToken

**Framework**: Video Subscriber Account  
**Kind**: property

A token that your app sends to an account provider to identify itself.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var verificationToken: String? { get set }
```

#### Discussion

Account providers use this token to verify the identity of the requesting app.

## See Also

- [var attributeNames: [String]](vsaccountmetadatarequest/attributenames.md)
  The SAML attributes that your app sends to the account provider.
- [var channelIdentifier: String?](vsaccountmetadatarequest/channelidentifier.md)
  The channel identifier for the request.
- [var supportedAccountProviderIdentifiers: [String]](vsaccountmetadatarequest/supportedaccountprovideridentifiers.md)
  A list of identifiers for TV providers that your app supports.
- [var supportedAuthenticationSchemes: [VSAccountProviderAuthenticationScheme]](vsaccountmetadatarequest/supportedauthenticationschemes.md)
  A collection of authentication schemes your app supports for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/verificationtoken)*