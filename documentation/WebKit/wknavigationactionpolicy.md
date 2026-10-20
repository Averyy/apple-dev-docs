# WKNavigationActionPolicy

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum WKNavigationActionPolicy : NSInteger;
```

## Topics

### Constants
- [WKNavigationActionPolicy.cancel](./wknavigationactionpolicy/cancel.md)
  Cancel the navigation.
- [WKNavigationActionPolicy.allow](./wknavigationactionpolicy/allow.md)
  Allow the navigation to continue.
- [WKNavigationActionPolicy.download](./wknavigationactionpolicy/download.md)
  Allow the download to proceed.
### Initializers
- [init?(rawValue: Int)](./wknavigationactionpolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Allowing or denying navigation requests
- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, preferences: WKWebpagePreferences, decisionHandler: (WKNavigationActionPolicy, WKWebpagePreferences) -> Void)](./wknavigationdelegate/webview%28_,decidepolicyfor,preferences,decisionhandler%29.md)
  Asks the delegate for permission to navigate to new content based on the specified preferences and action information.
- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, decisionHandler: (WKNavigationActionPolicy) -> Void)](./wknavigationdelegate/webview%28_,decidepolicyfor,decisionhandler%29-2ni62.md)
  Asks the delegate for permission to navigate to new content based on the specified action information.
- [func webView(WKWebView, decidePolicyFor: WKNavigationResponse, decisionHandler: (WKNavigationResponsePolicy) -> Void)](./wknavigationdelegate/webview%28_,decidepolicyfor,decisionhandler%29-19mn2.md)
  Asks the delegate for permission to navigate to new content after the response to the navigation request is known.
- [enum WKNavigationResponsePolicy](./wknavigationresponsepolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationactionpolicy)*