# didReceive(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a URL response to WebKit with information about the requested resource.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func didReceive(_ response: URLResponse)
```

```objc
- (void) didReceiveResponse:(NSURLResponse *) response;
```

## Discussion

Call this method to provide WebKit with the MIME type of the requested resource and its expected size. You must call this method at least once for each task, and you may call it multiple times if needed. Always call it before sending any data back to WebKit using the [`didReceive(_:)`](./didreceive%28_%29-8t5f8.md) method.

It is a programmer error to call this method after calling the [`didFinish()`](./didfinish%28%29.md) method of the same task object. It is also a programmer error to call this method after WebKit calls the [`webView(_:stop:)`](../wkurlschemehandler/webview%28_,stop%29.md) method of the corresponding handler object. If you do, this method raises an exception in both cases.

## Parameters

- `response`: The response to return to WebKit. Your response object must include the MIME type of the requested resource.

## See Also

### Reporting Progress Back to WebKit
- [func didReceive(Data)](./didreceive%28_%29-8t5f8.md)
  Sends some or all of the resource data to WebKit.
- [func didFinish()](./didfinish%28%29.md)
  Signals the successful completion of the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemetask/didreceive(_:)-2u23r)*