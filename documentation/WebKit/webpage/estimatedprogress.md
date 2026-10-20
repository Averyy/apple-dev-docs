# estimatedProgress

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An estimate of completion percentage of the current navigation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var estimatedProgress: Double { get }
```

#### Discussion

The value ranges from `0.0` to `1.0` based on the total number of bytes received, including the main document and all of its potential subresources. After navigation loading completes, the `estimatedProgress` value remains at `1.0` until a new navigation starts, at which point the `estimatedProgress` value resets to `0.0`.

## See Also

### Loading web content
- [func load(WebPage.BackForwardList.Item) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](./load%28_%29-32ngj.md)
  Navigates to an item from the back-forward list and sets it as the current item.
- [func load(URLRequest) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](./load%28_%29-7kw3h.md)
  Loads the web content that the specified URL request object references and navigates to that content.
- [func load(URL?) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](./load%28_%29-8wfiq.md)
  Loads the web content that the specified URL references and navigates to that content.
- [func load(Data, mimeType: String, characterEncoding: String.Encoding, baseURL: URL) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](./load%28_,mimetype,characterencoding,baseurl%29.md)
  Loads the content of the specified data object and navigates to it.
- [func load(html: String, baseURL: URL) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](./load%28html,baseurl%29.md)
  Loads the contents of the specified HTML string and navigates to it.
- [func load(simulatedRequest: URLRequest, responseHTML: String) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](./load%28simulatedrequest,responsehtml%29.md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [func load(simulatedRequest: URLRequest, response: URLResponse, responseData: Data) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](./load%28simulatedrequest,response,responsedata%29.md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [var isLoading: Bool](./isloading.md)
  Indicates whether the webpage is currently loading content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/estimatedprogress)*