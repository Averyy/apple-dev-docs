# webView(_:unableToImplementPolicyWithError:frame:)

**Framework**: WebKit  
**Kind**: method

Handles or drops events that were rejected by a policy maker.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, unableToImplementPolicyWithError error: (any Error)!, frame: WebFrame!)
```

#### Discussion

Delegates might implement this method to display or log an error message. If you do not implement this method, no action is taken.

## Parameters

- `webView`: The   object for which this object is the policy delegate.
- `error`: The error that occurred.
- `frame`: The frame in which the error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydelegate/webview(_:unabletoimplementpolicywitherror:frame:))*