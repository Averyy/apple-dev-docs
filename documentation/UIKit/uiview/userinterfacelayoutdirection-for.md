# userInterfaceLayoutDirection(for:)

**Framework**: UIKit  
**Kind**: method

Returns the user interface direction for the given semantic content attribute.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func userInterfaceLayoutDirection(for attribute: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection
```

#### Return Value

The user interface layout direction (left-to-right or right-to-left).

#### Discussion

When creating a view that contains subviews, you can use this method to determine whether the subviews should be flipped, and lay out the views in the appropriate order.

## Parameters

- `attribute`: The semantic content attribute for a view.

## See Also

- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](uiview/overrideuserinterfacestyle.md)
  The user interface style adopted by the view and all of its subviews.
- [var semanticContentAttribute: UISemanticContentAttribute](uiview/semanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [var effectiveUserInterfaceLayoutDirection: UIUserInterfaceLayoutDirection](uiview/effectiveuserinterfacelayoutdirection.md)
  The user interface layout direction appropriate for arranging the immediate content of the view.
- [class func userInterfaceLayoutDirection(for: UISemanticContentAttribute, relativeTo: UIUserInterfaceLayoutDirection) -> UIUserInterfaceLayoutDirection](uiview/userinterfacelayoutdirection(for:relativeto:).md)
  Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/userinterfacelayoutdirection(for:))*