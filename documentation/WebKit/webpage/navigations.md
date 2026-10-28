# navigations

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A sequence of all the navigation events that occur throughout the webpage, including both user navigation and programmatic navigation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var navigations: some AsyncSequence<WebPage.NavigationEvent, any Error> { get }
```

## Discussion

A specific navigation is comprised of a sequential set of [`WebPage.NavigationEvent`](./navigationevent.md)s; a new navigation begins when an event is [`WebPage.NavigationEvent.startedProvisionalNavigation`](./navigationevent/startedprovisionalnavigation.md).

This property produces a new sequence each time it is called, and starts tracking events as soon as it is created. The sequence is indefinite, but may be terminated under several circumstances:

- The owning [`WebPage`](../webpage.md)’s lifetime ends.
- An error occurs during navigation, at which point the sequence will throw the error and terminate.
- The `Task` enclosing iteration of the sequence is cancelled.

To track a specific programmatic navigation, use the return value of one of the loading APIs.

## See Also

### Observing navigation between webpages
- [WebPage.BackForwardList](./backforwardlist-swift.struct.md)
  An observable representation of a webpage’s previously loaded resources.
- [WebPage.NavigationEvent](./navigationevent.md)
  A particular state that occurs during the progression of a navigation.
- [WebPage.NavigationError](./navigationerror.md)
  A specific error that caused a navigation to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigations)*