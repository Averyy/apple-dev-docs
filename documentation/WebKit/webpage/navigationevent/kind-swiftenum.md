# WebPage.NavigationEvent.Kind

**Framework**: WebKit  
**Kind**: enum

A set of values representing the possible types a NavigationEvent can represent.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
enum Kind
```

## Topics

### Enumeration Cases
- [WebPage.NavigationEvent.Kind.committed](webpage/navigationevent/kind-swift.enum/committed.md)
  This event occurs when the web page has started to receive content for the main frame. This happens immediately before the web page starts to update the main frame.
- [WebPage.NavigationEvent.Kind.failed(underlyingError:)](webpage/navigationevent/kind-swift.enum/failed(underlyingerror:).md)
  This event indicates an error occurred during navigation.
- [WebPage.NavigationEvent.Kind.failedProvisionalNavigation(underlyingError:)](webpage/navigationevent/kind-swift.enum/failedprovisionalnavigation(underlyingerror:).md)
  This event indicates an error occurs during the early navigation process.
- [WebPage.NavigationEvent.Kind.finished](webpage/navigationevent/kind-swift.enum/finished.md)
  This event occurs once the navigation is complete.
- [WebPage.NavigationEvent.Kind.receivedServerRedirect](webpage/navigationevent/kind-swift.enum/receivedserverredirect.md)
  This event occurs when the web page received a server redirect for a request.
- [WebPage.NavigationEvent.Kind.startedProvisionalNavigation](webpage/navigationevent/kind-swift.enum/startedprovisionalnavigation.md)
  This event occurs when the web page receives provisional approval to process a navigation request, but before it receives a response to that request.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationevent/kind-swift.enum)*