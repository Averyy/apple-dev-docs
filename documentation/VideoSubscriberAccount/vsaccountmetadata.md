# VSAccountMetadata

**Framework**: Video Subscriber Account  
**Kind**: class

A collection of information for a subscriber’s account.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class VSAccountMetadata
```

#### Overview

The [`VSAccountMetadata`](vsaccountmetadata.md) object contains the information you requested in the [`VSAccountMetadataRequest`](vsaccountmetadatarequest.md) object that you passed to the [`enqueue(_:completionHandler:)`](vsaccountmanager/enqueue(_:completionhandler:).md) method. If the call succeeds, the system sends the [`VSAccountMetadata`](vsaccountmetadata.md) object to your app’s completion handler for your app to process.

## Topics

### Getting TV Provider Info
- [var accountProviderIdentifier: String?](vsaccountmetadata/accountprovideridentifier.md)
  The unique identifier of the account provider.
- [var authenticationExpirationDate: Date?](vsaccountmetadata/authenticationexpirationdate.md)
  The date when the user’s current authentication session expires.
### Getting App Authentication Info
- [var accountProviderResponse: VSAccountProviderResponse?](vsaccountmetadata/accountproviderresponse.md)
  The response from the account provider.
- [var samlAttributeQueryResponse: String?](vsaccountmetadata/samlattributequeryresponse.md)
  The SAML response from the account provider.
- [var verificationData: Data?](vsaccountmetadata/verificationdata.md)
  Data you use to verify that the response came from the account provider.

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
- [class VSAccountMetadataRequest](vsaccountmetadatarequest.md)
  An object that specifies what subscriber account information your app retrieves.
- [class VSAccountManagerResult](vsaccountmanagerresult.md)
  An object that represents a request made for subscriber account information.
- [class VSAccountProviderResponse](vsaccountproviderresponse.md)
  An object that contains the response from the account provider.
- [struct VSAccountProviderAuthenticationScheme](vsaccountproviderauthenticationscheme.md)
  Authentication schemes for account provider requests and responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmetadata)*