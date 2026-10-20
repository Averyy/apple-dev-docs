# load(_:mimeType:textEncodingName:baseURL:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the main page contents, MIME type, content encoding, and base URL.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
func load(_ data: Data, mimeType MIMEType: String, textEncodingName: String, baseURL: URL)
```

```objc
- (void) loadData:(NSData *) data MIMEType:(NSString *) MIMEType textEncodingName:(NSString *) textEncodingName baseURL:(NSURL *) baseURL;
```

## Parameters

- `data`: The content for the main page.
- `MIMEType`: The MIME type of the content.
- `textEncodingName`: The IANA encoding name as in `utf-8` or `utf-16`.
- `baseURL`: The base URL for the content.

## See Also

### Loading content
- [func loadHTMLString(String, baseURL: URL?)](./loadhtmlstring%28_,baseurl%29.md)
  Sets the main page content and base URL.
- [func loadRequest(URLRequest)](./loadrequest%28_%29.md)
  Connects to a given URL by initiating an asynchronous client request.
- [var request: URLRequest?](./request.md)
  The URL request identifying the location of the content to load.
- [var isLoading: Bool](./isloading.md)
  A Boolean value indicating whether the receiver is done loading content.
- [func stopLoading()](./stoploading%28%29.md)
  Stops the loading of any web content managed by the receiver.
- [func reload()](./reload%28%29.md)
  Reloads the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/load(_:mimetype:textencodingname:baseurl:))*