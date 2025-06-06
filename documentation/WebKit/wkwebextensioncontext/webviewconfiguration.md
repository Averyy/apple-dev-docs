# webViewConfiguration

**Framework**: Webkit  
**Kind**: property

The web view configuration to use for web views that load pages from this extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@NSCopying
@MainActor var webViewConfiguration: WKWebViewConfiguration? { get }
```

#### Discussion

Returns a customized copy of the configuration, originally set in the web extension controller configuration, for this extension.

The app must use this configuration when initializing web views intended to navigate to a URL originating from this extension’s base URL.

The app must also swap web views in tabs when navigating to and from web extension URLs. This property returns `nil` if the context isn’t associated with a web extension controller. The returned configuration copy can be customized prior to web view initialization.

> **Note**: Navigations will fail if a web view using this configuration attempts to navigate to a URL that doesn’t originate from this extension’s base URL. Similarly, navigations will be canceled if a web view not configured with this configuration attempts to navigate to a URL that does originate from this extension’s base URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/webviewconfiguration)*