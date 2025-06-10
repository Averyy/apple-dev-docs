# WKNavigationActionPolicy

**Framework**: WebKit  
**Kind**: enum

Constants that indicate whether to allow or cancel navigation to a webpage from an action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
enum WKNavigationActionPolicy
```

## Topics

### Constants
- [WKNavigationActionPolicy.cancel](wknavigationactionpolicy/cancel.md)
  Cancel the navigation.
- [WKNavigationActionPolicy.allow](wknavigationactionpolicy/allow.md)
  Allow the navigation to continue.
- [WKNavigationActionPolicy.download](wknavigationactionpolicy/download.md)
  Allow the download to proceed.
### Initializers
- [init?(rawValue: Int)](wknavigationactionpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, preferences: WKWebpagePreferences, decisionHandler: (WKNavigationActionPolicy, WKWebpagePreferences) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:preferences:decisionhandler:).md)
  Asks the delegate for permission to navigate to new content based on the specified preferences and action information.
- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, decisionHandler: (WKNavigationActionPolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-2ni62.md)
  Asks the delegate for permission to navigate to new content based on the specified action information.
- [func webView(WKWebView, decidePolicyFor: WKNavigationResponse, decisionHandler: (WKNavigationResponsePolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-19mn2.md)
  Asks the delegate for permission to navigate to new content after the response to the navigation request is known.
- [enum WKNavigationResponsePolicy](wknavigationresponsepolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy)*