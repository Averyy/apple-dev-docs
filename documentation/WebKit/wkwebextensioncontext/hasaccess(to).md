# hasAccess(to:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Checks the specified URL against the currently granted permission match patterns.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func hasAccess(to url: URL) -> Bool
```

```objc
- (BOOL) hasAccessToURL:(NSURL *) url;
```

## Parameters

- `url`: The URL for which to return the status.

## See Also

### Related Documentation
- [var currentPermissionMatchPatterns: Set<WKWebExtension.MatchPattern>](./currentpermissionmatchpatterns.md)
  The currently granted permission match patterns that have not expired.
- [func hasAccess(to: URL, in: (any WKWebExtensionTab)?) -> Bool](./hasaccess%28to,in%29.md)
  Checks the specified URL against the currently granted permission match patterns in a specific tab.
- [func permissionStatus(for: URL) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for%29-7ojrb.md)
  Checks the specified URL against the currently denied, granted, and requested permission match patterns.
- [func permissionStatus(for: URL, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for,in%29-96xaf.md)
  Checks the specified URL against the currently denied, granted, and requested permission match patterns.
- [func permissionStatus(for: WKWebExtension.MatchPattern) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for%29-7mu8.md)
  Checks the specified match pattern against the currently denied, granted, and requested permission match patterns.
- [func permissionStatus(for: WKWebExtension.MatchPattern, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](./permissionstatus%28for,in%29-nqhm.md)
  Checks the specified match pattern against the currently denied, granted, and requested permission match patterns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/hasaccess(to:))*