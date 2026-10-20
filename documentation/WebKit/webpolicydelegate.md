# WebPolicyDelegate

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebPolicyDelegate : NSObjectProtocol
```

```objc
@protocol WebPolicyDelegate <NSObject>
```

## Topics

### Instance Methods
- [func webView(WebView!, decidePolicyForMIMEType: String!, request: URLRequest!, frame: WebFrame!, decisionListener: (any WebPolicyDecisionListener)!)](./webpolicydelegate/webview%28_,decidepolicyformimetype,request,frame,decisionlistener%29.md)
  Decides whether to display content with a given MIME type.
- [func webView(WebView!, decidePolicyForNavigationAction: [AnyHashable : Any]!, request: URLRequest!, frame: WebFrame!, decisionListener: (any WebPolicyDecisionListener)!)](./webpolicydelegate/webview%28_,decidepolicyfornavigationaction,request,frame,decisionlistener%29.md)
  Routes a navigation action internally or to an external viewer.
- [func webView(WebView!, decidePolicyForNewWindowAction: [AnyHashable : Any]!, request: URLRequest!, newFrameName: String!, decisionListener: (any WebPolicyDecisionListener)!)](./webpolicydelegate/webview%28_,decidepolicyfornewwindowaction,request,newframename,decisionlistener%29.md)
  Decides whether to allow a targeted navigation event, such as opening a link in a new window.
- [func webView(WebView!, unableToImplementPolicyWithError: (any Error)!, frame: WebFrame!)](./webpolicydelegate/webview%28_,unabletoimplementpolicywitherror,frame%29.md)
  Handles or drops events that were rejected by a policy maker.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
### Setting Policies (Legacy)
- [protocol WebPolicyDecisionListener](./webpolicydecisionlistener.md)
  This protocol enables [`WebView`](./webview-swift.class.md) policy delegates to communicate with listener objects. A listener object conforming to this protocol is passed as one of the arguments to web view policy delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydelegate)*