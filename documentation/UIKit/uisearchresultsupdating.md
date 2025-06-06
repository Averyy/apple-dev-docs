# UISearchResultsUpdating

**Framework**: UIKit  
**Kind**: protocol

A set of methods that let you update search results based on information the user enters into the search bar.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UISearchResultsUpdating : NSObjectProtocol
```

## Topics

### Updating the search bar
- [func updateSearchResults(for: UISearchController)](uisearchresultsupdating/updatesearchresults(for:).md)
  Asks the object to update the search results for a specified controller.
- [func updateSearchResults(for: UISearchController, selecting: any UISearchSuggestion)](uisearchresultsupdating/updatesearchresults(for:selecting:).md)
  Asks the object to update the search results for a specified controller after the user selects a search suggestion.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UISearchContainerViewController](uisearchcontainerviewcontroller.md)
  A view controller that manages the presentation of search results in your interface.
- [class UISearchController](uisearchcontroller.md)
  A view controller that manages the display of search results based on interactions with a search bar.
- [class UISearchBar](uisearchbar.md)
  A specialized view for receiving search-related information from the user.
- [Displaying searchable content by using a search controller](displaying-searchable-content-by-using-a-search-controller.md)
  Create a user interface with searchable content in a table view.
- [Using suggested searches with a search controller](using-suggested-searches-with-a-search-controller.md)
  Create a search interface with a table view of suggested searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchresultsupdating)*