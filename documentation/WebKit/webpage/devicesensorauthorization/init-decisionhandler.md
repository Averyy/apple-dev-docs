# init(decisionHandler:)

**Framework**: WebKit  
**Kind**: init

Creates a new `DeviceSensorAuthorization` using the specified policy.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
init(decisionHandler: @escaping (WebPage.DeviceSensorAuthorization.Permission, WebPage.FrameInfo, WKSecurityOrigin) async -> WKPermissionDecision)
```

## Parameters

- `decisionHandler`: A closure which decides the permission decision for an authorization request,   which may be based on the kind of permission, the webpage frame information, or the security origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/devicesensorauthorization/init(decisionhandler:))*