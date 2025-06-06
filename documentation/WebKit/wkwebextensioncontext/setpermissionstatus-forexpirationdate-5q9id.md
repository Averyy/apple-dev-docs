# setPermissionStatus(_:for:expirationDate:)

**Framework**: Webkit  
**Kind**: method

Sets the permission status of a URL with a distant future expiration date.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func setPermissionStatus(_ status: WKWebExtensionContext.PermissionStatus, for url: URL, expirationDate: Date?)
```

#### Discussion

The URL is converted into a match pattern and will update [`grantedPermissionMatchPatterns`](wkwebextensioncontext/grantedpermissionmatchpatterns.md) and [`deniedPermissionMatchPatterns`](wkwebextensioncontext/deniedpermissionmatchpatterns.md). Use this method for changing a single URL’s status. Passing a `nil` expiration date will be treated as a distant future date. Only [`WKWebExtensionContext.PermissionStatus.deniedExplicitly`](wkwebextensioncontext/permissionstatus/deniedexplicitly.md), [`WKWebExtensionContext.PermissionStatus.unknown`](wkwebextensioncontext/permissionstatus/unknown.md), and [`WKWebExtensionContext.PermissionStatus.grantedExplicitly`](wkwebextensioncontext/permissionstatus/grantedexplicitly.md) states are allowed to be set using this method.

## Parameters

- `status`: The new permission status to set for the given URL.
- `url`: The URL for which to set the status.
- `expirationDate`: The expiration date for the new permission status, or   for distant future.

## See Also

- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: URL)](wkwebextensioncontext/setpermissionstatus(_:for:)-5xahd.md)
  Sets the permission status of a URL with a distant future expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/setpermissionstatus(_:for:expirationdate:)-5q9id)*