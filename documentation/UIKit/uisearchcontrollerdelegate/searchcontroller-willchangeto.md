# searchController(_:willChangeTo:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate before the search bar placement changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func searchController(_ searchController: UISearchController, willChangeTo newPlacement: UINavigationItem.SearchBarPlacement)
```

#### Discussion

The system calls this method before a search bar placement change occurs, such as in response to a layout change that alters the amount of available space in the navigation bar. Implement this method if you need to make any custom changes to your search suggestions UI according to the new search bar placement.

The system calls this method before [`searchController(_:didChangeFrom:)`](uisearchcontrollerdelegate/searchcontroller(_:didchangefrom:).md).

## Parameters

- `searchController`: The search controller associated with the search bar.
- `newPlacement`: The new search bar placement.

## See Also

- [func searchController(UISearchController, didChangeFrom: UINavigationItem.SearchBarPlacement)](uisearchcontrollerdelegate/searchcontroller(_:didchangefrom:).md)
  Notifies the delegate after the search bar placement changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/searchcontroller(_:willchangeto:))*