# request

**Framework**: Webkit  
**Kind**: property

The request that was used to create the data source.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var request: NSMutableURLRequest! { get }
```

#### Discussion

This URL may be different from the original request from [`initialRequest`](webdatasource/initialrequest.md).

A web view’s resource load delegate may modify requests by implementing the webView:resource:willSendRequest:redirectResponse:fromDataSource: method.

## See Also

- [var initialRequest: URLRequest!](webdatasource/initialrequest.md)
  A reference to the original request that was used to load the web content.
- [var response: URLResponse!](webdatasource/response.md)
  The response for this data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/request)*