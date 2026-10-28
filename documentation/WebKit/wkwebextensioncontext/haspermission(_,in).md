# hasPermission(_:in:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Checks the specified permission against the currently granted permissions in a specific tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func hasPermission(_ permission: WKWebExtension.Permission, in tab: (any WKWebExtensionTab)?) -> Bool
```

```objc
- (BOOL) hasPermission:(WKWebExtensionPermission) permission inTab:(id<WKWebExtensionTab>) tab;
```

## Discussion

Permissions can be granted on a per-tab basis. When the tab is known, permission checks should always use this method.

## Parameters

- `permission`: The permission for which to return the status.
- `tab`: The tab in which to return the permission status, or `nil` if the tab is not known or the global status is desired.

## See Also

### Related Documentation
- [var currentPermissions: Set<WKWebExtension.Permission>](./currentpermissions.md)
  The currently granted permissions that have not expired.
- [func hasPermission(WKWebExtension.Permission) -> Bool](./haspermission%28_%29.md)
  Checks the specified permission against the currently granted permissions.
- [func permissionStatus(for: WKWebExtension.Permission) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for%29-3qq2w.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.
- [func permissionStatus(for: WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for,in%29-4h82n.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/haspermission(_:in:))*