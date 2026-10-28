# loadFileURL(_:allowingReadAccessTo:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Loads the web content from the specified file and navigates to it.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func loadFileURL(_ URL: URL, allowingReadAccessTo readAccessURL: URL) -> WKNavigation?
```

```objc
- (WKNavigation *) loadFileURL:(NSURL *) URL allowingReadAccessToURL:(NSURL *) readAccessURL;
```

## Return Value

A new navigation object you use to track the loading progress of the request.

## Discussion

This method sets the source of this load request for app activity data to [`NSURLRequest.Attribution.developer`](../../Foundation/nsurlrequest/attribution-swift.enum/developer.md). To specify the source of this load, use [`loadFileRequest(_:allowingReadAccessTo:)`](./loadfilerequest%28_,allowingreadaccessto%29.md) instead.

## Parameters

- `URL`: The URL of a file that contains web content. This URL must be a file-based URL.
- `readAccessURL`: The URL of a file or directory containing web content that you grant the system permission to read. This URL must be a file-based URL and must not be empty. To prevent WebKit from reading any other content, specify the same value as the URL parameter. To read additional files related to the content file, specify a directory.

## See Also

### Loading web content
- [func load(Data, mimeType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?](./load%28_,mimetype,characterencodingname,baseurl%29.md)
  Loads the content of the specified data object and navigates to it.
- [func load(URLRequest) -> WKNavigation?](./load%28_%29-5siv6.md)
- [func load(URL) -> WKNavigation?](./load%28_%29-4xx8m.md)
- [func loadHTMLString(String, baseURL: URL?) -> WKNavigation?](./loadhtmlstring%28_,baseurl%29.md)
  Loads the contents of the specified HTML string and navigates to it.
- [func loadFileRequest(URLRequest, allowingReadAccessTo: URL) -> WKNavigation](./loadfilerequest%28_,allowingreadaccessto%29.md)
  Loads the web content from the file the URL request object specifies and navigates to that content.
- [func loadSimulatedRequest(URLRequest, response: URLResponse, responseData: Data) -> WKNavigation](./loadsimulatedrequest%28_,response,responsedata%29.md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [func loadSimulatedRequest(URLRequest, responseHTML: String) -> WKNavigation](./loadsimulatedrequest%28_,responsehtml%29.md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the view is currently loading content.
- [var estimatedProgress: Double](./estimatedprogress.md)
  An estimate of what fraction of the current navigation has been loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/loadfileurl(_:allowingreadaccessto:))*