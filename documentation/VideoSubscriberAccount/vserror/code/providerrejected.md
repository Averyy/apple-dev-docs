# VSError.Code.providerRejected

**Framework**: Video Subscriber Account  
**Kind**: case

The user’s subscription provider didn’t allow the request to proceed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case providerRejected
```

#### Discussion

This error can occur when the user’s subscription doesn’t include the resource the user requested, or when the system requires the user to authenticate, but the request doesn’t allow interruption.

## See Also

- [VSError.Code.accessNotGranted](vserror/code/accessnotgranted.md)
  The user hasn’t granted access to their subscription information.
- [VSError.Code.invalidVerificationToken](vserror/code/invalidverificationtoken.md)
  The user’s subscription provider rejected the verification token that the app sent with the request.
- [VSError.Code.rejected](vserror/code/rejected.md)
  The system rejected the request.
- [VSError.Code.serviceTemporarilyUnavailable](vserror/code/servicetemporarilyunavailable.md)
  The request failed due to a timeout or unreachable host, but a subsequent attempt might succeed.
- [VSError.Code.unsupported](vserror/code/unsupported.md)
  The provider doesn’t support the feature the user requested in the device’s current region.
- [VSError.Code.unsupportedProvider](vserror/code/unsupportedprovider.md)
  The system doesn’t support the user’s subscription provider.
- [VSError.Code.userCancelled](vserror/code/usercancelled.md)
  The user canceled the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserror/code/providerrejected)*