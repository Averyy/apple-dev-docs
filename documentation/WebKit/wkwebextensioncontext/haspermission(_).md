# hasPermission(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Checks the specified permission against the currently granted permissions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func hasPermission(_ permission: WKWebExtension.Permission) -> Bool
```

```objc
- (BOOL) hasPermission:(WKWebExtensionPermission) permission;
```

## Parameters

- `permission`: The permission for which to return the status.

## See Also

### Related Documentation
- [var currentPermissions: Set<WKWebExtension.Permission>](./currentpermissions.md)
  The currently granted permissions that have not expired.
- [func hasPermission(WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> Bool](./haspermission%28_,in%29.md)
  Checks the specified permission against the currently granted permissions in a specific tab.
- [func permissionStatus(for: WKWebExtension.Permission) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for%29-3qq2w.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.
- [func permissionStatus(for: WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for,in%29-4h82n.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/haspermission(_:))*