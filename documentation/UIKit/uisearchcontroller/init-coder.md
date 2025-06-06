# init(coder:)

**Framework**: UIKit  
**Kind**: init

Returns an initialized search controller from data in the specified unarchiver.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(coder: NSCoder)
```

#### Return Value

An initialized search controller, or `nil` if the coder doesn’t define a search controller.

## Parameters

- `coder`: An unarchiver object.

## See Also

- [init(searchResultsController: UIViewController?)](uisearchcontroller/init(searchresultscontroller:).md)
  Creates and returns a search controller with the specified view controller for displaying the results.
- [init(nibName: String?, bundle: Bundle?)](uisearchcontroller/init(nibname:bundle:).md)
  Returns an initialized view controller with the nib file in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/init(coder:))*