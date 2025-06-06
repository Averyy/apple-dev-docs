# webView(_:runOpenPanelWith:initiatedByFrame:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Displays a file upload panel.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.12+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, runOpenPanelWith parameters: WKOpenPanelParameters, initiatedByFrame frame: WKFrameInfo) async -> [URL]?
```

#### Discussion

If this method is not implemented, the web view behaves as if the user selected the Cancel button.

## Parameters

- `webView`: The web view invoking the delegate method.
- `parameters`: The parameters describing the file upload control.
- `frame`: The frame whose file upload control initiated the call.
- `completionHandler`: The completion handler called after the open panel has been dismissed. Pass the selected URLs if the user chose “OK”, otherwise  .

## See Also

- [class WKOpenPanelParameters](wkopenpanelparameters.md)
  The configuration details of a file upload control in your web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:runopenpanelwith:initiatedbyframe:completionhandler:))*