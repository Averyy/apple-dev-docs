# searchResultsUpdater

**Framework**: UIKit  
**Kind**: property

The object responsible for updating the contents of the search results controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var searchResultsUpdater: (any UISearchResultsUpdating)? { get set }
```

#### Discussion

Assign an object that adopts the [`UISearchResultsUpdating`](uisearchresultsupdating.md) protocol. Use the methods of that protocol to search your content and deliver the results to your search results view controller. The object contained by the [`searchResultsUpdater`](uisearchcontroller/searchresultsupdater.md) property is often the view controller that’s set during initialization.

## See Also

- [var searchBar: UISearchBar](uisearchcontroller/searchbar.md)
  The search bar to install in your interface.
- [var searchResultsController: UIViewController?](uisearchcontroller/searchresultscontroller.md)
  The view controller that displays the results of the search.
- [var isActive: Bool](uisearchcontroller/isactive.md)
  The presented state of the search interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/searchresultsupdater)*