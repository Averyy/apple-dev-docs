# VSError

**Framework**: Video Subscriber Account  
**Kind**: struct

Error information in the framework error domain.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct VSError
```

## Topics

### Error information
- [static var errorDomain: String](vserror/errordomain.md)
### Error codes
- [static var accessNotGranted: VSError.Code](vserror/accessnotgranted.md)
  The user hasn’t granted access to their subscription information.
- [static var invalidVerificationToken: VSError.Code](vserror/invalidverificationtoken.md)
  The user’s subscription provider rejected the verification token that the app sent with the request.
- [static var providerRejected: VSError.Code](vserror/providerrejected.md)
  The user’s subscription provider didn’t allow the request to proceed.
- [static var rejected: VSError.Code](vserror/rejected.md)
  The system rejected the request.
- [static var serviceTemporarilyUnavailable: VSError.Code](vserror/servicetemporarilyunavailable.md)
  The request failed due to a timeout or unreachable host, but a subsequent attempt might succeed.
- [static var unsupported: VSError.Code](vserror/unsupported.md)
  The provider doesn’t support the feature the user requested in the device’s current region.
- [static var unsupportedProvider: VSError.Code](vserror/unsupportedprovider.md)
  The system doesn’t support the user’s subscription provider.
- [static var userCancelled: VSError.Code](vserror/usercancelled.md)
  The user canceled the request.
- [VSError.Code](vserror/code.md)
  Error codes in the framework error domain.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [VSError.Code](vserror/code.md)
  Error codes in the framework error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserror)*