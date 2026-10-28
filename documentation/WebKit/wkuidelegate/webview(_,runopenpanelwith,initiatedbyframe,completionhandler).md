# webView(_:runOpenPanelWith:initiatedByFrame:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays a file upload panel.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.12+
- visionOS 2.4+

## Declaration

```swift
optional func webView(_ webView: WKWebView, runOpenPanelWith parameters: WKOpenPanelParameters, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping @MainActor @Sendable ([URL]?) -> Void)
```

```swift
optional func webView(_ webView: WKWebView, runOpenPanelWith parameters: WKOpenPanelParameters, initiatedByFrame frame: WKFrameInfo) async -> [URL]?
```

```objc
- (void) webView:(WKWebView *) webView runOpenPanelWithParameters:(WKOpenPanelParameters *) parameters initiatedByFrame:(WKFrameInfo *) frame completionHandler:(void (^)(NSArray<NSURL *> *)) completionHandler;
```

## Discussion

Implement this method to customize the upload panel. To disable file uploads, implement this method to return `nil`.

- By default on macOS, file uploads are disabled if you don’t implement this method.
- By default on iOS, file uploads are enabled if you don’t implement this method.

## Parameters

- `webView`: The web view that invokes the delegate method.
- `parameters`: The parameters that describe the file upload control.
- `frame`: The frame with the file upload control that initiates the call.
- `completionHandler`: The completion handler the system calls after a person dismisses the open panel. Pass the selected URLs if the person selects “OK”, otherwise pass `nil`.

## See Also

### Displaying an upload panel
- [class WKOpenPanelParameters](../wkopenpanelparameters.md)
  The configuration details of a file upload control in your web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:runopenpanelwith:initiatedbyframe:completionhandler:))*