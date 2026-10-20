# reload()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the current page.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
func reload()
```

```objc
- (void) reload;
```

## See Also

### Loading content
- [func load(Data, mimeType: String, textEncodingName: String, baseURL: URL)](./load%28_,mimetype,textencodingname,baseurl%29.md)
  Sets the main page contents, MIME type, content encoding, and base URL.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/reload())*