# optionalPermissionMatchPatterns

**Framework**: Webkit  
**Kind**: property

The set of websites that the extension may need access to for optional functionality.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var optionalPermissionMatchPatterns: Set<WKWebExtension.MatchPattern> { get }
```

#### Discussion

These match patterns can be requested by the extension at a later time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/optionalpermissionmatchpatterns)*