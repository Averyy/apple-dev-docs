# updateSearchResults(for:selecting:)

**Framework**: UIKit  
**Kind**: method

Asks the object to update the search results for a specified controller after the user selects a search suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func updateSearchResults(for searchController: UISearchController, selecting searchSuggestion: any UISearchSuggestion)
```

#### Discussion

The system calls this method when the user selects a search suggestion. Perform any required filtering and updating of search results or suggestions inside of this method.

## Parameters

- `searchController`: The   object used as the search bar.
- `searchSuggestion`: The suggestion the user selected.

## See Also

- [func updateSearchResults(for: UISearchController)](uisearchresultsupdating/updatesearchresults(for:).md)
  Asks the object to update the search results for a specified controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchresultsupdating/updatesearchresults(for:selecting:))*