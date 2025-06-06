# permissionStatus(for:in:)

**Framework**: Webkit  
**Kind**: method

Checks the specified permission against the currently denied, granted, and requested permissions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func permissionStatus(for permission: WKWebExtension.Permission, in tab: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus
```

#### Discussion

Permissions can be granted on a per-tab basis. When the tab is known, access checks should always specify the tab.

## Parameters

- `permission`: The permission for which to return the status.
- `tab`: The tab in which to return the permission status, or   if the tab is not known or the global status is desired.

## See Also

- [func permissionStatus(for: WKWebExtension.Permission) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:)-3qq2w.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.
- [func hasPermission(WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> Bool](wkwebextensioncontext/haspermission(_:in:).md)
  Checks the specified permission against the currently granted permissions in a specific tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/permissionstatus(for:in:)-4h82n)*