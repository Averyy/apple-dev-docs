# presentSearchController(_:)

**Framework**: UIKit  
**Kind**: method

Presents the designated search controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func presentSearchController(_ searchController: UISearchController)
```

#### Discussion

The system calls this method when the user begins editing in the search controller, or you set the [`isActive`](uisearchcontroller/isactive.md) property to [`true`](https://developer.apple.com/documentation/Swift/true). The system performs a default presentation if you don’t implement this method or you present the controller yourself.

## Parameters

- `searchController`: The   object to present.

## See Also

- [func didDismissSearchController(UISearchController)](uisearchcontrollerdelegate/diddismisssearchcontroller(_:).md)
  Notifies the delegate when the system completes automatic dismissal of the search controller.
- [func didPresentSearchController(UISearchController)](uisearchcontrollerdelegate/didpresentsearchcontroller(_:).md)
  Notifies the delegate when the system completes automatic presentation of the search controller.
- [func willDismissSearchController(UISearchController)](uisearchcontrollerdelegate/willdismisssearchcontroller(_:).md)
  Notifies the delegate that the system is about to automatically dismiss the search controller.
- [func willPresentSearchController(UISearchController)](uisearchcontrollerdelegate/willpresentsearchcontroller(_:).md)
  Notifies the delegate that the system is about to automatically display the search controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/presentsearchcontroller(_:))*