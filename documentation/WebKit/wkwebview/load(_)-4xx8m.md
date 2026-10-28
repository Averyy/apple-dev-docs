# load(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func load(_ url: URL) -> WKNavigation?
```

```objc
- (WKNavigation *) loadURL:(NSURL *) url;
```

## Return Value

A new navigation for the given request.

## Discussion

Navigates to a requested URL.

## Parameters

- `url`: The URL to which to navigate.

## See Also

### Loading web content
- [func load(Data, mimeType: String, characterEncodingName: String, baseURL: URL) -> WKNavigation?](./load%28_,mimetype,characterencodingname,baseurl%29.md)
  Loads the content of the specified data object and navigates to it.
- [func load(URLRequest) -> WKNavigation?](./load%28_%29-5siv6.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/load(_:)-4xx8m)*