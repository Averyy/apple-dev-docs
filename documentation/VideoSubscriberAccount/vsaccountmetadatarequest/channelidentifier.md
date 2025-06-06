# channelIdentifier

**Framework**: Videosubscriberaccount  
**Kind**: property

The channel identifier for the request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var channelIdentifier: String? { get set }
```

#### Discussion

This property identifies the app that is making the request. If you distribute multiple apps, use this identifier to communicate which app sent the request.

> **Note**:  This property is only for applications that use the SAML authentication scheme.

 This property is only for applications that use the SAML authentication scheme.

## See Also

- [var attributeNames: [String]](vsaccountmetadatarequest/attributenames.md)
  The SAML attributes that your app sends to the account provider.
- [var supportedAccountProviderIdentifiers: [String]](vsaccountmetadatarequest/supportedaccountprovideridentifiers.md)
  A list of identifiers for TV providers that your app supports.
- [var supportedAuthenticationSchemes: [VSAccountProviderAuthenticationScheme]](vsaccountmetadatarequest/supportedauthenticationschemes.md)
  A collection of authentication schemes your app supports for this request.
- [var verificationToken: String?](vsaccountmetadatarequest/verificationtoken.md)
  A token that your app sends to an account provider to identify itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest/channelidentifier)*