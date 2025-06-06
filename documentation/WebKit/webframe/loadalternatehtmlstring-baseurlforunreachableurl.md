# loadAlternateHTMLString(_:baseURL:forUnreachableURL:)

**Framework**: Webkit  
**Kind**: method

Loads alternate content for a frame whose URL is unreachable.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func loadAlternateHTMLString(_ string: String!, baseURL: URL!, forUnreachableURL unreachableURL: URL!)
```

#### Discussion

Use this method to display page-level loading errors in a web view. Typically, a `WebFrameLoadDelegate` or `WebPolicyDelegate` object invokes this method from these methods: `webView:didFailProvisionalLoadWithError:forFrame:` (`WebFrameLoadDelegate`), webView:decidePolicyForMIMEType:request:frame:decisionListener: (`WebPolicyDelegate`), or [`webView(_:unableToImplementPolicyWithError:frame:)`](webpolicydelegate/webview(_:unabletoimplementpolicywitherror:frame:).md) (`WebPolicyDelegate`). If invoked from one of these methods, the back-forward list is maintained.

## Parameters

- `string`: The string to use as the main page for the document.
- `baseURL`: A file that is used to resolve relative URLs within the document.
- `unreachableURL`: The URL for the alternate page content.

## See Also

- [func load(URLRequest!)](webframe/load(_:)-47p2s.md)
  Connects to a given URL by initiating an asynchronous client request.
- [func reload()](webframe/reload.md)
  Reloads the initial request passed as an argument to [`load(_:)`](webframe/load(_:)-47p2s.md).
- [func reloadFromOrigin()](webframe/reloadfromorigin.md)
  Performs an end-to-end revalidation using cache-validating conditionals if possible.
- [func stopLoading()](webframe/stoploading.md)
  Stops any pending loads on the receiver’s data source, and those of its children.
- [func loadHTMLString(String!, baseURL: URL!)](webframe/loadhtmlstring(_:baseurl:).md)
  Sets the main page contents and base URL.
- [func load(Data!, mimeType: String!, textEncodingName: String!, baseURL: URL!)](webframe/load(_:mimetype:textencodingname:baseurl:).md)
  Sets the main page contents, MIME type, content encoding, and base URL.
- [func load(WebArchive!)](webframe/load(_:)-6wkx6.md)
  Loads an archive into the web frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/loadalternatehtmlstring(_:baseurl:forunreachableurl:))*