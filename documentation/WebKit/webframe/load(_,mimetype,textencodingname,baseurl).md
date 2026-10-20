# load(_:mimeType:textEncodingName:baseURL:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the main page contents, MIME type, content encoding, and base URL.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func load(_ data: Data!, mimeType MIMEType: String!, textEncodingName encodingName: String!, baseURL URL: URL!)
```

```objc
- (void) loadData:(NSData *) data MIMEType:(NSString *) MIMEType textEncodingName:(NSString *) encodingName baseURL:(NSURL *) URL;
```

## Parameters

- `data`: The data to use for the main page of the document.
- `MIMEType`: The MIME type of the data.
- `encodingName`: The IANA encoding name (for example, “utf-8” or “utf-16”).
- `URL`: A file that is used to resolve relative URLs within the document.

## See Also

### Loading Content
- [func load(URLRequest!)](./load%28_%29-47p2s.md)
  Connects to a given URL by initiating an asynchronous client request.
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
- [func load(WebArchive!)](./load%28_%29-6wkx6.md)
  Loads an archive into the web frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/load(_:mimetype:textencodingname:baseurl:))*