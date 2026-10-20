# isActive

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The presented state of the search interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isActive) BOOL active;
```

#### Discussion

When the user taps in the search field of a managed search bar, the search controller automatically displays the search results controller. Usually, you get the value of this property to determine whether the search results are displayed. However, you can set this property to [`true`](../../Swift/true.md) to force the search interface to appear, even if the user hasn’t tapped in the search field.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Managing the search results
- [var searchBar: UISearchBar](./searchbar.md)
  The search bar to install in your interface.
- [var searchResultsUpdater: (any UISearchResultsUpdating)?](./searchresultsupdater.md)
  The object responsible for updating the contents of the search results controller.
- [var searchResultsController: UIViewController?](./searchresultscontroller.md)
  The view controller that displays the results of the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/isactive)*