# WebPage.NavigationError

**Framework**: WebKit  
**Kind**: enum

A specific error that caused a navigation to fail.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum NavigationError
```

## Topics

### Enumeration Cases
- [WebPage.NavigationError.failedProvisionalNavigation(_:)](webpage/navigationerror/failedprovisionalnavigation(_:).md)
  An error occurred during the early navigation process.
- [WebPage.NavigationError.invalidURL](webpage/navigationerror/invalidurl.md)
  The URL to navigate to is invalid.
- [WebPage.NavigationError.pageClosed](webpage/navigationerror/pageclosed.md)
  The navigation could not begin because the page has been closed.
- [WebPage.NavigationError.webContentProcessTerminated](webpage/navigationerror/webcontentprocessterminated.md)
  The process for the web content of this page was terminated for any reason.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.BackForwardList](webpage/backforwardlist-swift.struct.md)
  An observable representation of a webpage’s previously loaded resources.
- [WebPage.NavigationEvent](webpage/navigationevent.md)
  A particular state that occurs during the progression of a navigation.
- [var navigations: some AsyncSequence<WebPage.NavigationEvent, any Error>](webpage/navigations.md)
  A sequence of all the navigation events that occur throughout the webpage, including both user navigation and programmatic navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationerror)*