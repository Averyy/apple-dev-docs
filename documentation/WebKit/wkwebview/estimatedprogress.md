# estimatedProgress

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An estimate of what fraction of the current navigation has been loaded.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var estimatedProgress: Double { get }
```

```objc
@property (nonatomic, readonly) double estimatedProgress;
```

#### Discussion

This value ranges from `0.0` to `1.0` based on the total number of bytes received, including the main document and all of its potential subresources. After navigation loading completes, the `estimatedProgress` value remains at `1.0` until a new navigation starts, at which point the `estimatedProgress` value resets to `0.0`. The [`WKWebView`](../wkwebview.md) class is key-value observing (KVO) compliant for this property.

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
- [func loadFileURL(URL, allowingReadAccessTo: URL) -> WKNavigation?](./loadfileurl%28_,allowingreadaccessto%29.md)
  Loads the web content from the specified file and navigates to it.
- [func loadSimulatedRequest(URLRequest, response: URLResponse, responseData: Data) -> WKNavigation](./loadsimulatedrequest%28_,response,responsedata%29.md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [func loadSimulatedRequest(URLRequest, responseHTML: String) -> WKNavigation](./loadsimulatedrequest%28_,responsehtml%29.md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the view is currently loading content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/estimatedprogress)*