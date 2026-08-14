# VSAccountManager

**Framework**: Video Subscriber Account  
**Kind**: class

The object that coordinates your app’s authentication requests with a TV provider’s authentication service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class VSAccountManager
```

#### Overview

The `VSAccountManager` object allows your app to request access from the user to communicate with their TV provider to understand system-level authentication status, send authentication requests for your app, and deep link to the TV Provider system settings.

## Topics

### Responding to account manager requests
- [var delegate: (any VSAccountManagerDelegate)?](vsaccountmanager/delegate.md)
  The delegate of the account manager object.
- [protocol VSAccountManagerDelegate](vsaccountmanagerdelegate.md)
  The methods you use to respond to authentication view controller requests.
### Checking access status
- [func checkAccessStatus(options: [VSCheckAccessOption : Any], completionHandler: (VSAccountAccessStatus, (any Error)?) -> Void)](vsaccountmanager/checkaccessstatus(options:completionhandler:).md)
  Checks your app’s access to user subscription information, and requests access if needed.
- [struct VSCheckAccessOption](vscheckaccessoption.md)
  The options your app uses when checking access status.
- [enum VSAccountAccessStatus](vsaccountaccessstatus.md)
  Constants that represent your app’s access status to the user’s subscription information.
### Enqueuing requests
- [func enqueue(VSAccountMetadataRequest, completionHandler: (VSAccountMetadata?, (any Error)?) -> Void) -> VSAccountManagerResult](vsaccountmanager/enqueue(_:completionhandler:).md)
  Submits a request for subscriber account information.
- [class VSAccountMetadataRequest](vsaccountmetadatarequest.md)
  An object that specifies what subscriber account information your app retrieves.
- [class VSAccountMetadata](vsaccountmetadata.md)
  A collection of information for a subscriber’s account.
- [class VSAccountManagerResult](vsaccountmanagerresult.md)
  An object that represents a request made for subscriber account information.
- [class VSAccountProviderResponse](vsaccountproviderresponse.md)
  An object that contains the response from the account provider.
- [struct VSAccountProviderAuthenticationScheme](vsaccountproviderauthenticationscheme.md)
  Authentication schemes for account provider requests and responses.
### Deep linking to TV provider settings
- [let VSOpenTVProviderSettingsURLString: String](vsopentvprovidersettingsurlstring.md)
  A URL string you use to deep link to the system’s TV Provider settings.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanager)*