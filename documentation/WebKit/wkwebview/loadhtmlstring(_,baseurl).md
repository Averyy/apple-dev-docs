# loadHTMLString(_:baseURL:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Loads the contents of the specified HTML string and navigates to it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func loadHTMLString(_ string: String, baseURL: URL?) -> WKNavigation?
```

```objc
- (WKNavigation *) loadHTMLString:(NSString *) string baseURL:(NSURL *) baseURL;
```

## Return Value

A new navigation object you use to track the loading progress of the request.

## Discussion

Use this method to navigate to a webpage that you loaded or created yourself. For example, you might use this method to load HTML content that your app generates programmatically.

This method sets the source of this load request for app activity data to [`NSURLRequest.Attribution.developer`](../../Foundation/nsurlrequest/attribution-swift.enum/developer.md).

## Parameters

- `string`: The string to use as the contents of the webpage.
- `baseURL`: The base URL to use when the system resolves relative URLs within the HTML string.

## See Also

### Loading web content
- [func load(Data, mimeType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?](./load%28_,mimetype,characterencodingname,baseurl%29.md)
  Loads the content of the specified data object and navigates to it.
- [func load(URLRequest) -> WKNavigation?](./load%28_%29-5siv6.md)
- [func load(URL) -> WKNavigation?](./load%28_%29-4xx8m.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/loadhtmlstring(_:baseurl:))*