# viewLayoutMarginsDidChange()

**Framework**: UIKit  
**Kind**: method

Called to notify the view controller that the layout margins of its root view changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func viewLayoutMarginsDidChange()
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Discussion

Use this method to update the position of content based on the new margin values.

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var viewRespectsSystemMinimumLayoutMargins: Bool](uiviewcontroller/viewrespectssystemminimumlayoutmargins.md)
  A Boolean value indicating whether the view controller’s view uses the system-defined minimum layout margins.
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](uiviewcontroller/systemminimumlayoutmargins.md)
  The minimum layout margins for the view controller’s root view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewlayoutmarginsdidchange())*