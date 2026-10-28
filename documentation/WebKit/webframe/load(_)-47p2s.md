# load(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Connects to a given URL by initiating an asynchronous client request.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func load(_ request: URLRequest!)
```

```objc
- (void) loadRequest:(NSURLRequest *) request;
```

## Discussion

Creates a provisional data source that will transition to a committed data source once any data has been received. Use the [`dataSource`](./datasource.md) method to check if a committed data source is available, and the [`stopLoading()`](./stoploading%28%29.md) method to stop the load. This method is typically invoked on the main frame.

## Parameters

- `request`: A client request.

## See Also

### Loading Content
- [func reload()](./reload%28%29.md)
  Reloads the initial request passed as an argument to [`load(_:)`](./load%28_%29-47p2s.md).
- [func reloadFromOrigin()](./reloadfromorigin%28%29.md)
  Performs an end-to-end revalidation using cache-validating conditionals if possible.
- [func stopLoading()](./stoploading%28%29.md)
  Stops any pending loads on the receiver’s data source, and those of its children.
- [func loadAlternateHTMLString(String!, baseURL: URL!, forUnreachableURL: URL!)](./loadalternatehtmlstring%28_,baseurl,forunreachableurl%29.md)
  Loads alternate content for a frame whose URL is unreachable.
- [func loadHTMLString(String!, baseURL: URL!)](./loadhtmlstring%28_,baseurl%29.md)
  Sets the main page contents and base URL.
- [func load(Data!, mimeType: String!, textEncodingName: String!, baseURL: URL!)](./load%28_,mimetype,textencodingname,baseurl%29.md)
  Sets the main page contents, MIME type, content encoding, and base URL.
- [func load(WebArchive!)](./load%28_%29-6wkx6.md)
  Loads an archive into the web frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/load(_:)-47p2s)*