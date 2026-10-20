# invalidVerificationToken

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Type Property

The user’s subscription provider rejected the verification token that the app sent with the request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var invalidVerificationToken: VSError.Code { get }
```

## See Also

### Error codes
- [static var accessNotGranted: VSError.Code](./accessnotgranted.md)
  The user hasn’t granted access to their subscription information.
- [static var providerRejected: VSError.Code](./providerrejected.md)
  The user’s subscription provider didn’t allow the request to proceed.
- [static var rejected: VSError.Code](./rejected.md)
  The system rejected the request.
- [static var serviceTemporarilyUnavailable: VSError.Code](./servicetemporarilyunavailable.md)
  The request failed due to a timeout or unreachable host, but a subsequent attempt might succeed.
- [static var unsupported: VSError.Code](./unsupported.md)
  The provider doesn’t support the feature the user requested in the device’s current region.
- [static var unsupportedProvider: VSError.Code](./unsupportedprovider.md)
  The system doesn’t support the user’s subscription provider.
- [static var userCancelled: VSError.Code](./usercancelled.md)
  The user canceled the request.
- [VSError.Code](./code.md)
  Error codes in the framework error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserror/invalidverificationtoken)*