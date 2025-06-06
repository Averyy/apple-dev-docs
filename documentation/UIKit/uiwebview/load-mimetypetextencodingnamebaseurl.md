# load(_:mimeType:textEncodingName:baseURL:)

**Framework**: UIKit  
**Kind**: method

Sets the main page contents, MIME type, content encoding, and base URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
func load(_ data: Data, mimeType MIMEType: String, textEncodingName: String, baseURL: URL)
```

## Parameters

- `data`: The content for the main page.
- `MIMEType`: The MIME type of the content.
- `textEncodingName`: The IANA encoding name as in   or  .
- `baseURL`: The base URL for the content.

## See Also

- [func loadHTMLString(String, baseURL: URL?)](uiwebview/loadhtmlstring(_:baseurl:).md)
  Sets the main page content and base URL.
- [func loadRequest(URLRequest)](uiwebview/loadrequest(_:).md)
  Connects to a given URL by initiating an asynchronous client request.
- [var request: URLRequest?](uiwebview/request.md)
  The URL request identifying the location of the content to load.
- [var isLoading: Bool](uiwebview/isloading.md)
  A Boolean value indicating whether the receiver is done loading content.
- [func stopLoading()](uiwebview/stoploading.md)
  Stops the loading of any web content managed by the receiver.
- [func reload()](uiwebview/reload.md)
  Reloads the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/load(_:mimetype:textencodingname:baseurl:))*