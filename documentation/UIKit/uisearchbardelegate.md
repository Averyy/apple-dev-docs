# UISearchBarDelegate

**Framework**: UIKit  
**Kind**: protocol

A collection of optional methods that you implement to make a search bar control functional.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UISearchBarDelegate : UIBarPositioningDelegate
```

#### Overview

A [`UISearchBar`](uisearchbar.md) object provides the user interface for a search field on a bar, but it’s the application’s responsibility to implement the actions when buttons are tapped. At a minimum, the delegate needs to perform the actual search when text is entered in the text field.

## Topics

### Managing the search text
- [func searchBar(UISearchBar, textDidChange: String)](uisearchbardelegate/searchbar(_:textdidchange:).md)
  Tells the delegate that the user changed the search text.
- [func searchBar(UISearchBar, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](uisearchbardelegate/searchbar(_:shouldchangetextin:replacementtext:).md)
  Ask the delegate if text in a specified range should be replaced with given text.
- [func searchBarShouldBeginEditing(UISearchBar) -> Bool](uisearchbardelegate/searchbarshouldbeginediting(_:).md)
  Asks the delegate if editing should begin in the specified search bar.
- [func searchBarTextDidBeginEditing(UISearchBar)](uisearchbardelegate/searchbartextdidbeginediting(_:).md)
  Tells the delegate when the user begins editing the search text.
- [func searchBarShouldEndEditing(UISearchBar) -> Bool](uisearchbardelegate/searchbarshouldendediting(_:).md)
  Asks the delegate if editing should stop in the specified search bar.
- [func searchBarTextDidEndEditing(UISearchBar)](uisearchbardelegate/searchbartextdidendediting(_:).md)
  Tells the delegate that the user finished editing the search text.
### Responding to clicks in search controls
- [func searchBarBookmarkButtonClicked(UISearchBar)](uisearchbardelegate/searchbarbookmarkbuttonclicked(_:).md)
  Tells the delegate that the bookmark button was tapped.
- [func searchBarCancelButtonClicked(UISearchBar)](uisearchbardelegate/searchbarcancelbuttonclicked(_:).md)
  Tells the delegate that the cancel button was tapped.
- [func searchBarSearchButtonClicked(UISearchBar)](uisearchbardelegate/searchbarsearchbuttonclicked(_:).md)
  Tells the delegate that the search button was tapped.
- [func searchBarResultsListButtonClicked(UISearchBar)](uisearchbardelegate/searchbarresultslistbuttonclicked(_:).md)
  Tells the delegate that the search results list button was tapped.
### Responding to scope button changes
- [func searchBar(UISearchBar, selectedScopeButtonIndexDidChange: Int)](uisearchbardelegate/searchbar(_:selectedscopebuttonindexdidchange:).md)
  Tells the delegate that the scope button selection changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIBarPositioningDelegate](uibarpositioningdelegate.md)

## See Also

- [var delegate: (any UISearchBarDelegate)?](uisearchbar/delegate.md)
  The search bar’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate)*