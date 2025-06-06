# WebDataSource

**Framework**: Webkit  
**Kind**: class

`WebDataSource` encapsulates the web content to be displayed in a web frame view. A `WebDataSource` object has a representation object, conforming to the `WebDocumentRepresentation` protocol, that holds the data in an appropriate format depending on the MIME type. You can extend WebKit to support new MIME types by implementing your own view and representation classes, and specifying the mapping between them using the  [`registerClass(_:representationClass:forMIMEType:)`](webview/registerclass(_:representationclass:formimetype:).md) `WebView` class method.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class WebDataSource
```

#### Overview

`WebDataSource` objects have an associated initial request, possibly a modified request, and a response object. Since the data source may be in the process of being loaded, you should check the state of a data source using [`isLoading`](webdatasource/isloading.md) before accessing its data. Use [`data`](webdatasource/data.md) to get the raw data. Use the [`representation`](webdatasource/representation.md) method to get the actual representation object and query it for more details.

## Topics

### Initializing an instance
- [init!(request: URLRequest!)](webdatasource/init(request:).md)
  initializes a data source with a URL request.
### Querying page data and state
- [var data: Data!](webdatasource/data.md)
  The raw data that represents the data source’s content.
- [var isLoading: Bool](webdatasource/isloading.md)
  A Boolean that indicates whether the data source is loading its content.
- [var pageTitle: String!](webdatasource/pagetitle.md)
  The title of the data source’s page.
- [var representation: (any WebDocumentRepresentation)!](webdatasource/representation.md)
  The data source’s representation depending on its MIME type.
- [var textEncodingName: String!](webdatasource/textencodingname.md)
  The text encoding for the data source’s web view, if set, or the text encoding of the response.
### Getting the request and response
- [var initialRequest: URLRequest!](webdatasource/initialrequest.md)
  A reference to the original request that was used to load the web content.
- [var request: NSMutableURLRequest!](webdatasource/request.md)
  The request that was used to create the data source.
- [var response: URLResponse!](webdatasource/response.md)
  The response for this data source.
### Getting the web frame
- [var webFrame: WebFrame!](webdatasource/webframe.md)
  The web frame that represents this data source.
### Getting an unreachable URL
- [var unreachableURL: URL!](webdatasource/unreachableurl.md)
  The data source’s unreachable URL.
### Getting a web archive
- [var webArchive: WebArchive!](webdatasource/webarchive.md)
  A web archive representing the data source, its subresources, and subframes.
### Accessing subresources
- [var mainResource: WebResource!](webdatasource/mainresource.md)
  A`WebResource` object representing the data source.
- [func addSubresource(WebResource!)](webdatasource/addsubresource(_:).md)
  Adds a resource to the data source’s list of subresources.
- [func subresource(for: URL!) -> WebResource!](webdatasource/subresource(for:).md)
  Returns a subresource for the given URL.
- [var subresources: [Any]!](webdatasource/subresources.md)
  The data source’s subresources that have finished downloading.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WebFrame](webframe.md)
  A `WebFrame` object encapsulates the data displayed in a `WebFrameView` object. There is one `WebFrame` object per frame displayed in a `WebView`. An entire webpage is represented by a hierarchy of `WebFrame` objects in which the root object is called the .
- [class WebFrameView](webframeview.md)
  `WebFrameView` objects and their subviews display the web content contained in a frame. You never create instances of `WebFrameView` directly—`WebView` objects create and manage a hierarchy of `WebFrameView` objects, one for each frame. `WebFrameView` objects use a scroll view whose document view conforms to the [`WebDocumentView`](webdocumentview.md) protocol.
- [protocol WebFrameLoadDelegate](webframeloaddelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource)*