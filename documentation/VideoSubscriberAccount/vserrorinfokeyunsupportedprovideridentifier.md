# VSErrorInfoKeyUnsupportedProviderIdentifier

**Framework**: Video Subscriber Account  
**Kind**: var

The identifier of the unsupported subscription provider.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- macOS ?+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let VSErrorInfoKeyUnsupportedProviderIdentifier: String
```

#### Discussion

This key is a string in the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary that the system returns with the error.

## See Also

- [let VSErrorDomain: String](vserrordomain.md)
  The domain for all errors in the framework.
- [let VSErrorInfoKeySAMLResponse: String](vserrorinfokeysamlresponse.md)
  The subscription provider’s SAML error response.
- [let VSErrorInfoKeySAMLResponseStatus: String](vserrorinfokeysamlresponsestatus.md)
  The subscription provider’s SAML error-response status code.
- [let VSErrorInfoKeyAccountProviderResponse: String](vserrorinfokeyaccountproviderresponse.md)
  The account provider’s error-response object.
- [struct VSError](vserror.md)
  Error information in the framework error domain.
- [VSError.Code](vserror/code.md)
  Error codes in the framework error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserrorinfokeyunsupportedprovideridentifier)*