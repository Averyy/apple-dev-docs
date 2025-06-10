# WebDownloadDelegate

**Framework**: WebKit  
**Kind**: protocol

The `WebDownloadDelegate` protocol declares one additional method for delegates of [`WebDownload`](webdownload.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol WebDownloadDelegate : NSURLDownloadDelegate
```

## Topics

### Authentication messages
- [func downloadWindow(forAuthenticationSheet: WebDownload!) -> NSWindow!](webdownloaddelegate/downloadwindow(forauthenticationsheet:).md)
  Returns the window to be used by the authentication sheet.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSURLDownloadDelegate](../Foundation/NSURLDownloadDelegate.md)

## See Also

- [class WebDownload](webdownload.md)
  `WebDownload` objects initiate download client requests on behalf of a delegate. A download request involves loading the data, decoding it (if necessary), and saving it to a file. Instances of this class behave similar to `NSURLDownload` except delegates of `WebDownload` may implement an additional delegate method. The method allows the delegate to specify the window to be used for authentication sheets. If the delegate does not implement this method, the `WebDownload` object will prompt the user for authentication using the standard WebKit authentication panel, as either a sheet or window. There are no additional methods defined in this class. See [`WebDownloadDelegate`](webdownloaddelegate.md) for the delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdownloaddelegate)*