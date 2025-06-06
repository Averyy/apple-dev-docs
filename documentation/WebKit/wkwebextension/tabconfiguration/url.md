# url

**Framework**: Webkit  
**Kind**: property

Indicates the initial URL for the tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var url: URL? { get }
```

#### Discussion

If this property is `nil`, the app’s default start page should appear in the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabconfiguration/url)*