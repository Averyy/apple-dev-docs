# VSErrorInfoKeySAMLResponseStatus

**Framework**: Video Subscriber Account  
**Kind**: var

The subscription provider’s SAML error-response status code.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let VSErrorInfoKeySAMLResponseStatus: String
```

#### Discussion

This key is a string in the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary that the system returns with the error.

## See Also

- [let VSErrorDomain: String](vserrordomain.md)
  The domain for all errors in the framework.
- [let VSErrorInfoKeySAMLResponse: String](vserrorinfokeysamlresponse.md)
  The subscription provider’s SAML error response.
- [let VSErrorInfoKeyAccountProviderResponse: String](vserrorinfokeyaccountproviderresponse.md)
  The account provider’s error-response object.
- [let VSErrorInfoKeyUnsupportedProviderIdentifier: String](vserrorinfokeyunsupportedprovideridentifier.md)
  The identifier of the unsupported subscription provider.
- [struct VSError](vserror.md)
  Error information in the framework error domain.
- [VSError.Code](vserror/code.md)
  Error codes in the framework error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserrorinfokeysamlresponsestatus)*