# permissionStatus(for:)

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
func permissionStatus(for url: URL) -> WKWebExtensionContext.PermissionStatus
```

```objc
- (WKWebExtensionContextPermissionStatus) permissionStatusForURL:(NSURL *) url;
```

#### Discussion

URLs and match patterns can be granted on a per-tab basis. When the tab is known, access checks should always use the method that checks in a tab.

## Parameters

- `url`: The URL for which to return the status.

## See Also

### Related Documentation
- [func permissionStatus(for: URL, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for,in%29-96xaf.md)
  Checks the specified URL against the currently denied, granted, and requested permission match patterns.
- [func hasAccess(to: URL) -> Bool](./hasaccess%28to%29.md)
  Checks the specified URL against the currently granted permission match patterns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/permissionstatus(for:)-7ojrb)*