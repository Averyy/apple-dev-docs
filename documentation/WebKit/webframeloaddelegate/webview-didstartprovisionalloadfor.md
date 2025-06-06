# webView(_:didStartProvisionalLoadFor:)

**Framework**: Webkit  
**Kind**: method

Called when a page load is in progress in a given frame.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, didStartProvisionalLoadFor frame: WebFrame!)
```

#### Discussion

This method is invoked when a new client request is made by `sender` to load a provisional data source for `frame`. This method may be invoked after sending [`load(_:)`](webframe/load(_:)-47p2s.md) to a `WebFrame` object or as a consequence of the user clicking a link displayed in a web frame view. Delegates might implement this method to notify the user that a request is in progress. Additional information about the request can be obtained from the data source of `frame`.

## Parameters

- `sender`: The web view containing the frame.
- `frame`: The frame being loaded.

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didstartprovisionalloadfor:))*