# reloadFromOrigin()

**Framework**: WebKit  
**Kind**: method

Performs an end-to-end revalidation using cache-validating conditionals if possible.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func reloadFromOrigin()
```

#### Discussion

End-to-end reload may be necessary if the cache entry has become corrupted for some reason.

## See Also

- [func load(URLRequest!)](webframe/load(_:)-47p2s.md)
  Connects to a given URL by initiating an asynchronous client request.
- [func reload()](webframe/reload.md)
  Reloads the initial request passed as an argument to [`load(_:)`](webframe/load(_:)-47p2s.md).
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/reloadfromorigin())*