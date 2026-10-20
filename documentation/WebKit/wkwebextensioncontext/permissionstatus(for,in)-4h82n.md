# permissionStatus(for:in:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Checks the specified permission against the currently denied, granted, and requested permissions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func permissionStatus(for permission: WKWebExtension.Permission, in tab: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus
```

```objc
- (WKWebExtensionContextPermissionStatus) permissionStatusForPermission:(WKWebExtensionPermission) permission inTab:(id<WKWebExtensionTab>) tab;
```

#### Discussion

Permissions can be granted on a per-tab basis. When the tab is known, access checks should always specify the tab.

## Parameters

- `permission`: The permission for which to return the status.
- `tab`: The tab in which to return the permission status, or `nil` if the tab is not known or the global status is desired.

## See Also

### Related Documentation
- [func permissionStatus(for: WKWebExtension.Permission) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for%29-3qq2w.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.
- [func hasPermission(WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> Bool](./haspermission%28_,in%29.md)
  Checks the specified permission against the currently granted permissions in a specific tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/permissionstatus(for:in:)-4h82n)*