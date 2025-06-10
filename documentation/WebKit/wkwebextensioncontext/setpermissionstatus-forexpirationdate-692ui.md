# setPermissionStatus(_:for:expirationDate:)

**Framework**: WebKit  
**Kind**: method

Sets the status of a permission with a specific expiration date.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func setPermissionStatus(_ status: WKWebExtensionContext.PermissionStatus, for permission: WKWebExtension.Permission, expirationDate: Date?)
```

#### Discussion

This method will update [`grantedPermissions`](wkwebextensioncontext/grantedpermissions.md) and [`deniedPermissions`](wkwebextensioncontext/deniedpermissions.md). Use this method for changing a single permission’s status.

Passing a `nil` expiration date will be treated as a distant future date. Only [`WKWebExtensionContext.PermissionStatus.deniedExplicitly`](wkwebextensioncontext/permissionstatus/deniedexplicitly.md), [`WKWebExtensionContext.PermissionStatus.unknown`](wkwebextensioncontext/permissionstatus/unknown.md), and [`WKWebExtensionContext.PermissionStatus.grantedExplicitly`](wkwebextensioncontext/permissionstatus/grantedexplicitly.md) states are allowed to be set using this method.

## Parameters

- `status`: The new permission status to set for the given permission.
- `permission`: The permission for which to set the status.
- `expirationDate`: The expiration date for the new permission status, or \c nil for distant future.

## See Also

- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.Permission)](wkwebextensioncontext/setpermissionstatus(_:for:)-4u95f.md)
  Sets the status of a permission with a distant future expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/setpermissionstatus(_:for:expirationdate:)-692ui)*