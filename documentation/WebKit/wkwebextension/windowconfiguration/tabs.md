# tabs

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

Indicates the existing tabs that should be moved to the window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var tabs: [any WKWebExtensionTab] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<id<WKWebExtensionTab>> * tabs;
```

## Discussion

If [`tabs`](./tabs.md) and [`tabURLs`](./taburls.md) are both empty, the app’s default start page should appear in a tab.

## See Also

### Related Documentation
- [var tabURLs: [URL]](./taburls.md)
  Indicates the URLs that the window should initially load as tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/windowconfiguration/tabs)*