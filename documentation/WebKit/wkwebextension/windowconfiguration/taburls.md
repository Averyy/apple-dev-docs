# tabURLs

**Framework**: WebKit  
**Kind**: property

Indicates the URLs that the window should initially load as tabs.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var tabURLs: [URL] { get }
```

#### Discussion

If [`tabURLs`](wkwebextension/windowconfiguration/taburls.md) and [`tabs`](wkwebextension/windowconfiguration/tabs.md) are both empty, the app’s default start page should appear in a tab.

## See Also

- [var tabs: [any WKWebExtensionTab]](wkwebextension/windowconfiguration/tabs.md)
  Indicates the existing tabs that should be moved to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/windowconfiguration/taburls)*