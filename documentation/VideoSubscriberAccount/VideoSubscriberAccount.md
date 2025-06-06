# Video Subscriber Account

**Framework**: Videosubscriberaccount  
**Kind**: module

Support TV provider and Apple TV app functionality.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+

#### Overview

`VideoSubscriberAccount` provides APIs to help you create apps that require secure communication with a TV provider’s authentication service. The framework also informs the Apple TV app about whether your user has a subscription and the details of that subscription.

## Topics

### TV provider authentication
- [class VSAccountManager](vsaccountmanager.md)
  The object that coordinates your app’s authentication requests with a TV provider’s authentication service.
### TV app integration
- [class VSSubscription](vssubscription.md)
  An object that describes a subscriber’s access to content.
- [class VSSubscriptionRegistrationCenter](vssubscriptionregistrationcenter.md)
  An object that stores subscription information that the system provides to the Apple TV app.
- [class VSAccountApplicationProvider](vsaccountapplicationprovider.md)
  An object to display app-specific providers in your app.
### User account management
- [class VSUserAccountManager](vsuseraccountmanager.md)
  The object that coordinates your app’s user account actions.
- [struct VSUserAccount](vsuseraccount-swift.struct.md)
  An object that represents a user’s account.
### Errors
- [let VSErrorDomain: String](vserrordomain.md)
  The domain for all errors in the framework.
- [let VSErrorInfoKeySAMLResponse: String](vserrorinfokeysamlresponse.md)
  The subscription provider’s SAML error response.
- [let VSErrorInfoKeySAMLResponseStatus: String](vserrorinfokeysamlresponsestatus.md)
  The subscription provider’s SAML error-response status code.
- [let VSErrorInfoKeyAccountProviderResponse: String](vserrorinfokeyaccountproviderresponse.md)
  The account provider’s error-response object.
- [let VSErrorInfoKeyUnsupportedProviderIdentifier: String](vserrorinfokeyunsupportedprovideridentifier.md)
  The identifier of the unsupported subscription provider.
- [struct VSError](vserror.md)
  Error information in the framework error domain.
- [VSError.Code](vserror/code.md)
  Error codes in the framework error domain.
### Structures
- [struct VSAppleSubscription](vsapplesubscription-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/VideoSubscriberAccount)*