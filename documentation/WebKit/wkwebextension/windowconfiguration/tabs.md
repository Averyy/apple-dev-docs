# tabs

**Framework**: WebKit  
**Kind**: property

Indicates the existing tabs that should be moved to the window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var tabs: [any WKWebExtensionTab] { get }
```

#### Discussion

If [`tabs`](wkwebextension/windowconfiguration/tabs.md) and [`tabURLs`](wkwebextension/windowconfiguration/taburls.md) are both empty, the app’s default start page should appear in a tab.

## See Also

- [var tabURLs: [URL]](wkwebextension/windowconfiguration/taburls.md)
  Indicates the URLs that the window should initially load as tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/windowconfiguration/tabs)*