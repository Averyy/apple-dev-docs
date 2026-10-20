# initialRequest

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A reference to the original request that was used to load the web content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var initialRequest: URLRequest! { get }
```

```objc
@property (nonatomic, strong, readonly) NSURLRequest * initialRequest;
```

## See Also

### Getting the request and response
- [var request: NSMutableURLRequest!](./request.md)
  The request that was used to create the data source.
- [var response: URLResponse!](./response.md)
  The response for this data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/initialrequest)*