# load(_:mimeType:characterEncodingName:baseURL:)

**Framework**: Webkit  
**Kind**: method

Loads the content of the specified data object and navigates to it.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func load(_ data: Data, mimeType MIMEType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?
```

#### Return Value

A new navigation object for tracking the request.

#### Discussion

Use this method to navigate to a webpage that you loaded yourself and saved in a data object. For example, if you previously wrote HTML content to a data object, use this method to navigate to that content.

## Parameters

- `data`: The data to use as the contents of the webpage.
- `MIMEType`: The MIME type of the information in the   parameter. This parameter must not contain an empty string.
- `characterEncodingName`: The data’s character encoding name.
- `baseURL`: A URL that you use to resolve relative URLs within the document.

## See Also

- [func load(URLRequest) -> WKNavigation?](wkwebview/load(_:).md)
  Loads the web content that the specified URL request object references and navigates to that content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/load(_:mimetype:characterencodingname:baseurl:))*