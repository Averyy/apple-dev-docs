# load(html:baseURL:)

**Framework**: WebKit  
**Kind**: method

Loads the contents of the specified HTML string and navigates to it.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@discardableResult
@MainActor final func load(html: String, baseURL: URL = Foundation.URL(string: "about:blank")!) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
```

#### Return Value

An async sequence you use to track the loading progress of the navigation. If the `Task` enclosing the sequence is cancelled, the page will stop loading all resources.

#### Discussion

Use this method to navigate to a webpage that you loaded or created yourself. For example, you might use this method to load HTML content that your app generates programmatically.

This method sets the source of this load request for app activity data to NSURLRequest.Attribution.developer.

## Parameters

- `html`: The string to use as the contents of the webpage.
- `baseURL`: The base URL to use when the system resolves relative URLs within the HTML string. By default, this is  .

## See Also

- [func load(WebPage.BackForwardList.Item) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](webpage/load(_:)-32ngj.md)
  Navigates to an item from the back-forward list and sets it as the current item.
- [func load(URLRequest) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](webpage/load(_:)-7kw3h.md)
  Loads the web content that the specified URL request object references and navigates to that content.
- [func load(URL?) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](webpage/load(_:)-8wfiq.md)
  Loads the web content that the specified URL references and navigates to that content.
- [func load(Data, mimeType: String, characterEncoding: String.Encoding, baseURL: URL) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](webpage/load(_:mimetype:characterencoding:baseurl:).md)
  Loads the content of the specified data object and navigates to it.
- [func load(simulatedRequest: URLRequest, responseHTML: String) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](webpage/load(simulatedrequest:responsehtml:).md)
  Loads the web content from the HTML you provide as if the HTML were the response to the request.
- [func load(simulatedRequest: URLRequest, response: URLResponse, responseData: Data) -> some AsyncSequence<WebPage.NavigationEvent, any Error>
](webpage/load(simulatedrequest:response:responsedata:).md)
  Loads the web content from the data you provide as if the data were the response to the request.
- [var isLoading: Bool](webpage/isloading.md)
  Indicates whether the webpage is currently loading content.
- [var estimatedProgress: Double](webpage/estimatedprogress.md)
  An estimate of completion percentage of the current navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/load(html:baseurl:))*