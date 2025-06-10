# isLoading

**Framework**: WebKit  
**Kind**: property

Indicates whether the webpage is currently loading content.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final var isLoading: Bool { get }
```

#### Return Value

`true` if the receiver is still loading content, otherwise, `false`.

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
- [var estimatedProgress: Double](webpage/estimatedprogress.md)
  An estimate of completion percentage of the current navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/isloading)*