# webView(_:didReceiveIcon:for:)

**Framework**: Webkit  
**Kind**: method

Called when a page icon changes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, didReceiveIcon image: NSImage!, for frame: WebFrame!)
```

#### Discussion

This method may be invoked multiple times before all resources for `frame` are completely loaded. Sometimes a page uses a default icon or stored image that changes when the actual images is loaded.

## Parameters

- `sender`: The web view containing the frame.
- `image`: The page icon for a data source.
- `frame`: The frame being loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didreceiveicon:for:))*