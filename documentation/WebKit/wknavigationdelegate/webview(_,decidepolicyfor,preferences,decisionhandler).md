# webView(_:decidePolicyFor:preferences:decisionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for permission to navigate to new content based on the specified preferences and action information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, preferences: WKWebpagePreferences, decisionHandler: @escaping @MainActor @Sendable (WKNavigationActionPolicy, WKWebpagePreferences) -> Void)
```

```swift
optional func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, preferences: WKWebpagePreferences) async -> (WKNavigationActionPolicy, WKWebpagePreferences)
```

```objc
- (void) webView:(WKWebView *) webView decidePolicyForNavigationAction:(WKNavigationAction *) navigationAction preferences:(WKWebpagePreferences *) preferences decisionHandler:(void (^)(enum WKNavigationActionPolicy, WKWebpagePreferences *)) decisionHandler;
```

#### Discussion

Use this method to allow or deny a navigation request that originated with the specified action. The web view calls this method after the interaction occurs but before it attempts to load any content. If you implement this method, always execute the `decisionHandler` block at some point. You may execute it synchronously from your delegate method’s implementation, or execute it asynchronously after your method returns.

If your delegate object implements this method, the web view doesn’t call the [`webView(_:decidePolicyFor:decisionHandler:)`](./webview%28_,decidepolicyfor,decisionhandler%29-2ni62.md) method.

## Parameters

- `webView`: The web view from which the navigation request began.
- `navigationAction`: Details about the action that triggered the navigation request.
- `preferences`: The default preferences to use when displaying the new webpage. Specify the default preferences for pages using the [`defaultWebpagePreferences`](../wkwebviewconfiguration/defaultwebpagepreferences.md) property of [`WKWebViewConfiguration`](../wkwebviewconfiguration.md) when you create your web view.
- `decisionHandler`: A completion handler block to call with the results about whether to allow or cancel the navigation. This handler has no return value and takes the following parameters:

  - **policy**: A constant that indicates whether to cancel or allow the navigation. For a list of possible values, see [`WKNavigationActionPolicy`](../wknavigationactionpolicy.md).
  - **preferences**: The set of preferences to apply to the page if the navigation is allowed. You may pass the object from the `preferences` parameter or configure a new preferences object and pass it instead.

## See Also

### Allowing or denying navigation requests
- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, decisionHandler: (WKNavigationActionPolicy) -> Void)](./webview%28_,decidepolicyfor,decisionhandler%29-2ni62.md)
  Asks the delegate for permission to navigate to new content based on the specified action information.
- [enum WKNavigationActionPolicy](../wknavigationactionpolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from an action.
- [func webView(WKWebView, decidePolicyFor: WKNavigationResponse, decisionHandler: (WKNavigationResponsePolicy) -> Void)](./webview%28_,decidepolicyfor,decisionhandler%29-19mn2.md)
  Asks the delegate for permission to navigate to new content after the response to the navigation request is known.
- [enum WKNavigationResponsePolicy](../wknavigationresponsepolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:decidepolicyfor:preferences:decisionhandler:))*