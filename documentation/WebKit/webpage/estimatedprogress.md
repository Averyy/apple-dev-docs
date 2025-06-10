# estimatedProgress

**Framework**: WebKit  
**Kind**: property

An estimate of completion percentage of the current navigation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final var estimatedProgress: Double { get }
```

#### Discussion

The value ranges from `0.0` to `1.0` based on the total number of bytes received, including the main document and all of its potential subresources. After navigation loading completes, the `estimatedProgress` value remains at `1.0` until a new navigation starts, at which point the `estimatedProgress` value resets to `0.0`.

## See Also

- [func load(WebPage.BackForwardList.Item) -> WebPage.NavigationID?](webpage/load(_:)-78prx.md)
  Navigates to an item from the back-forward list and sets it as the current item.
- [func load(URLRequest) -> WebPage.NavigationID?](webpage/load(_:)-75gd5.md)
  Loads the web content that the specified URL request object references and navigates to that content.
- [func load(Data, mimeType: String, characterEncoding: String.Encoding, baseURL: URL) -> WebPage.NavigationID?](webpage/load(_:mimetype:characterencoding:baseurl:).md)
  Loads the content of the specified data object and navigates to it.
- [func load(html: String, baseURL: URL) -> WebPage.NavigationID?](webpage/load(html:baseurl:).md)
  Loads the contents of the specified HTML string and navigates to it.
- [func load(simulatedRequest: URLRequest, responseHTML: String) -> WebPage.NavigationID?](webpage/load(simulatedrequest:responsehtml:).md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [func load(simulatedRequest: URLRequest, response: URLResponse, responseData: Data) -> WebPage.NavigationID?](webpage/load(simulatedrequest:response:responsedata:).md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [var isLoading: Bool](webpage/isloading.md)
  Indicates whether the webpage is currently loading content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/estimatedprogress)*