# webView(_:decidePolicyFor:decisionHandler:)

**Framework**: WebKit  
**Kind**: method

Asks the delegate for permission to navigate to new content after the response to the navigation request is known.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, decidePolicyFor navigationResponse: WKNavigationResponse) async -> WKNavigationResponsePolicy
```

## Mentions

- [Replacing UIWebView in your app](replacing-uiwebview-in-your-app.md)

#### Discussion

Use this method to allow or deny a navigation request after the web view receives the response to its original URL request. The `navigationResponse` parameter contains the details of the response, including the type of data that the response contains. If you implement this method, always execute the `decisionHandler` block at some point. You may execute it synchronously from your delegate method’s implementation, or execute it asynchronously after your method returns.

## Parameters

- `webView`: The web view from which the navigation request began.
- `navigationResponse`: Descriptive information about the navigation response.
- `decisionHandler`: A completion handler block to call with the results about whether to allow or cancel the navigation. This handler has no return value and takes the following parameter:

## See Also

- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, preferences: WKWebpagePreferences, decisionHandler: (WKNavigationActionPolicy, WKWebpagePreferences) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:preferences:decisionhandler:).md)
  Asks the delegate for permission to navigate to new content based on the specified preferences and action information.
- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, decisionHandler: (WKNavigationActionPolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-2ni62.md)
  Asks the delegate for permission to navigate to new content based on the specified action information.
- [enum WKNavigationActionPolicy](wknavigationactionpolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from an action.
- [enum WKNavigationResponsePolicy](wknavigationresponsepolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-19mn2)*