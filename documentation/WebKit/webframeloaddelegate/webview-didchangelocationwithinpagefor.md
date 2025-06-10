# webView(_:didChangeLocationWithinPageFor:)

**Framework**: WebKit  
**Kind**: method

Called when the scroll position within a frame changes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, didChangeLocationWithinPageFor frame: WebFrame!)
```

#### Discussion

Typically invoked when the user clicks on an anchor within a page. Additional information about the request can be obtained from the data source of `frame`.

## Parameters

- `sender`: The web view containing the frame.
- `frame`: The frame being loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didchangelocationwithinpagefor:))*