# webView(_:decidePolicyFor:preferences:decisionHandler:)

**Framework**: WebKit  
**Kind**: method

Asks the delegate for permission to navigate to new content based on the specified preferences and action information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, preferences: WKWebpagePreferences) async -> (WKNavigationActionPolicy, WKWebpagePreferences)
```

#### Discussion

Use this method to allow or deny a navigation request that originated with the specified action. The web view calls this method after the interaction occurs but before it attempts to load any content. If you implement this method, always execute the `decisionHandler` block at some point. You may execute it synchronously from your delegate method’s implementation, or execute it asynchronously after your method returns.

If your delegate object implements this method, the web view doesn’t call the [`webView(_:decidePolicyFor:decisionHandler:)`](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-2ni62.md) method.

## Parameters

- `webView`: The web view from which the navigation request began.
- `navigationAction`: Details about the action that triggered the navigation request.
- `preferences`: The default preferences to use when displaying the new webpage. Specify the default preferences for pages using the   property of   when you create your web view.
- `decisionHandler`: A completion handler block to call with the results about whether to allow or cancel the navigation. This handler has no return value and takes the following parameters:

## See Also

- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, decisionHandler: (WKNavigationActionPolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-2ni62.md)
  Asks the delegate for permission to navigate to new content based on the specified action information.
- [enum WKNavigationActionPolicy](wknavigationactionpolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from an action.
- [func webView(WKWebView, decidePolicyFor: WKNavigationResponse, decisionHandler: (WKNavigationResponsePolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-19mn2.md)
  Asks the delegate for permission to navigate to new content after the response to the navigation request is known.
- [enum WKNavigationResponsePolicy](wknavigationresponsepolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:decidepolicyfor:preferences:decisionhandler:))*