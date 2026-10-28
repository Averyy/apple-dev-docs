# permissionStatus(for:in:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Checks the specified URL against the currently denied, granted, and requested permission match patterns.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func permissionStatus(for url: URL, in tab: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus
```

```objc
- (WKWebExtensionContextPermissionStatus) permissionStatusForURL:(NSURL *) url inTab:(id<WKWebExtensionTab>) tab;
```

## Discussion

URLs and match patterns can be granted on a per-tab basis. When the tab is known, access checks should always use this method.

## Parameters

- `url`: The URL for which to return the status.
- `tab`: The tab in which to return the permission status, or `nil` if the tab is not known or the global status is desired.

## See Also

### Related Documentation
- [func permissionStatus(for: URL) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for%29-7ojrb.md)
  Checks the specified URL against the currently denied, granted, and requested permission match patterns.
- [func hasAccess(to: URL, in: (any WKWebExtensionTab)?) -> Bool](./hasaccess%28to,in%29.md)
  Checks the specified URL against the currently granted permission match patterns in a specific tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/permissionstatus(for:in:)-96xaf)*