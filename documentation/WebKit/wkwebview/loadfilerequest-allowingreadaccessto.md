# loadFileRequest(_:allowingReadAccessTo:)

**Framework**: WebKit  
**Kind**: method

Loads the web content from the file the URL request object specifies and navigates to that content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func loadFileRequest(_ request: URLRequest, allowingReadAccessTo readAccessURL: URL) -> WKNavigation
```

#### Return Value

A new navigation object you use to track the loading progress of the request.

#### Discussion

Provide the source of this load request for app activity data by setting the [`attribution`](https://developer.apple.com/documentation/Foundation/URLRequest/attribution-swift.property) parameter on your request.

## Parameters

- `request`: A URL request that specifies the file to display. The URL in this request must be a file-based URL.
- `readAccessURL`: The URL of a file or directory containing web content that you grant the system permission to read. This URL must be a file-based URL and must not be empty. To prevent WebKit from reading any other content, specify the same value as the URL parameter. To read additional files related to the content file, specify a directory.

## See Also

- [func load(URLRequest) -> WKNavigation?](wkwebview/load(_:).md)
  Loads the web content that the specified URL request object references and navigates to that content.
- [func load(Data, mimeType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?](wkwebview/load(_:mimetype:characterencodingname:baseurl:).md)
  Loads the content of the specified data object and navigates to it.
- [func loadHTMLString(String, baseURL: URL?) -> WKNavigation?](wkwebview/loadhtmlstring(_:baseurl:).md)
  Loads the contents of the specified HTML string and navigates to it.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/loadfilerequest(_:allowingreadaccessto:))*