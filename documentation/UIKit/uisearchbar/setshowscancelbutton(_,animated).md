# setShowsCancelButton(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the display state of the cancel button optionally with animation.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setShowsCancelButton(_ showsCancelButton: Bool, animated: Bool)
```

```objc
- (void) setShowsCancelButton:(BOOL) showsCancelButton animated:(BOOL) animated;
```

## Discussion

Cancel buttons are not displayed for apps running on iPad, even when you specify [`true`](../../Swift/true.md) for the `showsCancelButton` parameter

## Parameters

- `showsCancelButton`: [`true`](../../Swift/true.md) to display the cancel button, otherwise [`false`](../../Swift/false.md).
- `animated`: [`true`](../../Swift/true.md) to use animation to change the display state of the cancel button, otherwise [`false`](../../Swift/false.md).

## See Also

### Configuring the search interface
- [var showsBookmarkButton: Bool](./showsbookmarkbutton.md)
  A Boolean value indicating whether the bookmark button is displayed.
- [var showsCancelButton: Bool](./showscancelbutton.md)
  A Boolean value indicating whether the cancel button is displayed.
- [var showsSearchResultsButton: Bool](./showssearchresultsbutton.md)
  A Boolean value indicating whether the search results button is displayed.
- [var isSearchResultsButtonSelected: Bool](./issearchresultsbuttonselected.md)
  A Boolean value indicating whether the search results button is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/setshowscancelbutton(_:animated:))*