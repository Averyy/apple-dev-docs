# loadRequest(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Connects to a given URL by initiating an asynchronous client request.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
func loadRequest(_ request: URLRequest)
```

```objc
- (void) loadRequest:(NSURLRequest *) request;
```

## Discussion

Don’t use this method to load local HTML files; instead, use [`loadHTMLString(_:baseURL:)`](./loadhtmlstring%28_,baseurl%29.md). To stop this load, use the [`stopLoading()`](./stoploading%28%29.md) method. To see whether the receiver is done loading the content, use the [`isLoading`](./isloading.md) property.

## Parameters

- `request`: A URL request identifying the location of the content to load.

## See Also

### Loading content
- [func load(Data, mimeType: String, textEncodingName: String, baseURL: URL)](./load%28_,mimetype,textencodingname,baseurl%29.md)
  Sets the main page contents, MIME type, content encoding, and base URL.
- [func loadHTMLString(String, baseURL: URL?)](./loadhtmlstring%28_,baseurl%29.md)
  Sets the main page content and base URL.
- [var request: URLRequest?](./request.md)
  The URL request identifying the location of the content to load.
- [var isLoading: Bool](./isloading.md)
  A Boolean value indicating whether the receiver is done loading content.
- [func stopLoading()](./stoploading%28%29.md)
  Stops the loading of any web content managed by the receiver.
- [func reload()](./reload%28%29.md)
  Reloads the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/loadrequest(_:))*