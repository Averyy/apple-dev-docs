# WKNavigationResponsePolicy

**Framework**: Webkit  
**Kind**: enum

Constants that indicate whether to allow or cancel navigation to a webpage from a response.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
enum WKNavigationResponsePolicy
```

## Topics

### Constants
- [WKNavigationResponsePolicy.cancel](wknavigationresponsepolicy/cancel.md)
  Cancel the navigation.
- [WKNavigationResponsePolicy.allow](wknavigationresponsepolicy/allow.md)
  Allow the navigation to continue.
- [WKNavigationResponsePolicy.download](wknavigationresponsepolicy/download.md)
  Allow the download to proceed.
### Initializers
- [init?(rawValue: Int)](wknavigationresponsepolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, preferences: WKWebpagePreferences, decisionHandler: (WKNavigationActionPolicy, WKWebpagePreferences) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:preferences:decisionhandler:).md)
  Asks the delegate for permission to navigate to new content based on the specified preferences and action information.
- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, decisionHandler: (WKNavigationActionPolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-2ni62.md)
  Asks the delegate for permission to navigate to new content based on the specified action information.
- [enum WKNavigationActionPolicy](wknavigationactionpolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from an action.
- [func webView(WKWebView, decidePolicyFor: WKNavigationResponse, decisionHandler: (WKNavigationResponsePolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-19mn2.md)
  Asks the delegate for permission to navigate to new content after the response to the navigation request is known.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationresponsepolicy)*