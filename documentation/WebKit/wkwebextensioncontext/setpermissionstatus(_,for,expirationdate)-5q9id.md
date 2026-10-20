# setPermissionStatus(_:for:expirationDate:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the permission status of a URL with a distant future expiration date.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func setPermissionStatus(_ status: WKWebExtensionContext.PermissionStatus, for url: URL, expirationDate: Date?)
```

```objc
- (void) setPermissionStatus:(WKWebExtensionContextPermissionStatus) status forURL:(NSURL *) url expirationDate:(NSDate *) expirationDate;
```

#### Discussion

The URL is converted into a match pattern and will update [`grantedPermissionMatchPatterns`](./grantedpermissionmatchpatterns.md) and [`deniedPermissionMatchPatterns`](./deniedpermissionmatchpatterns.md). Use this method for changing a single URL’s status. Passing a `nil` expiration date will be treated as a distant future date. Only [`WKWebExtensionContext.PermissionStatus.deniedExplicitly`](./permissionstatus/deniedexplicitly.md), [`WKWebExtensionContext.PermissionStatus.unknown`](./permissionstatus/unknown.md), and [`WKWebExtensionContext.PermissionStatus.grantedExplicitly`](./permissionstatus/grantedexplicitly.md) states are allowed to be set using this method.

## Parameters

- `status`: The new permission status to set for the given URL.
- `url`: The URL for which to set the status.
- `expirationDate`: The expiration date for the new permission status, or `nil` for distant future.

## See Also

### Related Documentation
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: URL)](./setpermissionstatus%28_,for%29-5xahd.md)
  Sets the permission status of a URL with a distant future expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/setpermissionstatus(_:for:expirationdate:)-5q9id)*