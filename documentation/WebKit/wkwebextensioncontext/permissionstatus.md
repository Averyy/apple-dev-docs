# WKWebExtensionContext.PermissionStatus

**Framework**: WebKit  
**Kind**: enum

Constants used to indicate permission status in web extension context.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
enum PermissionStatus
```

## Topics

### Enumeration Cases
- [WKWebExtensionContext.PermissionStatus.deniedExplicitly](wkwebextensioncontext/permissionstatus/deniedexplicitly.md)
  Indicates that the permission was explicitly denied.
- [WKWebExtensionContext.PermissionStatus.deniedImplicitly](wkwebextensioncontext/permissionstatus/deniedimplicitly.md)
  Indicates that the permission was implicitly denied because of another explicitly denied permission.
- [WKWebExtensionContext.PermissionStatus.grantedExplicitly](wkwebextensioncontext/permissionstatus/grantedexplicitly.md)
  Indicates that the permission was explicitly granted permission.
- [WKWebExtensionContext.PermissionStatus.grantedImplicitly](wkwebextensioncontext/permissionstatus/grantedimplicitly.md)
  Indicates that the permission was implicitly granted because of another explicitly granted permission.
- [WKWebExtensionContext.PermissionStatus.requestedExplicitly](wkwebextensioncontext/permissionstatus/requestedexplicitly.md)
  Indicates that the permission was explicitly requested.
- [WKWebExtensionContext.PermissionStatus.requestedImplicitly](wkwebextensioncontext/permissionstatus/requestedimplicitly.md)
  Indicates that the permission was implicitly requested because of another explicitly requested permission.
- [WKWebExtensionContext.PermissionStatus.unknown](wkwebextensioncontext/permissionstatus/unknown.md)
  Indicates an unknown permission status.
### Initializers
- [init?(rawValue: Int)](wkwebextensioncontext/permissionstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/permissionstatus)*