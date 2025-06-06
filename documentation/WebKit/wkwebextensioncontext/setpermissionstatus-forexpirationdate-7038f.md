# setPermissionStatus(_:for:expirationDate:)

**Framework**: Webkit  
**Kind**: method

Sets the status of a match pattern with a specific expiration date.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func setPermissionStatus(_ status: WKWebExtensionContext.PermissionStatus, for pattern: WKWebExtension.MatchPattern, expirationDate: Date?)
```

#### Discussion

This method will update [`grantedPermissionMatchPatterns`](wkwebextensioncontext/grantedpermissionmatchpatterns.md) and [`deniedPermissionMatchPatterns`](wkwebextensioncontext/deniedpermissionmatchpatterns.md). Use this method for changing a single match pattern’s status.

Passing a `nil` expiration date will be treated as a distant future date. Only [`WKWebExtensionContext.PermissionStatus.deniedExplicitly`](wkwebextensioncontext/permissionstatus/deniedexplicitly.md), [`WKWebExtensionContext.PermissionStatus.unknown`](wkwebextensioncontext/permissionstatus/unknown.md), and [`WKWebExtensionContext.PermissionStatus.grantedExplicitly`](wkwebextensioncontext/permissionstatus/grantedexplicitly.md) states are allowed to be set using this method.

## Parameters

- `status`: The new permission status to set for the given match pattern.
- `pattern`: The match pattern for which to set the status.
- `expirationDate`: The expiration date for the new permission status, or   for distant future.

## See Also

- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.MatchPattern)](wkwebextensioncontext/setpermissionstatus(_:for:)-6auqv.md)
  Sets the status of a match pattern with a distant future expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/setpermissionstatus(_:for:expirationdate:)-7038f)*