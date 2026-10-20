# response

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The response for this data source.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var response: URLResponse! { get }
```

```objc
@property (nonatomic, strong, readonly) NSURLResponse * response;
```

## See Also

### Getting the request and response
- [var initialRequest: URLRequest!](./initialrequest.md)
  A reference to the original request that was used to load the web content.
- [var request: NSMutableURLRequest!](./request.md)
  The request that was used to create the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/response)*