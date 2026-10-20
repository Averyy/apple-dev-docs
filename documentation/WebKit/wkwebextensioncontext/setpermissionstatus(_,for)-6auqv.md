# setPermissionStatus(_:for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the status of a match pattern with a distant future expiration date.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func setPermissionStatus(_ status: WKWebExtensionContext.PermissionStatus, for pattern: WKWebExtension.MatchPattern)
```

```objc
- (void) setPermissionStatus:(WKWebExtensionContextPermissionStatus) status forMatchPattern:(WKWebExtensionMatchPattern *) pattern;
```

#### Discussion

This method will update [`grantedPermissionMatchPatterns`](./grantedpermissionmatchpatterns.md) and [`deniedPermissionMatchPatterns`](./deniedpermissionmatchpatterns.md). Use this method for changing a single match pattern’s status. Only [`WKWebExtensionContext.PermissionStatus.deniedExplicitly`](./permissionstatus/deniedexplicitly.md), [`WKWebExtensionContext.PermissionStatus.unknown`](./permissionstatus/unknown.md), and [`WKWebExtensionContext.PermissionStatus.grantedExplicitly`](./permissionstatus/grantedexplicitly.md) states are allowed to be set using this method.

## Parameters

- `status`: The new permission status to set for the given match pattern.
- `pattern`: The match pattern for which to set the status.

## See Also

### Related Documentation
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: WKWebExtension.MatchPattern, expirationDate: Date?)](./setpermissionstatus%28_,for,expirationdate%29-7038f.md)
  Sets the status of a match pattern with a specific expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/setpermissionstatus(_:for:)-6auqv)*