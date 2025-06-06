# VSAccountMetadataRequest

**Framework**: Videosubscriberaccount  
**Kind**: class

An object that specifies what subscriber account information your app retrieves.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class VSAccountMetadataRequest
```

#### Overview

Use a `VSAccountMetadataRequest` object to indicate the specific information your app will obtain about a subscriber from their subscription provider. Also, use this object to provide information to the subscription provider that it needs to perform the request, such as a verification token, the authentication schemes your app supports, or your app’s identifier.

## Topics

### Requesting TV Provider Info
- [var includeAccountProviderIdentifier: Bool](vsaccountmetadatarequest/includeaccountprovideridentifier.md)
  A Boolean value that indicates whether your app requests the identifier of the account provider.
- [var includeAuthenticationExpirationDate: Bool](vsaccountmetadatarequest/includeauthenticationexpirationdate.md)
  A Boolean value that indicates whether your app requests the expiration date of the user’s current authentication session.
### Requesting App-Level Authentication
- [var attributeNames: [String]](vsaccountmetadatarequest/attributenames.md)
  The SAML attributes that your app sends to the account provider.
- [var channelIdentifier: String?](vsaccountmetadatarequest/channelidentifier.md)
  The channel identifier for the request.
- [var supportedAccountProviderIdentifiers: [String]](vsaccountmetadatarequest/supportedaccountprovideridentifiers.md)
  A list of identifiers for TV providers that your app supports.
- [var supportedAuthenticationSchemes: [VSAccountProviderAuthenticationScheme]](vsaccountmetadatarequest/supportedauthenticationschemes.md)
  A collection of authentication schemes your app supports for this request.
- [var verificationToken: String?](vsaccountmetadatarequest/verificationtoken.md)
  A token that your app sends to an account provider to identify itself.
### Specifying Additional Options
- [var isInterruptionAllowed: Bool](vsaccountmetadatarequest/isinterruptionallowed.md)
  A Boolean value that indicates whether your app can prompt the user to authenticate to complete the request.
- [var featuredAccountProviderIdentifiers: [String]](vsaccountmetadatarequest/featuredaccountprovideridentifiers.md)
  The providers your app lists prominently during authentication.
- [var forceAuthentication: Bool](vsaccountmetadatarequest/forceauthentication.md)
  A Boolean value that indicates whether the app ignores cached credentials.
- [var localizedVideoTitle: String?](vsaccountmetadatarequest/localizedvideotitle.md)
  A short, user-presentable name for the video that the user wants to play.
- [var applicationAccountProviders: [VSAccountApplicationProvider]?](vsaccountmetadatarequest/applicationaccountproviders.md)
  An array of application-specific providers to add to the list of account providers.
### Supporting Authentication Share
- [var accountProviderAuthenticationToken: String?](vsaccountmetadatarequest/accountproviderauthenticationtoken.md)
  An authentication session token that your app sends to the account provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func enqueue(VSAccountMetadataRequest, completionHandler: (VSAccountMetadata?, (any Error)?) -> Void) -> VSAccountManagerResult](vsaccountmanager/enqueue(_:completionhandler:).md)
  Submits a request for subscriber account information.
- [class VSAccountMetadata](vsaccountmetadata.md)
  A collection of information for a subscriber’s account.
- [class VSAccountManagerResult](vsaccountmanagerresult.md)
  An object that represents a request made for subscriber account information.
- [class VSAccountProviderResponse](vsaccountproviderresponse.md)
  An object that contains the response from the account provider.
- [struct VSAccountProviderAuthenticationScheme](vsaccountproviderauthenticationscheme.md)
  Authentication schemes for account provider requests and responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadatarequest)*