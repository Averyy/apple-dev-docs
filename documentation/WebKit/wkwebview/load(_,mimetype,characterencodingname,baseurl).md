# load(_:mimeType:characterEncodingName:baseURL:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Loads the content of the specified data object and navigates to it.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func load(_ data: Data, mimeType MIMEType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?
```

```objc
- (WKNavigation *) loadData:(NSData *) data MIMEType:(NSString *) MIMEType characterEncodingName:(NSString *) characterEncodingName baseURL:(NSURL *) baseURL;
```

## Return Value

A new navigation object for tracking the request.

## Discussion

Use this method to navigate to a webpage that you loaded yourself and saved in a data object. For example, if you previously wrote HTML content to a data object, use this method to navigate to that content.

## Parameters

- `data`: The data to use as the contents of the webpage.
- `MIMEType`: The MIME type of the information in the `data` parameter. This parameter must not contain an empty string.
- `characterEncodingName`: The data’s character encoding name.
- `baseURL`: A URL that you use to resolve relative URLs within the document.

## See Also

### Loading web content
- [func load(URLRequest) -> WKNavigation?](./load%28_%29-5siv6.md)
- [func load(URL) -> WKNavigation?](./load%28_%29-4xx8m.md)
- [func loadHTMLString(String, baseURL: URL?) -> WKNavigation?](./loadhtmlstring%28_,baseurl%29.md)
  Loads the contents of the specified HTML string and navigates to it.
- [func loadFileRequest(URLRequest, allowingReadAccessTo: URL) -> WKNavigation](./loadfilerequest%28_,allowingreadaccessto%29.md)
  Loads the web content from the file the URL request object specifies and navigates to that content.
- [func loadFileURL(URL, allowingReadAccessTo: URL) -> WKNavigation?](./loadfileurl%28_,allowingreadaccessto%29.md)
  Loads the web content from the specified file and navigates to it.
- [func loadSimulatedRequest(URLRequest, response: URLResponse, responseData: Data) -> WKNavigation](./loadsimulatedrequest%28_,response,responsedata%29.md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [func loadSimulatedRequest(URLRequest, responseHTML: String) -> WKNavigation](./loadsimulatedrequest%28_,responsehtml%29.md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the view is currently loading content.
- [var estimatedProgress: Double](./estimatedprogress.md)
  An estimate of what fraction of the current navigation has been loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/load(_:mimetype:characterencodingname:baseurl:))*