# searchResultsController

**Framework**: UIKit  
**Kind**: property

The view controller that displays the results of the search.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var searchResultsController: UIViewController? { get }
```

#### Discussion

When the user enters text in the search bar, the search controller displays this view controller immediately and without any animations. You’re responsible for passing the search results to this view controller so that they can be displayed. You do this using the object in the [`searchResultsUpdater`](uisearchcontroller/searchresultsupdater.md) property.

When the value of this property is `nil`, the search controller doesn’t present a separate view controller for the search results. Instead, you should display the results using the original view controller containing the search bar and searchable contents.

## See Also

- [var searchBar: UISearchBar](uisearchcontroller/searchbar.md)
  The search bar to install in your interface.
- [var searchResultsUpdater: (any UISearchResultsUpdating)?](uisearchcontroller/searchresultsupdater.md)
  The object responsible for updating the contents of the search results controller.
- [var isActive: Bool](uisearchcontroller/isactive.md)
  The presented state of the search interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/searchresultscontroller)*