# UISearchControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of delegate methods for search controller objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UISearchControllerDelegate : NSObjectProtocol
```

## Topics

### Presenting and dismissing the search controller
- [func didDismissSearchController(UISearchController)](uisearchcontrollerdelegate/diddismisssearchcontroller(_:).md)
  Notifies the delegate when the system completes automatic dismissal of the search controller.
- [func didPresentSearchController(UISearchController)](uisearchcontrollerdelegate/didpresentsearchcontroller(_:).md)
  Notifies the delegate when the system completes automatic presentation of the search controller.
- [func presentSearchController(UISearchController)](uisearchcontrollerdelegate/presentsearchcontroller(_:).md)
  Presents the designated search controller.
- [func willDismissSearchController(UISearchController)](uisearchcontrollerdelegate/willdismisssearchcontroller(_:).md)
  Notifies the delegate that the system is about to automatically dismiss the search controller.
- [func willPresentSearchController(UISearchController)](uisearchcontrollerdelegate/willpresentsearchcontroller(_:).md)
  Notifies the delegate that the system is about to automatically display the search controller.
### Responding to search bar placement updates
- [func searchController(UISearchController, didChangeFrom: UINavigationItem.SearchBarPlacement)](uisearchcontrollerdelegate/searchcontroller(_:didchangefrom:).md)
  Notifies the delegate after the search bar placement changes.
- [func searchController(UISearchController, willChangeTo: UINavigationItem.SearchBarPlacement)](uisearchcontrollerdelegate/searchcontroller(_:willchangeto:).md)
  Notifies the delegate before the search bar placement changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UISearchControllerDelegate)?](uisearchcontroller/delegate.md)
  The search controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate)*