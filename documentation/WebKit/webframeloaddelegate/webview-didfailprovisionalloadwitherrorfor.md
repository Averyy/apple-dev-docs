# webView(_:didFailProvisionalLoadWithError:for:)

**Framework**: Webkit  
**Kind**: method

Called if an error occurs when starting to load data for a page.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, didFailProvisionalLoadWithError error: (any Error)!, for frame: WebFrame!)
```

#### Discussion

The frame continues to display the committed data source if there is one.

## Parameters

- `sender`: The web view containing the frame.
- `error`: Specifies the type of error that occurred during the load.
- `frame`: The frame being loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didfailprovisionalloadwitherror:for:))*