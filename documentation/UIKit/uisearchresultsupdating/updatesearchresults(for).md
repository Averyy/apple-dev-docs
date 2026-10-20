# updateSearchResults(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the object to update the search results for a specified controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func updateSearchResults(for searchController: UISearchController)
```

```objc
- (void) updateSearchResultsForSearchController:(UISearchController *) searchController;
```

#### Discussion

The system calls this method when the search bar becomes the first responder or the search bar’s text changes. Perform any required filtering and updating of search results or suggestions inside of this method.

## Parameters

- `searchController`: The [`UISearchController`](../uisearchcontroller.md) object used as the search bar.

## See Also

### Updating the search bar
- [func updateSearchResults(for: UISearchController, selecting: any UISearchSuggestion)](./updatesearchresults%28for,selecting%29.md)
  Asks the object to update the search results for a specified controller after the user selects a search suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchresultsupdating/updatesearchresults(for:))*