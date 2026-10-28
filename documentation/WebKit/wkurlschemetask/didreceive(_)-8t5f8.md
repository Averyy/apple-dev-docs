# didReceive(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends some or all of the resource data to WebKit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func didReceive(_ data: Data)
```

```objc
- (void) didReceiveData:(NSData *) data;
```

## Discussion

Call this method to deliver any resource data back to WebKit. If you load the data incrementally, you may call this method multiple times to deliver each new portion of the data. Each time you call this method, WebKit appends the new data to any previously received data.

This method raises an exception if you call it before the [`didReceive(_:)`](./didreceive%28_%29-2u23r.md) method, or after the [`didFinish()`](./didfinish%28%29.md) method. It also raises an exception if you call it after WebKit calls the [`webView(_:stop:)`](../wkurlschemehandler/webview%28_,stop%29.md) method of the corresponding handler object.

## Parameters

- `data`: Data for the resource. This object may contain all of the data or only some of it.

## See Also

### Reporting Progress Back to WebKit
- [func didReceive(URLResponse)](./didreceive%28_%29-2u23r.md)
  Returns a URL response to WebKit with information about the requested resource.
- [func didFinish()](./didfinish%28%29.md)
  Signals the successful completion of the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemetask/didreceive(_:)-8t5f8)*