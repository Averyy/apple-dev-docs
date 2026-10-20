# webView(_:willPerformClientRedirectTo:delay:fire:for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when a frame receives a client redirect and before it is fired.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, willPerformClientRedirectTo URL: URL!, delay seconds: TimeInterval, fire date: Date!, for frame: WebFrame!)
```

```objc
- (void) webView:(WebView *) sender willPerformClientRedirectToURL:(NSURL *) URL delay:(NSTimeInterval) seconds fireDate:(NSDate *) date forFrame:(WebFrame *) frame;
```

#### Discussion

Delegates might implement this method to display progress while a client redirect is pending. If a client redirect is cancelled the [`webView(_:didCancelClientRedirectFor:)`](./webview%28_,didcancelclientredirectfor%29.md) delegate method is invoked.

## Parameters

- `sender`: The web view containing the frame.
- `URL`: The redirect location.
- `seconds`: The number of seconds from `date` before the redirect will be fired.
- `date`: The date and time to call the redirect.
- `frame`: The frame where the redirect occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:willperformclientredirectto:delay:fire:for:))*