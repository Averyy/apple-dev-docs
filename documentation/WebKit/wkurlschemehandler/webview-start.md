# webView(_:start:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Asks your handler to begin loading the data for the specified resource.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func webView(_ webView: WKWebView, start urlSchemeTask: any WKURLSchemeTask)
```

#### Discussion

When a web view encounters a resource with your custom URL scheme, it calls this method on the appropriate handler object. Use your implementation of this method to begin loading the resource. Call the methods of the provided [`WKURLSchemeTask`](wkurlschemetask.md) object to report the progress of the loading operation back to the web view. You also use that object to deliver the resource data to the web view.

## Parameters

- `webView`: The web view that requires the resource.
- `urlSchemeTask`: The task object that identifies the resource to load. You also use this object to report the progress of the load operation back to the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemehandler/webview(_:start:))*