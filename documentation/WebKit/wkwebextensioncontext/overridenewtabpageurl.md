# overrideNewTabPageURL

**Framework**: WebKit  
**Kind**: property

The URL to use as an alternative to the default new tab page, if the extension has one.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var overrideNewTabPageURL: URL? { get }
```

#### Discussion

Provides the URL for a new tab page, if provided by the extension; otherwise `nil` if no page is defined.

The app should prompt the user for permission to use the extension’s new tab page as the default.

> **Note**: Navigation to the override new tab page is only possible after this extension has been loaded.

## See Also

- [var webViewConfiguration: WKWebViewConfiguration?](wkwebextensioncontext/webviewconfiguration.md)
  The web view configuration to use for web views that load pages from this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/overridenewtabpageurl)*