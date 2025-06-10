# permissionStatus(for:)

**Framework**: WebKit  
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
func permissionStatus(for permission: WKWebExtension.Permission) -> WKWebExtensionContext.PermissionStatus
```

#### Discussion

Permissions can be granted on a per-tab basis. When the tab is known, access checks should always use the method that checks in a tab.

## Parameters

- `permission`: The permission for which to return the status.

## See Also

- [func permissionStatus(for: WKWebExtension.Permission, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:in:)-4h82n.md)
  Checks the specified permission against the currently denied, granted, and requested permissions.
- [func hasPermission(WKWebExtension.Permission) -> Bool](wkwebextensioncontext/haspermission(_:).md)
  Checks the specified permission against the currently granted permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/permissionstatus(for:)-3qq2w)*