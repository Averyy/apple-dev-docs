# isLoading

**Framework**: Webkit  
**Kind**: property

A Boolean value that indicates whether the view is currently loading content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isLoading: Bool { get }
```

#### Discussion

Set to `true` if the receiver is still loading content; otherwise, `false.` The [`WKWebView`](wkwebview.md) class is key-value observing (KVO) compliant for this property.

## See Also

- [func load(URLRequest) -> WKNavigation?](wkwebview/load(_:).md)
  Loads the web content that the specified URL request object references and navigates to that content.
- [func load(Data, mimeType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?](wkwebview/load(_:mimetype:characterencodingname:baseurl:).md)
  Loads the content of the specified data object and navigates to it.
- [func loadHTMLString(String, baseURL: URL?) -> WKNavigation?](wkwebview/loadhtmlstring(_:baseurl:).md)
  Loads the contents of the specified HTML string and navigates to it.
- [func loadFileRequest(URLRequest, allowingReadAccessTo: URL) -> WKNavigation](wkwebview/loadfilerequest(_:allowingreadaccessto:).md)
  Loads the web content from the file the URL request object specifies and navigates to that content.
- [func loadFileURL(URL, allowingReadAccessTo: URL) -> WKNavigation?](wkwebview/loadfileurl(_:allowingreadaccessto:).md)
  Loads the web content from the specified file and navigates to it.
- [func loadSimulatedRequest(URLRequest, response: URLResponse, responseData: Data) -> WKNavigation](wkwebview/loadsimulatedrequest(_:response:responsedata:).md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [func loadSimulatedRequest(URLRequest, responseHTML: String) -> WKNavigation](wkwebview/loadsimulatedrequest(_:responsehtml:).md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [var estimatedProgress: Double](wkwebview/estimatedprogress.md)
  An estimate of what fraction of the current navigation has been loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/isloading)*