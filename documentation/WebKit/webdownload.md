# WebDownload

**Framework**: WebKit  
**Kind**: class

`WebDownload` objects initiate download client requests on behalf of a delegate. A download request involves loading the data, decoding it (if necessary), and saving it to a file. Instances of this class behave similar to `NSURLDownload` except delegates of `WebDownload` may implement an additional delegate method. The method allows the delegate to specify the window to be used for authentication sheets. If the delegate does not implement this method, the `WebDownload` object will prompt the user for authentication using the standard WebKit authentication panel, as either a sheet or window. There are no additional methods defined in this class. See [`WebDownloadDelegate`](webdownloaddelegate.md) for the delegate method.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class WebDownload
```

## Relationships

### Inherits From
- [NSURLDownload](../Foundation/NSURLDownload.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol WebDownloadDelegate](webdownloaddelegate.md)
  The `WebDownloadDelegate` protocol declares one additional method for delegates of [`WebDownload`](webdownload.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdownload)*