# hasAccessToAllURLs

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating if the currently granted permission match patterns set contains the `<all_urls>` pattern.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var hasAccessToAllURLs: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasAccessToAllURLs;
```

#### Discussion

This does not check for any `*` host patterns. In most cases you should use the broader [`hasAccessToAllHosts`](./hasaccesstoallhosts.md).

## See Also

### Related Documentation
- [var currentPermissionMatchPatterns: Set<WKWebExtension.MatchPattern>](./currentpermissionmatchpatterns.md)
  The currently granted permission match patterns that have not expired.
- [var hasAccessToAllHosts: Bool](./hasaccesstoallhosts.md)
  A Boolean value indicating if the currently granted permission match patterns set contains the `<all_urls>` pattern or any `*` host patterns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/hasaccesstoallurls)*