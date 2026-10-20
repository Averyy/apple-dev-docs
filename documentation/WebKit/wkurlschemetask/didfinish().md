# didFinish()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) didFinish;
```

#### Discussion

This method signals to WebKit that it has all of the resource’s data and the task is now complete. Call this method after sending a response and the resource data to WebKit using the [`didReceive(_:)`](./didreceive%28_%29-2u23r.md) and [`didReceive(_:)`](./didreceive%28_%29-8t5f8.md) methods.

This method raises an exception if you call it before the [`didReceive(_:)`](./didreceive%28_%29-2u23r.md) method, or if the task is already complete. It also raises an exception if you call it after WebKit calls the [`webView(_:stop:)`](../wkurlschemehandler/webview%28_,stop%29.md) method of the corresponding handler object.

## See Also

### Reporting Progress Back to WebKit
- [func didReceive(URLResponse)](./didreceive%28_%29-2u23r.md)
  Returns a URL response to WebKit with information about the requested resource.
- [func didReceive(Data)](./didreceive%28_%29-8t5f8.md)
  Sends some or all of the resource data to WebKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemetask/didfinish())*