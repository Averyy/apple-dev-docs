# currentPermissionMatchPatterns

**Framework**: Webkit  
**Kind**: property

The currently granted permission match patterns that have not expired.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var currentPermissionMatchPatterns: Set<WKWebExtension.MatchPattern> { get }
```

## See Also

- [var grantedPermissionMatchPatterns: [WKWebExtension.MatchPattern : Date]](wkwebextensioncontext/grantedpermissionmatchpatterns.md)
  The currently granted permission match patterns and their expiration dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/currentpermissionmatchpatterns)*