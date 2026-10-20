# VSError.Code

**Framework**: Video Subscriber Account  
**Kind**: enum  
**Role**: Enumeration

Error codes in the framework error domain.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum VSErrorCode : NSInteger;
```

## Topics

### Error Codes
- [VSError.Code.accessNotGranted](./code/accessnotgranted.md)
  The user hasn’t granted access to their subscription information.
- [VSError.Code.invalidVerificationToken](./code/invalidverificationtoken.md)
  The user’s subscription provider rejected the verification token that the app sent with the request.
- [VSError.Code.providerRejected](./code/providerrejected.md)
  The user’s subscription provider didn’t allow the request to proceed.
- [VSError.Code.rejected](./code/rejected.md)
  The system rejected the request.
- [VSError.Code.serviceTemporarilyUnavailable](./code/servicetemporarilyunavailable.md)
  The request failed due to a timeout or unreachable host, but a subsequent attempt might succeed.
- [VSError.Code.unsupported](./code/unsupported.md)
  The provider doesn’t support the feature the user requested in the device’s current region.
- [VSError.Code.unsupportedProvider](./code/unsupportedprovider.md)
  The system doesn’t support the user’s subscription provider.
- [VSError.Code.userCancelled](./code/usercancelled.md)
  The user canceled the request.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [let VSErrorDomain: String](../vserrordomain.md)
  The domain for all errors in the framework.
- [let VSErrorInfoKeySAMLResponse: String](../vserrorinfokeysamlresponse.md)
  The subscription provider’s SAML error response.
- [let VSErrorInfoKeySAMLResponseStatus: String](../vserrorinfokeysamlresponsestatus.md)
  The subscription provider’s SAML error-response status code.
- [let VSErrorInfoKeyAccountProviderResponse: String](../vserrorinfokeyaccountproviderresponse.md)
  The account provider’s error-response object.
- [let VSErrorInfoKeyUnsupportedProviderIdentifier: String](../vserrorinfokeyunsupportedprovideridentifier.md)
  The identifier of the unsupported subscription provider.
- [struct VSError](../vserror.md)
  Error information in the framework error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserror/code)*