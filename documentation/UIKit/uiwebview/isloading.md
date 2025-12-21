# isLoading

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the receiver is done loading content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
var isLoading: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the receiver is still loading content; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func load(Data, mimeType: String, textEncodingName: String, baseURL: URL)](uiwebview/load(_:mimetype:textencodingname:baseurl:).md)
  Sets the main page contents, MIME type, content encoding, and base URL.
- [func loadHTMLString(String, baseURL: URL?)](uiwebview/loadhtmlstring(_:baseurl:).md)
  Sets the main page content and base URL.
- [func loadRequest(URLRequest)](uiwebview/loadrequest(_:).md)
  Connects to a given URL by initiating an asynchronous client request.
- [var request: URLRequest?](uiwebview/request.md)
  The URL request identifying the location of the content to load.
- [func stopLoading()](uiwebview/stoploading.md)
  Stops the loading of any web content managed by the receiver.
- [func reload()](uiwebview/reload.md)
  Reloads the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebview/isloading)*