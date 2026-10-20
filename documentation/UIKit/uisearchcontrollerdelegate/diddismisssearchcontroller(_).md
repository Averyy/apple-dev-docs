# didDismissSearchController(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when the system completes automatic dismissal of the search controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func didDismissSearchController(_ searchController: UISearchController)
```

```objc
- (void) didDismissSearchController:(UISearchController *) searchController;
```

#### Discussion

The system only calls this method when it automatically dismisses the search controller. The system doesn’t call this method if you explicitly dismiss the search controller.

## Parameters

- `searchController`: The [`UISearchController`](../uisearchcontroller.md) object to dismiss.

## See Also

### Presenting and dismissing the search controller
- [func didPresentSearchController(UISearchController)](./didpresentsearchcontroller%28_%29.md)
  Notifies the delegate when the system completes automatic presentation of the search controller.
- [func presentSearchController(UISearchController)](./presentsearchcontroller%28_%29.md)
  Presents the designated search controller.
- [func willDismissSearchController(UISearchController)](./willdismisssearchcontroller%28_%29.md)
  Notifies the delegate that the system is about to automatically dismiss the search controller.
- [func willPresentSearchController(UISearchController)](./willpresentsearchcontroller%28_%29.md)
  Notifies the delegate that the system is about to automatically display the search controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/diddismisssearchcontroller(_:))*