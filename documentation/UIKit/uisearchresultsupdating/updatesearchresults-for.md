# updateSearchResults(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the object to update the search results for a specified controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateSearchResults(for searchController: UISearchController)
```

#### Discussion

The system calls this method when the search bar becomes the first responder or the search bar’s text changes. Perform any required filtering and updating of search results or suggestions inside of this method.

## Parameters

- `searchController`: The   object used as the search bar.

## See Also

- [func updateSearchResults(for: UISearchController, selecting: any UISearchSuggestion)](uisearchresultsupdating/updatesearchresults(for:selecting:).md)
  Asks the object to update the search results for a specified controller after the user selects a search suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchresultsupdating/updatesearchresults(for:))*