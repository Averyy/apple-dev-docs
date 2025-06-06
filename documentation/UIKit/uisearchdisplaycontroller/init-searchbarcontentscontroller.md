# init(searchBar:contentsController:)

**Framework**: UIKit  
**Kind**: init

Returns a display controller initialized with the given search bar and contents controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init(searchBar: UISearchBar, contentsController viewController: UIViewController)
```

#### Return Value

A search display controller initialized with the given search bar and contents controller.

## Parameters

- `searchBar`: The search bar must not currently be associated with another search display controller.
- `viewController`: The view controller must not currently be associated with another search display controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/init(searchbar:contentscontroller:))*