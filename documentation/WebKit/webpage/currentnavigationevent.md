# currentNavigationEvent

**Framework**: WebKit  
**Kind**: property

The current navigation event, or `nil` if there have been no navigations so far.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final var currentNavigationEvent: WebPage.NavigationEvent? { get }
```

#### Discussion

This property may be used to observe changes to both an individual navigation, and across navigations.

A new navigation begins when a `NavigationEvent` has a type of `startedProvisionalNavigation`, and is finished once a navigation event with a type of `.finished`, `.failedProvisionalNavigation`, or `.failed`.

## See Also

- [WebPage.BackForwardList](webpage/backforwardlist-swift.struct.md)
  An observable representation of a webpage’s navigations.
- [WebPage.NavigationID](webpage/navigationid.md)
  An opaque identifier which can be used to uniquely identify a load request for a web page.
- [WebPage.NavigationEvent](webpage/navigationevent.md)
  A particular state that occurs during the progression of a navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/currentnavigationevent)*