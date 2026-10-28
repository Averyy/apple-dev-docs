# setPermissionStatus(_:for:)

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
func setPermissionStatus(_ status: WKWebExtensionContext.PermissionStatus, for url: URL)
```

```objc
- (void) setPermissionStatus:(WKWebExtensionContextPermissionStatus) status forURL:(NSURL *) url;
```

## Discussion

The URL is converted into a match pattern and will update [`grantedPermissionMatchPatterns`](./grantedpermissionmatchpatterns.md) and [`deniedPermissionMatchPatterns`](./deniedpermissionmatchpatterns.md). Use this method for changing a single URL’s status. Only [`WKWebExtensionContext.PermissionStatus.deniedExplicitly`](./permissionstatus/deniedexplicitly.md), [`WKWebExtensionContext.PermissionStatus.unknown`](./permissionstatus/unknown.md), and [`WKWebExtensionContext.PermissionStatus.grantedExplicitly`](./permissionstatus/grantedexplicitly.md) states are allowed to be set using this method.

## Parameters

- `status`: The new permission status to set for the given URL.
- `url`: The URL for which to set the status.

## See Also

### Related Documentation
- [func setPermissionStatus(WKWebExtensionContext.PermissionStatus, for: URL, expirationDate: Date?)](./setpermissionstatus%28_,for,expirationdate%29-5q9id.md)
  Sets the permission status of a URL with a distant future expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/setpermissionstatus(_:for:)-5xahd)*