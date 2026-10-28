# tabURLs

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

Indicates the URLs that the window should initially load as tabs.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var tabURLs: [URL] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSURL *> * tabURLs;
```

## Discussion

If [`tabURLs`](./taburls.md) and [`tabs`](./tabs.md) are both empty, the app’s default start page should appear in a tab.

## See Also

### Related Documentation
- [var tabs: [any WKWebExtensionTab]](./tabs.md)
  Indicates the existing tabs that should be moved to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/windowconfiguration/taburls)*