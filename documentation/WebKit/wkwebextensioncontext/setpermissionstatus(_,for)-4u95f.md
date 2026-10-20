# setPermissionStatus(_:for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the status of a permission with a distant future expiration date.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func setPermissionStatus(_ status: WKWebExtensionContext.PermissionStatus, for permission: WKWebExtension.Permission)
```

```objc
- (void) setPermissionStatus:(WKWebExtensionContextPermissionStatus) status forPermission:(WKWebExtensionPermission) permission;
```

#### Discussion

This method will update [`grantedPermissions`](./grantedpermissions.md) and [`deniedPermissions`](./deniedpermissions.md). Use this method for changing a single permission’s status.

Only [`WKWebExtensionContext.PermissionStatus.deniedExplicitly`](./permissionstatus/deniedexplicitly.md), [`WKWebExtensionContext.PermissionStatus.unknown`](./permissionstatus/unknown.md), and [`WKWebExtensionContext.PermissionStatus.grantedExplicitly`](./permissionstatus/grantedexplicitly.md) states are allowed to be set using this method.

## Parameters

- `status`: The new permission status to set for the given permission.
- `permission`: The permission for which to set the status.

## See Also

### Related Documentation
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.Permission, expirationDate: Date?)](./setpermissionstatus%28_,for,expirationdate%29-692ui.md)
  Sets the status of a permission with a specific expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/setpermissionstatus(_:for:)-4u95f)*