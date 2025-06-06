# setPermissionStatus(_:for:)

**Framework**: Webkit  
**Kind**: method

Sets the status of a match pattern with a distant future expiration date.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func setPermissionStatus(_ status: WKWebExtensionContext.PermissionStatus, for pattern: WKWebExtension.MatchPattern)
```

#### Discussion

This method will update [`grantedPermissionMatchPatterns`](wkwebextensioncontext/grantedpermissionmatchpatterns.md) and [`deniedPermissionMatchPatterns`](wkwebextensioncontext/deniedpermissionmatchpatterns.md). Use this method for changing a single match pattern’s status. Only [`WKWebExtensionContext.PermissionStatus.deniedExplicitly`](wkwebextensioncontext/permissionstatus/deniedexplicitly.md), [`WKWebExtensionContext.PermissionStatus.unknown`](wkwebextensioncontext/permissionstatus/unknown.md), and [`WKWebExtensionContext.PermissionStatus.grantedExplicitly`](wkwebextensioncontext/permissionstatus/grantedexplicitly.md) states are allowed to be set using this method.

## Parameters

- `status`: The new permission status to set for the given match pattern.
- `pattern`: The match pattern for which to set the status.

## See Also

- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.MatchPattern, expirationDate: Date?)](wkwebextensioncontext/setpermissionstatus(_:for:expirationdate:)-7038f.md)
  Sets the status of a match pattern with a specific expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/setpermissionstatus(_:for:)-6auqv)*