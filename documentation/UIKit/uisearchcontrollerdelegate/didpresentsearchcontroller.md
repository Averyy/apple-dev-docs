# didPresentSearchController(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate when the system completes automatic presentation of the search controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func didPresentSearchController(_ searchController: UISearchController)
```

#### Discussion

The system only calls this method when it automatically presents the search controller. The system doesn’t call this method if you explicitly present the search controller.

## Parameters

- `searchController`: The   object to present.

## See Also

- [func didDismissSearchController(UISearchController)](uisearchcontrollerdelegate/diddismisssearchcontroller(_:).md)
  Notifies the delegate when the system completes automatic dismissal of the search controller.
- [func presentSearchController(UISearchController)](uisearchcontrollerdelegate/presentsearchcontroller(_:).md)
  Presents the designated search controller.
- [func willDismissSearchController(UISearchController)](uisearchcontrollerdelegate/willdismisssearchcontroller(_:).md)
  Notifies the delegate that the system is about to automatically dismiss the search controller.
- [func willPresentSearchController(UISearchController)](uisearchcontrollerdelegate/willpresentsearchcontroller(_:).md)
  Notifies the delegate that the system is about to automatically display the search controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/didpresentsearchcontroller(_:))*