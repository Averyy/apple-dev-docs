# load(_:)

**Framework**: Webkit  
**Kind**: method

Connects to a given URL by initiating an asynchronous client request.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func load(_ request: URLRequest!)
```

#### Discussion

Creates a provisional data source that will transition to a committed data source once any data has been received. Use the [`dataSource`](webframe/datasource.md) method to check if a committed data source is available, and the [`stopLoading()`](webframe/stoploading().md) method to stop the load. This method is typically invoked on the main frame.

## Parameters

- `request`: A client request.

## See Also

- [func reload()](webframe/reload.md)
  Reloads the initial request passed as an argument to [`load(_:)`](webframe/load(_:)-47p2s.md).
- [func reloadFromOrigin()](webframe/reloadfromorigin.md)
  Performs an end-to-end revalidation using cache-validating conditionals if possible.
- [func stopLoading()](webframe/stoploading.md)
  Stops any pending loads on the receiver’s data source, and those of its children.
- [func loadAlternateHTMLString(String!, baseURL: URL!, forUnreachableURL: URL!)](webframe/loadalternatehtmlstring(_:baseurl:forunreachableurl:).md)
  Loads alternate content for a frame whose URL is unreachable.
- [func loadHTMLString(String!, baseURL: URL!)](webframe/loadhtmlstring(_:baseurl:).md)
  Sets the main page contents and base URL.
- [func load(Data!, mimeType: String!, textEncodingName: String!, baseURL: URL!)](webframe/load(_:mimetype:textencodingname:baseurl:).md)
  Sets the main page contents, MIME type, content encoding, and base URL.
- [func load(WebArchive!)](webframe/load(_:)-6wkx6.md)
  Loads an archive into the web frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/load(_:)-47p2s)*