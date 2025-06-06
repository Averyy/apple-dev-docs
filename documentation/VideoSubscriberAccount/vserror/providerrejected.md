# providerRejected

**Framework**: Videosubscriberaccount  
**Kind**: property

The user’s subscription provider didn’t allow the request to proceed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var providerRejected: VSError.Code { get }
```

#### Discussion

This error can occur when the user’s subscription doesn’t include the resource the user requested, or when the system requires the user to authenticate, but the request doesn’t allow interruption.

## See Also

- [static var accessNotGranted: VSError.Code](vserror/accessnotgranted.md)
  The user hasn’t granted access to their subscription information.
- [static var invalidVerificationToken: VSError.Code](vserror/invalidverificationtoken.md)
  The user’s subscription provider rejected the verification token that the app sent with the request.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserror/providerrejected)*