# webView(_:decidePolicyForNavigationAction:request:frame:decisionListener:)

**Framework**: WebKit  
**Kind**: method

Routes a navigation action internally or to an external viewer.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, decidePolicyForNavigationAction actionInformation: [AnyHashable : Any]!, request: URLRequest!, frame: WebFrame!, decisionListener listener: (any WebPolicyDecisionListener)!)
```

#### Discussion

This method is invoked when a navigation decision needs to be made. The web view implements a policy decision by sending one of the [`WebPolicyDecisionListener`](webpolicydecisionlistener.md) protocol messages to `listener`. This method is invoked whenever a server redirect is encountered, and before loading starts.

If you do not implement this method, the default behavior is used. The listener handles the navigation internally if the request is for an error page or if the [`canHandle(_:)`](https://developer.apple.com/documentation/Foundation/NSURLConnection/canHandle(_:)) method of the `NSURLConnection` class returns [`true`](https://developer.apple.com/documentation/swift/true) when passed `request`. Otherwise, the listener ignores the navigation, and it is handled externally.

## Parameters

- `webView`: The   object for which this object is the policy delegate.
- `actionInformation`: A description of the action that triggered the navigation request. The possible key-value pairs in this dictionary are defined in  .
- `request`: The request for which the navigation is made.
- `frame`: The   object in which the action occurred.
- `listener`: The   object that receives the policy decision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydelegate/webview(_:decidepolicyfornavigationaction:request:frame:decisionlistener:))*