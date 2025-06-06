# permissionStatus(for:)

**Framework**: Webkit  
**Kind**: method

Checks the specified match pattern against the currently denied, granted, and requested permission match patterns.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func permissionStatus(for pattern: WKWebExtension.MatchPattern) -> WKWebExtensionContext.PermissionStatus
```

#### Discussion

Match patterns can be granted on a per-tab basis. When the tab is known, access checks should always use the method that checks in a tab.

## Parameters

- `pattern`: The pattern for which to return the status.

## See Also

- [func permissionStatus(for: WKWebExtension.MatchPattern, in: (any WKWebExtensionTab)?) -> WKWebExtensionContext.PermissionStatus](wkwebextensioncontext/permissionstatus(for:in:)-nqhm.md)
  Checks the specified match pattern against the currently denied, granted, and requested permission match patterns.
- [func hasAccess(to: URL, in: (any WKWebExtensionTab)?) -> Bool](wkwebextensioncontext/hasaccess(to:in:).md)
  Checks the specified URL against the currently granted permission match patterns in a specific tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/permissionstatus(for:)-7mu8)*