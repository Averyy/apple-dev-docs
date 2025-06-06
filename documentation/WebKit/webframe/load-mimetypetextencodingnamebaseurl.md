# load(_:mimeType:textEncodingName:baseURL:)

**Framework**: Webkit  
**Kind**: method

Sets the main page contents, MIME type, content encoding, and base URL.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func load(_ data: Data!, mimeType MIMEType: String!, textEncodingName encodingName: String!, baseURL URL: URL!)
```

## Parameters

- `data`: The data to use for the main page of the document.
- `MIMEType`: The MIME type of the data.
- `encodingName`: The IANA encoding name (for example, “utf-8” or “utf-16”).
- `URL`: A file that is used to resolve relative URLs within the document.

## See Also

- [func load(URLRequest!)](webframe/load(_:)-47p2s.md)
  Connects to a given URL by initiating an asynchronous client request.
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
- [func load(WebArchive!)](webframe/load(_:)-6wkx6.md)
  Loads an archive into the web frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/load(_:mimetype:textencodingname:baseurl:))*