# VSError.Code.rejected

**Framework**: Video Subscriber Account  
**Kind**: case  
**Role**: Case

The system rejected the request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case rejected
```

```c
VSErrorCodeRejected
```

#### Discussion

Only TV provider apps can use this error code.

## See Also

### Error Codes
- [VSError.Code.accessNotGranted](./accessnotgranted.md)
  The user hasn’t granted access to their subscription information.
- [VSError.Code.invalidVerificationToken](./invalidverificationtoken.md)
  The user’s subscription provider rejected the verification token that the app sent with the request.
- [VSError.Code.providerRejected](./providerrejected.md)
  The user’s subscription provider didn’t allow the request to proceed.
- [VSError.Code.serviceTemporarilyUnavailable](./servicetemporarilyunavailable.md)
  The request failed due to a timeout or unreachable host, but a subsequent attempt might succeed.
- [VSError.Code.unsupported](./unsupported.md)
  The provider doesn’t support the feature the user requested in the device’s current region.
- [VSError.Code.unsupportedProvider](./unsupportedprovider.md)
  The system doesn’t support the user’s subscription provider.
- [VSError.Code.userCancelled](./usercancelled.md)
  The user canceled the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vserror/code/rejected)*