# UISearchControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of delegate methods for search controller objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UISearchControllerDelegate : NSObjectProtocol
```

```objc
@protocol UISearchControllerDelegate <NSObject>
```

## Topics

### Presenting and dismissing the search controller
- [func didDismissSearchController(UISearchController)](./uisearchcontrollerdelegate/diddismisssearchcontroller%28_%29.md)
  Notifies the delegate when the system completes automatic dismissal of the search controller.
- [func didPresentSearchController(UISearchController)](./uisearchcontrollerdelegate/didpresentsearchcontroller%28_%29.md)
  Notifies the delegate when the system completes automatic presentation of the search controller.
- [func presentSearchController(UISearchController)](./uisearchcontrollerdelegate/presentsearchcontroller%28_%29.md)
  Presents the designated search controller.
- [func willDismissSearchController(UISearchController)](./uisearchcontrollerdelegate/willdismisssearchcontroller%28_%29.md)
  Notifies the delegate that the system is about to automatically dismiss the search controller.
- [func willPresentSearchController(UISearchController)](./uisearchcontrollerdelegate/willpresentsearchcontroller%28_%29.md)
  Notifies the delegate that the system is about to automatically display the search controller.
### Responding to search bar placement updates
- [func searchController(UISearchController, didChangeFrom: UINavigationItem.SearchBarPlacement)](./uisearchcontrollerdelegate/searchcontroller%28_,didchangefrom%29.md)
  Notifies the delegate after the search bar placement changes.
- [func searchController(UISearchController, willChangeTo: UINavigationItem.SearchBarPlacement)](./uisearchcontrollerdelegate/searchcontroller%28_,willchangeto%29.md)
  Notifies the delegate before the search bar placement changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to presentation and dismissal
- [var delegate: (any UISearchControllerDelegate)?](./uisearchcontroller/delegate.md)
  The search controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate)*