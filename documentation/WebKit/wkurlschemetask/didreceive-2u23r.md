# didReceive(_:)

**Framework**: Webkit  
**Kind**: method  
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

#### Discussion

Call this method to provide WebKit with the MIME type of the requested resource and its expected size. You must call this method at least once for each task, and you may call it multiple times if needed. Always call it before sending any data back to WebKit using the [`didReceive(_:)`](wkurlschemetask/didreceive(_:)-8t5f8.md) method.

It is a programmer error to call this method after calling the [`didFinish()`](wkurlschemetask/didfinish().md) method of the same task object. It is also a programmer error to call this method after WebKit calls the [`webView(_:stop:)`](wkurlschemehandler/webview(_:stop:).md) method of the corresponding handler object. If you do, this method raises an exception in both cases.

## Parameters

- `response`: The response to return to WebKit. Your response object must include the MIME type of the requested resource.

## See Also

- [func didReceive(Data)](wkurlschemetask/didreceive(_:)-8t5f8.md)
  Sends some or all of the resource data to WebKit.
- [func didFinish()](wkurlschemetask/didfinish.md)
  Signals the successful completion of the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemetask/didreceive(_:)-2u23r)*