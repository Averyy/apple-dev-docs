# searchDisplayControllerDidBeginSearch(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the controller has started searching.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func searchDisplayControllerDidBeginSearch(_ controller: UISearchDisplayController)
```

## Parameters

- `controller`: The search display controller for which the receiver is the delegate.

## See Also

- [func searchDisplayControllerWillBeginSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerwillbeginsearch(_:).md)
  Tells the delegate that the controller is about to begin searching.
- [func searchDisplayControllerWillEndSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerwillendsearch(_:).md)
  Tells the delegate that the controller is about to end searching.
- [func searchDisplayControllerDidEndSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerdidendsearch(_:).md)
  Tells the delegate that the controller has finished searching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontrollerdidbeginsearch(_:))*