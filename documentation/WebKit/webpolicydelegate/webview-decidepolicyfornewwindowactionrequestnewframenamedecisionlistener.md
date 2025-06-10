# webView(_:decidePolicyForNewWindowAction:request:newFrameName:decisionListener:)

**Framework**: WebKit  
**Kind**: method

Decides whether to allow a targeted navigation event, such as opening a link in a new window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, decidePolicyForNewWindowAction actionInformation: [AnyHashable : Any]!, request: URLRequest!, newFrameName frameName: String!, decisionListener listener: (any WebPolicyDecisionListener)!)
```

#### Discussion

This method is invoked when a targeted navigation decision needs to be made. A targeted navigation typically opens a new window to display content.  The receiver implements a policy decision by sending one of the [`WebPolicyDecisionListener`](webpolicydecisionlistener.md) protocol messages to `listener`. This method allows delegates to modify the behavior of targeted links which normally open a new window. Delegates might do something else, such as download or present the content in a special way. If this method sends [`use()`](webpolicydecisionlistener/use().md) to `listener` then the new window will be opened, and [`webView(_:decidePolicyForNavigationAction:request:frame:decisionListener:)`](webpolicydelegate/webview(_:decidepolicyfornavigationaction:request:frame:decisionlistener:).md) will be invoked with a [`WebNavigationType.other`](webnavigationtype/other.md) as the value for the [`WebActionNavigationTypeKey`](webactionnavigationtypekey.md) key in the action dictionary.

The default behavior sends [`use()`](webpolicydecisionlistener/use().md) to `listener`.

## Parameters

- `webView`: The   object for which this object is the policy delegate.
- `actionInformation`: A description of the action that triggered the navigation request. The possible key-value pairs in this dictionary are defined in  .
- `request`: The request for which the new window action is performed.
- `frameName`: The name of the new frame that contains the content returned from the request.
- `listener`: The   object that receives the policy decision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydelegate/webview(_:decidepolicyfornewwindowaction:request:newframename:decisionlistener:))*