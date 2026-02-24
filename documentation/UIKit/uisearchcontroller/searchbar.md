# searchBar

**Framework**: UIKit  
**Kind**: property

The search bar to install in your interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var searchBar: UISearchBar { get }
```

#### Discussion

Before presenting your searchable content, install the search bar somewhere in your view hierarchy. The search bar becomes the starting point for searching your contents. Interactions with the search bar are handled automatically by the `UISearchController` object, which notifies the object in the [`searchResultsUpdater`](uisearchcontroller/searchresultsupdater.md) property whenever the search information changes.

You can provide a custom search bar by subclassing [`UISearchController`](uisearchcontroller.md) and overriding this property to return your custom implementation. To ensure the correct configuration of your search bar, lazily initialize it when it’s first requested, as shown in the code below.

**Swift**:

```swift
class CustomSearchController: UISearchController {

    // Mark this property as lazy to defer initialization until
    // the searchBar property is called.
    private lazy var customSearchBar = CustomSearchBar()


    // Override this property to return your custom implementation.
    override var searchBar: UISearchBar { customSearchBar }
}
```

**Objective-C**:

```objc
@implementation CustomSearchController {
    CustomSearchBar *customSearchBar;
}

// Override this property to return your custom implementation.
- (UISearchBar *)searchBar {
    // Lazily initialize your custom search bar.
    if (!customSearchBar) {
        customSearchBar = [[CustomSearchBar alloc] init];
    }
    return customSearchBar;
}

@end
```

## See Also

- [var searchResultsUpdater: (any UISearchResultsUpdating)?](uisearchcontroller/searchresultsupdater.md)
  The object responsible for updating the contents of the search results controller.
- [var searchResultsController: UIViewController?](uisearchcontroller/searchresultscontroller.md)
  The view controller that displays the results of the search.
- [var isActive: Bool](uisearchcontroller/isactive.md)
  The presented state of the search interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/searchbar)*