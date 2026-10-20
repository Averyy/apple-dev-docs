# requestedPermissionMatchPatterns

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The set of websites that the extension requires access to for its base functionality.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var requestedPermissionMatchPatterns: Set<WKWebExtension.MatchPattern> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<WKWebExtensionMatchPattern *> * requestedPermissionMatchPatterns;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/requestedpermissionmatchpatterns)*