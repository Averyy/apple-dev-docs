# parentTab

**Framework**: Webkit  
**Kind**: property

Indicates the parent tab with which the tab should be related.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var parentTab: (any WKWebExtensionTab)? { get }
```

#### Discussion

If this property is `nil`, no parent tab was specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabconfiguration/parenttab)*