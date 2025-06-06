# userInterfaceLayoutDirection(for:relativeTo:)

**Framework**: UIKit  
**Kind**: method

Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func userInterfaceLayoutDirection(for semanticContentAttribute: UISemanticContentAttribute, relativeTo layoutDirection: UIUserInterfaceLayoutDirection) -> UIUserInterfaceLayoutDirection
```

#### Return Value

The layout direction implied by the semantic content attribute and relative to the layout direction.

#### Discussion

For example, when this method is passed a layout direction of [`UIUserInterfaceLayoutDirection.rightToLeft`](uiuserinterfacelayoutdirection/righttoleft.md) and a semantic content attribute of [`UISemanticContentAttribute.playback`](uisemanticcontentattribute/playback.md), it returns [`UIUserInterfaceLayoutDirection.leftToRight`](uiuserinterfacelayoutdirection/lefttoright.md). Although layout and drawing code can use this method to determine how to arrange elements, it might be easier to query the container view’s [`effectiveUserInterfaceLayoutDirection`](uiview/effectiveuserinterfacelayoutdirection.md) property instead.

## Parameters

- `semanticContentAttribute`: The semantic content attribute for a view.
- `layoutDirection`: The user interface layout direction (  or  ).

## See Also

- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](uiview/overrideuserinterfacestyle.md)
  The user interface style adopted by the view and all of its subviews.
- [var semanticContentAttribute: UISemanticContentAttribute](uiview/semanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [var effectiveUserInterfaceLayoutDirection: UIUserInterfaceLayoutDirection](uiview/effectiveuserinterfacelayoutdirection.md)
  The user interface layout direction appropriate for arranging the immediate content of the view.
- [class func userInterfaceLayoutDirection(for: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection](uiview/userinterfacelayoutdirection(for:).md)
  Returns the user interface direction for the given semantic content attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/userinterfacelayoutdirection(for:relativeto:))*