# presentSearchController(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents the designated search controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func presentSearchController(_ searchController: UISearchController)
```

```objc
- (void) presentSearchController:(UISearchController *) searchController;
```

## Discussion

The system calls this method when the user begins editing in the search controller, or you set the [`isActive`](../uisearchcontroller/isactive.md) property to [`true`](../../Swift/true.md). The system performs a default presentation if you don’t implement this method or you present the controller yourself.

## Parameters

- `searchController`: The [`UISearchController`](../uisearchcontroller.md) object to present.

## See Also

### Presenting and dismissing the search controller
- [func didDismissSearchController(UISearchController)](./diddismisssearchcontroller%28_%29.md)
  Notifies the delegate when the system completes automatic dismissal of the search controller.
- [func didPresentSearchController(UISearchController)](./didpresentsearchcontroller%28_%29.md)
  Notifies the delegate when the system completes automatic presentation of the search controller.
- [func willDismissSearchController(UISearchController)](./willdismisssearchcontroller%28_%29.md)
  Notifies the delegate that the system is about to automatically dismiss the search controller.
- [func willPresentSearchController(UISearchController)](./willpresentsearchcontroller%28_%29.md)
  Notifies the delegate that the system is about to automatically display the search controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/presentsearchcontroller(_:))*