# WKWebExtensionContext.PermissionStatus

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum WKWebExtensionContextPermissionStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [WKWebExtensionContext.PermissionStatus.deniedExplicitly](./permissionstatus/deniedexplicitly.md)
  Indicates that the permission was explicitly denied.
- [WKWebExtensionContext.PermissionStatus.deniedImplicitly](./permissionstatus/deniedimplicitly.md)
  Indicates that the permission was implicitly denied because of another explicitly denied permission.
- [WKWebExtensionContext.PermissionStatus.grantedExplicitly](./permissionstatus/grantedexplicitly.md)
  Indicates that the permission was explicitly granted permission.
- [WKWebExtensionContext.PermissionStatus.grantedImplicitly](./permissionstatus/grantedimplicitly.md)
  Indicates that the permission was implicitly granted because of another explicitly granted permission.
- [WKWebExtensionContext.PermissionStatus.requestedExplicitly](./permissionstatus/requestedexplicitly.md)
  Indicates that the permission was explicitly requested.
- [WKWebExtensionContext.PermissionStatus.requestedImplicitly](./permissionstatus/requestedimplicitly.md)
  Indicates that the permission was implicitly requested because of another explicitly requested permission.
- [WKWebExtensionContext.PermissionStatus.unknown](./permissionstatus/unknown.md)
  Indicates an unknown permission status.
### Initializers
- [init?(rawValue: Int)](./permissionstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/permissionstatus)*