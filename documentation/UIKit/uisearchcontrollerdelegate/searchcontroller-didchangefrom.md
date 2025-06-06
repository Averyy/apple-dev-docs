# searchController(_:didChangeFrom:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate after the search bar placement changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func searchController(_ searchController: UISearchController, didChangeFrom previousPlacement: UINavigationItem.SearchBarPlacement)
```

#### Discussion

The system calls this method after a search bar placement change occurs. Implement this method if you need to make any custom changes to your search suggestions UI according to the previous search bar placement.

The system calls this method after [`searchController(_:willChangeTo:)`](uisearchcontrollerdelegate/searchcontroller(_:willchangeto:).md).

## Parameters

- `searchController`: The search controller associated with the search bar.
- `previousPlacement`: The previous search bar placement.

## See Also

- [func searchController(UISearchController, willChangeTo: UINavigationItem.SearchBarPlacement)](uisearchcontrollerdelegate/searchcontroller(_:willchangeto:).md)
  Notifies the delegate before the search bar placement changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/searchcontroller(_:didchangefrom:))*