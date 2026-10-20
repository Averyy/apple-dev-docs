# currentPermissionMatchPatterns

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The currently granted permission match patterns that have not expired.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var currentPermissionMatchPatterns: Set<WKWebExtension.MatchPattern> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<WKWebExtensionMatchPattern *> * currentPermissionMatchPatterns;
```

## See Also

### Related Documentation
- [var grantedPermissionMatchPatterns: [WKWebExtension.MatchPattern : Date]](./grantedpermissionmatchpatterns.md)
  The currently granted permission match patterns and their expiration dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/currentpermissionmatchpatterns)*