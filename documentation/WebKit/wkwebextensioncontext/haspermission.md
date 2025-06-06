# hasPermission(_:)

**Framework**: Webkit  
**Kind**: method

Checks the specified permission against the currently granted permissions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func hasPermission(_ permission: WKWebExtension.Permission) -> Bool
```

## Parameters

- `permission`: The permission for which to return the status.

## See Also

- [var currentPermissions: Set<WKWebExtension.Permission>](wkwebextensioncontext/currentpermissions.md)
  The currently granted permissions that have not expired.
- [func hasPermission(WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> Bool](wkwebextensioncontext/haspermission(_:in:).md)
  Checks the specified permission against the currently granted permissions in a specific tab.
- [func permissionStatus(for: WKWebExtension.Permission) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:)-3qq2w.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.
- [func permissionStatus(for: WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:in:)-4h82n.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/haspermission(_:))*