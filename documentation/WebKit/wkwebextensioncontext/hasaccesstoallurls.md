# hasAccessToAllURLs

**Framework**: WebKit  
**Kind**: property

A Boolean value indicating if the currently granted permission match patterns set contains the `<all_urls>` pattern.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var hasAccessToAllURLs: Bool { get }
```

#### Discussion

This does not check for any `*` host patterns. In most cases you should use the broader [`hasAccessToAllHosts`](wkwebextensioncontext/hasaccesstoallhosts.md).

## See Also

- [var currentPermissionMatchPatterns: Set<WKWebExtension.MatchPattern>](wkwebextensioncontext/currentpermissionmatchpatterns.md)
  The currently granted permission match patterns that have not expired.
- [var hasAccessToAllHosts: Bool](wkwebextensioncontext/hasaccesstoallhosts.md)
  A Boolean value indicating if the currently granted permission match patterns set contains the `<all_urls>` pattern or any `*` host patterns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/hasaccesstoallurls)*