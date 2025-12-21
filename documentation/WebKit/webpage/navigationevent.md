# WebPage.NavigationEvent

**Framework**: WebKit  
**Kind**: enum

A particular state that occurs during the progression of a navigation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum NavigationEvent
```

## Topics

### Enumeration Cases
- [WebPage.NavigationEvent.committed](webpage/navigationevent/committed.md)
  This event occurs when the page has started to receive content for the main frame.
- [WebPage.NavigationEvent.finished](webpage/navigationevent/finished.md)
  This event occurs once the navigation is complete.
- [WebPage.NavigationEvent.receivedServerRedirect](webpage/navigationevent/receivedserverredirect.md)
  This event occurs when the page received a server redirect for a request.
- [WebPage.NavigationEvent.startedProvisionalNavigation](webpage/navigationevent/startedprovisionalnavigation.md)
  This event occurs when the page receives provisional approval to process a navigation request, but before it receives a response to that request.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.BackForwardList](webpage/backforwardlist-swift.struct.md)
  An observable representation of a webpage’s previously loaded resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationevent)*