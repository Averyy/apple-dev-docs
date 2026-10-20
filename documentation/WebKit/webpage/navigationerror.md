# WebPage.NavigationError

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

A specific error that caused a navigation to fail.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum NavigationError
```

## Topics

### Enumeration Cases
- [WebPage.NavigationError.failedProvisionalNavigation(_:)](./navigationerror/failedprovisionalnavigation%28_%29.md)
  An error occurred during the early navigation process.
- [WebPage.NavigationError.invalidURL](./navigationerror/invalidurl.md)
  The URL to navigate to is invalid.
- [WebPage.NavigationError.pageClosed](./navigationerror/pageclosed.md)
  The navigation could not begin because the page has been closed.
- [WebPage.NavigationError.webContentProcessTerminated](./navigationerror/webcontentprocessterminated.md)
  The process for the web content of this page was terminated for any reason.

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing navigation between webpages
- [WebPage.BackForwardList](./backforwardlist-swift.struct.md)
  An observable representation of a webpage’s previously loaded resources.
- [WebPage.NavigationEvent](./navigationevent.md)
  A particular state that occurs during the progression of a navigation.
- [var navigations: some AsyncSequence<WebPage.NavigationEvent, any Error>](./navigations.md)
  A sequence of all the navigation events that occur throughout the webpage, including both user navigation and programmatic navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationerror)*