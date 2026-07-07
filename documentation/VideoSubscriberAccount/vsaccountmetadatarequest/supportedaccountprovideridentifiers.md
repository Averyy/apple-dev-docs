# supportedAccountProviderIdentifiers

**Framework**: Video Subscriber Account  
**Kind**: property

A list of identifiers for TV providers that your app supports.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var supportedAccountProviderIdentifiers: [String] { get set }
```

#### Discussion

Use this property to specify which TV providers receive the request. An empty list indicates that your app supports all TV providers in the region.

## See Also

- [var attributeNames: [String]](vsaccountmetadatarequest/attributenames.md)
  The SAML attributes that your app sends to the account provider.
- [var channelIdentifier: String?](vsaccountmetadatarequest/channelidentifier.md)
  The channel identifier for the request.
- [var supportedAuthenticationSchemes: [VSAccountProviderAuthenticationScheme]](vsaccountmetadatarequest/supportedauthenticationschemes.md)
  A collection of authentication schemes your app supports for this request.
- [var verificationToken: String?](vsaccountmetadatarequest/verificationtoken.md)
  A token that your app sends to an account provider to identify itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/supportedaccountprovideridentifiers)*