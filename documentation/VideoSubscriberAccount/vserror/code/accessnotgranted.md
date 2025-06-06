# VSError.Code.accessNotGranted

**Framework**: Videosubscriberaccount  
**Kind**: case

The user hasn’t granted access to their subscription information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case accessNotGranted
```

## See Also

- [VSError.Code.invalidVerificationToken](vserror/code/invalidverificationtoken.md)
  The user’s subscription provider rejected the verification token that the app sent with the request.
- [VSError.Code.providerRejected](vserror/code/providerrejected.md)
  The user’s subscription provider didn’t allow the request to proceed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserror/code/accessnotgranted)*