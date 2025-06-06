# loadRequest(_:)

**Framework**: UIKit  
**Kind**: method

Connects to a given URL by initiating an asynchronous client request.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
func loadRequest(_ request: URLRequest)
```

#### Discussion

Don’t use this method to load local HTML files; instead, use [`loadHTMLString(_:baseURL:)`](uiwebview/loadhtmlstring(_:baseurl:).md). To stop this load, use the [`stopLoading()`](uiwebview/stoploading().md) method. To see whether the receiver is done loading the content, use the [`isLoading`](uiwebview/isloading.md) property.

## Parameters

- `request`: A URL request identifying the location of the content to load.

## See Also

- [func load(Data, mimeType: String, textEncodingName: String, baseURL: URL)](uiwebview/load(_:mimetype:textencodingname:baseurl:).md)
  Sets the main page contents, MIME type, content encoding, and base URL.
- [func loadHTMLString(String, baseURL: URL?)](uiwebview/loadhtmlstring(_:baseurl:).md)
  Sets the main page content and base URL.
- [var request: URLRequest?](uiwebview/request.md)
  The URL request identifying the location of the content to load.
- [var isLoading: Bool](uiwebview/isloading.md)
  A Boolean value indicating whether the receiver is done loading content.
- [func stopLoading()](uiwebview/stoploading.md)
  Stops the loading of any web content managed by the receiver.
- [func reload()](uiwebview/reload.md)
  Reloads the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/loadrequest(_:))*