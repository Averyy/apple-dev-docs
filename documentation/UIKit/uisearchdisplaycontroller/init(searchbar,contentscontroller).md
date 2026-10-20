# init(searchBar:contentsController:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns a display controller initialized with the given search bar and contents controller.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UISearchDisplayController`](../uisearchdisplaycontroller.md).

## Declaration

```swift
init(searchBar: UISearchBar, contentsController viewController: UIViewController)
```

```objc
- (instancetype) initWithSearchBar:(UISearchBar *) searchBar contentsController:(UIViewController *) viewController;
```

#### Return Value

A search display controller initialized with the given search bar and contents controller.

## Parameters

- `searchBar`: A search bar.

  The search bar must not currently be associated with another search display controller.
- `viewController`: The view controller that manages display of the original contents that are to be searched.

  The view controller must not currently be associated with another search display controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/init(searchbar:contentscontroller:))*