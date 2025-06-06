# webView(_:identifierForInitialRequest:from:)

**Framework**: Webkit  
**Kind**: method

Returns an identifier object used to track the progress of loading a single resource.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, identifierForInitialRequest request: URLRequest!, from dataSource: WebDataSource!) -> Any!
```

#### Return Value

An identifier object that is retained by `sender` and passed as a parameter to all other delegate messages pertaining to this resource.

#### Discussion

Delegates might implement this method to begin tracking the progress of loading an individual resource. Note that this method is invoked once per load where as the [`webView(_:resource:willSend:redirectResponse:from:)`](webresourceloaddelegate/webview(_:resource:willsend:redirectresponse:from:).md) method may be invoked multiple times.

## Parameters

- `sender`: The web view that sent this message.
- `request`: The request that initiated this load for  .
- `dataSource`: The data source for this web view.

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webresourceloaddelegate/webview(_:identifierforinitialrequest:from:))*