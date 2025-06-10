# webView(_:didFailLoadWithError:for:)

**Framework**: WebKit  
**Kind**: method

Called when an error occurs loading a committed data source.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, didFailLoadWithError error: (any Error)!, for frame: WebFrame!)
```

#### Discussion

This method is called after the data source has been committed but resulted in an error.

## Parameters

- `sender`: The web view containing the frame.
- `error`: The type of error that occurred during the load.
- `frame`: The frame being loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didfailloadwitherror:for:))*