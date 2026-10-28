# loadHTMLString(_:baseURL:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the main page content and base URL.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
func loadHTMLString(_ string: String, baseURL: URL?)
```

```objc
- (void) loadHTMLString:(NSString *) string baseURL:(NSURL *) baseURL;
```

## Discussion

To help you avoid being vulnerable to security attacks, be sure to use this method to load local HTML files; don’t use [`loadRequest(_:)`](./loadrequest%28_%29.md).

## Parameters

- `string`: The content for the main page.
- `baseURL`: The base URL for the content.

## See Also

### Loading content
- [func load(Data, mimeType: String, textEncodingName: String, baseURL: URL)](./load%28_,mimetype,textencodingname,baseurl%29.md)
  Sets the main page contents, MIME type, content encoding, and base URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/loadhtmlstring(_:baseurl:))*