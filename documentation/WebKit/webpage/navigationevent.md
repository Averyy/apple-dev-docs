# WebPage.NavigationEvent

**Framework**: WebKit  
**Kind**: struct

A particular state that occurs during the progression of a navigation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct NavigationEvent
```

## Topics

### Instance Properties
- [let kind: WebPage.NavigationEvent.Kind](webpage/navigationevent/kind-swift.property.md)
  The type of this navigation event.
- [let navigationID: WebPage.NavigationID](webpage/navigationevent/navigationid.md)
  The ID of the navigation that triggered this event.
### Enumerations
- [WebPage.NavigationEvent.Kind](webpage/navigationevent/kind-swift.enum.md)
  A set of values representing the possible types a NavigationEvent can represent.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.BackForwardList](webpage/backforwardlist-swift.struct.md)
  An observable representation of a webpage’s navigations.
- [WebPage.NavigationID](webpage/navigationid.md)
  An opaque identifier which can be used to uniquely identify a load request for a web page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationevent)*