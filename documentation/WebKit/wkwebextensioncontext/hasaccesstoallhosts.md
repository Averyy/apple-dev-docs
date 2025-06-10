# hasAccessToAllHosts

**Framework**: WebKit  
**Kind**: property

A Boolean value indicating if the currently granted permission match patterns set contains the `<all_urls>` pattern or any `*` host patterns.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var hasAccessToAllHosts: Bool { get }
```

## See Also

- [var currentPermissionMatchPatterns: Set<WKWebExtension.MatchPattern>](wkwebextensioncontext/currentpermissionmatchpatterns.md)
  The currently granted permission match patterns that have not expired.
- [var hasAccessToAllURLs: Bool](wkwebextensioncontext/hasaccesstoallurls.md)
  A Boolean value indicating if the currently granted permission match patterns set contains the `<all_urls>` pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/hasaccesstoallhosts)*