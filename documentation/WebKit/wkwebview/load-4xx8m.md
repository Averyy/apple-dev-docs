# load(_:)

**Framework**: WebKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func load(_ url: URL) -> WKNavigation?
```

#### Return Value

A new navigation for the given request.

#### Discussion

Navigates to a requested URL.

## Parameters

- `url`: The URL to which to navigate.

## See Also

- [func load(Data, mimeType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?](wkwebview/load(_:mimetype:characterencodingname:baseurl:).md)
  Loads the content of the specified data object and navigates to it.
- [func load(URLRequest) -> WKNavigation?](wkwebview/load(_:)-5siv6.md)
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
- [var isLoading: Bool](wkwebview/isloading.md)
  A Boolean value that indicates whether the view is currently loading content.
- [var estimatedProgress: Double](wkwebview/estimatedprogress.md)
  An estimate of what fraction of the current navigation has been loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/load(_:)-4xx8m)*