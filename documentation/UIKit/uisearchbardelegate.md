# UISearchBarDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A collection of optional methods that you implement to make a search bar control functional.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UISearchBarDelegate : UIBarPositioningDelegate
```

```objc
@protocol UISearchBarDelegate <UIBarPositioningDelegate>
```

#### Overview

A [`UISearchBar`](./uisearchbar.md) object provides the user interface for a search field on a bar, but it’s the application’s responsibility to implement the actions when buttons are tapped. At a minimum, the delegate needs to perform the actual search when text is entered in the text field.

## Topics

### Managing the search text
- [func searchBar(UISearchBar, textDidChange: String)](./uisearchbardelegate/searchbar%28_,textdidchange%29.md)
  Tells the delegate that the user changed the search text.
- [func searchBarShouldBeginEditing(UISearchBar) -> Bool](./uisearchbardelegate/searchbarshouldbeginediting%28_%29.md)
  Asks the delegate if editing should begin in the specified search bar.
- [func searchBarTextDidBeginEditing(UISearchBar)](./uisearchbardelegate/searchbartextdidbeginediting%28_%29.md)
  Tells the delegate when the user begins editing the search text.
- [func searchBarShouldEndEditing(UISearchBar) -> Bool](./uisearchbardelegate/searchbarshouldendediting%28_%29.md)
  Asks the delegate if editing should stop in the specified search bar.
- [func searchBarTextDidEndEditing(UISearchBar)](./uisearchbardelegate/searchbartextdidendediting%28_%29.md)
  Tells the delegate that the user finished editing the search text.
- [func searchBar(UISearchBar, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./uisearchbardelegate/searchbar%28_,shouldchangetextin,replacementtext%29.md)
  Ask the delegate if text in a specified range should be replaced with given text.
### Responding to clicks in search controls
- [func searchBarBookmarkButtonClicked(UISearchBar)](./uisearchbardelegate/searchbarbookmarkbuttonclicked%28_%29.md)
  Tells the delegate that the bookmark button was tapped.
- [func searchBarCancelButtonClicked(UISearchBar)](./uisearchbardelegate/searchbarcancelbuttonclicked%28_%29.md)
  Tells the delegate that the cancel button was tapped.
- [func searchBarSearchButtonClicked(UISearchBar)](./uisearchbardelegate/searchbarsearchbuttonclicked%28_%29.md)
  Tells the delegate that the search button was tapped.
- [func searchBarResultsListButtonClicked(UISearchBar)](./uisearchbardelegate/searchbarresultslistbuttonclicked%28_%29.md)
  Tells the delegate that the search results list button was tapped.
### Responding to scope button changes
- [func searchBar(UISearchBar, selectedScopeButtonIndexDidChange: Int)](./uisearchbardelegate/searchbar%28_,selectedscopebuttonindexdidchange%29.md)
  Tells the delegate that the scope button selection changed.
### Instance Methods
- [func searchBar(UISearchBar, shouldChangeTextInRanges: [NSValue], replacementText: String) -> Bool](./uisearchbardelegate/searchbar%28_,shouldchangetextinranges,replacementtext%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIBarPositioningDelegate](./uibarpositioningdelegate.md)

## See Also

### Handling search bar interactions
- [var delegate: (any UISearchBarDelegate)?](./uisearchbar/delegate.md)
  The search bar’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate)*