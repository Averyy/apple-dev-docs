# init(searchResultsController:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a search controller with the specified view controller for displaying the results.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(searchResultsController: UIViewController?)
```

#### Return Value

An initialized search controller.

#### Discussion

After creating the search controller, always assign an object to the [`searchResultsUpdater`](uisearchcontroller/searchresultsupdater.md) property. The search controller uses that object to update the search results.

## Parameters

- `searchResultsController`: The view controller that displays the search results. Specify   if you want to display the search results in the same view controller that displays your searchable content. For apps running in tvOS, provide a results controller because tvOS doesn’t accept   as a valid argument.

## See Also

- [init?(coder: NSCoder)](uisearchcontroller/init(coder:).md)
  Returns an initialized search controller from data in the specified unarchiver.
- [init(nibName: String?, bundle: Bundle?)](uisearchcontroller/init(nibname:bundle:).md)
  Returns an initialized view controller with the nib file in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/init(searchresultscontroller:))*