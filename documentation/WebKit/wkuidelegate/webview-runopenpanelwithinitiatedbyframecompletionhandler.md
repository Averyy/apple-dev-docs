# webView(_:runOpenPanelWith:initiatedByFrame:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Displays a file upload panel.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.12+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, runOpenPanelWith parameters: WKOpenPanelParameters, initiatedByFrame frame: WKFrameInfo) async -> [URL]?
```

#### Discussion

Implement this method to customize the upload panel. To disable file uploads, implement this method to return `nil`.

- By default on macOS, file uploads are disabled if you don’t implement this method.
- By default on iOS, file uploads are enabled if you don’t implement this method.

## Parameters

- `webView`: The web view that invokes the delegate method.
- `parameters`: The parameters that describe the file upload control.
- `frame`: The frame with the file upload control that initiates the call.
- `completionHandler`: The completion handler the system calls after a person dismisses the open panel. Pass the selected URLs if the person selects “OK”, otherwise pass  .

## See Also

- [class WKOpenPanelParameters](wkopenpanelparameters.md)
  The configuration details of a file upload control in your web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:runopenpanelwith:initiatedbyframe:completionhandler:))*