# init(nibName:bundle:)

**Framework**: UIKit  
**Kind**: init

Returns an initialized view controller with the nib file in the specified bundle.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)
```

## Parameters

- `nibNameOrNil`: The name of the nib file to associate with the view controller. The nib file name shouldn’t contain any leading path information. If you specify  , the   property is set to  .
- `nibBundleOrNil`: The bundle in which to search for the nib file. This method looks for the nib file in the bundle’s language-specific project directories first, followed by the Resources directory.

## See Also

- [init(searchResultsController: UIViewController?)](uisearchcontroller/init(searchresultscontroller:).md)
  Creates and returns a search controller with the specified view controller for displaying the results.
- [init?(coder: NSCoder)](uisearchcontroller/init(coder:).md)
  Returns an initialized search controller from data in the specified unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/init(nibname:bundle:))*