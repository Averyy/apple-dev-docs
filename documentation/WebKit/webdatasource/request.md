# request

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The request that was used to create the data source.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var request: NSMutableURLRequest! { get }
```

```objc
@property (nonatomic, strong, readonly) NSMutableURLRequest * request;
```

#### Discussion

This URL may be different from the original request from [`initialRequest`](./initialrequest.md).

A web view’s resource load delegate may modify requests by implementing the webView:resource:willSendRequest:redirectResponse:fromDataSource: method.

## See Also

### Getting the request and response
- [var initialRequest: URLRequest!](./initialrequest.md)
  A reference to the original request that was used to load the web content.
- [var response: URLResponse!](./response.md)
  The response for this data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/request)*