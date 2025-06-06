# didFinish()

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Signals the successful completion of the task.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func didFinish()
```

#### Discussion

This method signals to WebKit that it has all of the resource’s data and the task is now complete. Call this method after sending a response and the resource data to WebKit using the [`didReceive(_:)`](wkurlschemetask/didreceive(_:)-2u23r.md) and [`didReceive(_:)`](wkurlschemetask/didreceive(_:)-8t5f8.md) methods.

This method raises an exception if you call it before the [`didReceive(_:)`](wkurlschemetask/didreceive(_:)-2u23r.md) method, or if the task is already complete. It also raises an exception if you call it after WebKit calls the [`webView(_:stop:)`](wkurlschemehandler/webview(_:stop:).md) method of the corresponding handler object.

## See Also

- [func didReceive(URLResponse)](wkurlschemetask/didreceive(_:)-2u23r.md)
  Returns a URL response to WebKit with information about the requested resource.
- [func didReceive(Data)](wkurlschemetask/didreceive(_:)-8t5f8.md)
  Sends some or all of the resource data to WebKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemetask/didfinish())*