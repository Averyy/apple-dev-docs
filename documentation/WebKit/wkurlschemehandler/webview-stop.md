# webView(_:stop:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Asks your handler to stop loading the data for the specified resource.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func webView(_ webView: WKWebView, stop urlSchemeTask: any WKURLSchemeTask)
```

#### Discussion

If WebKit determines that it no longer needs a resource that your handler is loading, it calls this method to stop the load operation. Typically, WebKit calls this method when the user navigates to another page, but may call it for other reasons.

When WebKit calls this method, stop the load operation immediately for the specified resource and free up any allocated memory for it. Don’t call any methods of the provided `urlSchemeTask` object to report your progress back to WebKit. If you do, the methods of that object raise an exception.

## Parameters

- `webView`: The web view that asked you to stop loading the resource.
- `urlSchemeTask`: The task object that identifies the resource the web view no longer needs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemehandler/webview(_:stop:))*