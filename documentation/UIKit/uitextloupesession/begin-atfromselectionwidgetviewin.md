# begin(at:fromSelectionWidgetView:in:)

**Framework**: UIKit  
**Kind**: method

Creates a new loupe session and displays the loupe at the specified location in your view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+

## Declaration

```swift
@MainActor
class func begin(at point: CGPoint, fromSelectionWidgetView selectionWidget: UIView?, in interactionView: UIView) -> Self?
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Return Value

A new loupe session for the specified view. The method returns `nil` if showing the loupe is inappropriate in the current context.

#### Discussion

Call this method to animate the appearance of the loupe at the specified `point` in `interactionView`.  Store a strong reference to this returned session and use it to update the position of the loupe. To hide the loupe again, call [`invalidate()`](uitextloupesession/invalidate().md) and then remove your reference to the session.

## Parameters

- `point`: The point in your view’s coordinate system that you want to magnify using the loupe. When creating the loupe with a gesture recognizer, specify the location of the gesture.
- `selectionWidget`: The view associated with the insertion point. When using a   object to display selections in your view, specify the view in the interaction object’s   property for this parameter.
- `interactionView`: The view in which to display the loupe. Specify all coordinate values relative to this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextloupesession/begin(at:fromselectionwidgetview:in:))*