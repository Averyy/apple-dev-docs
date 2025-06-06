# optionsPageURL

**Framework**: Webkit  
**Kind**: property

The URL of the extension’s options page, if the extension has one.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var optionsPageURL: URL? { get }
```

#### Discussion

Provides the URL for the dedicated options page, if provided by the extension; otherwise `nil` if no page is defined.

The app should provide access to this page through a user interface element.

> **Note**: Navigation to the options page is only possible after this extension has been loaded.

## See Also

- [var webViewConfiguration: WKWebViewConfiguration?](wkwebextensioncontext/webviewconfiguration.md)
  The web view configuration to use for web views that load pages from this extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/optionspageurl)*