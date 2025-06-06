# WebPolicyDelegate

**Framework**: Webkit  
**Kind**: protocol

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol WebPolicyDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func webView(WebView!, decidePolicyForMIMEType: String!, request: URLRequest!, frame: WebFrame!, decisionListener: (any WebPolicyDecisionListener)!)](webpolicydelegate/webview(_:decidepolicyformimetype:request:frame:decisionlistener:).md)
  Decides whether to display content with a given MIME type.
- [func webView(WebView!, decidePolicyForNavigationAction: [AnyHashable : Any]!, request: URLRequest!, frame: WebFrame!, decisionListener: (any WebPolicyDecisionListener)!)](webpolicydelegate/webview(_:decidepolicyfornavigationaction:request:frame:decisionlistener:).md)
  Routes a navigation action internally or to an external viewer.
- [func webView(WebView!, decidePolicyForNewWindowAction: [AnyHashable : Any]!, request: URLRequest!, newFrameName: String!, decisionListener: (any WebPolicyDecisionListener)!)](webpolicydelegate/webview(_:decidepolicyfornewwindowaction:request:newframename:decisionlistener:).md)
  Decides whether to allow a targeted navigation event, such as opening a link in a new window.
- [func webView(WebView!, unableToImplementPolicyWithError: (any Error)!, frame: WebFrame!)](webpolicydelegate/webview(_:unabletoimplementpolicywitherror:frame:).md)
  Handles or drops events that were rejected by a policy maker.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
- [protocol WebPolicyDecisionListener](webpolicydecisionlistener.md)
  This protocol enables [`WebView`](webview.md) policy delegates to communicate with listener objects. A listener object conforming to this protocol is passed as one of the arguments to web view policy delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydelegate)*