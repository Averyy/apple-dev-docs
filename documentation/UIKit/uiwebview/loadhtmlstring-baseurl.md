# loadHTMLString(_:baseURL:)

**Framework**: UIKit  
**Kind**: method

Sets the main page content and base URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
func loadHTMLString(_ string: String, baseURL: URL?)
```

#### Discussion

To help you avoid being vulnerable to security attacks, be sure to use this method to load local HTML files; don’t use [`loadRequest(_:)`](uiwebview/loadrequest(_:).md).

## Parameters

- `string`: The content for the main page.
- `baseURL`: The base URL for the content.

## See Also

- [func load(Data, mimeType: String, textEncodingName: String, baseURL: URL)](uiwebview/load(_:mimetype:textencodingname:baseurl:).md)
  Sets the main page contents, MIME type, content encoding, and base URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/loadhtmlstring(_:baseurl:))*