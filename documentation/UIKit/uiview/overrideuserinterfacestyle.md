# overrideUserInterfaceStyle

**Framework**: UIKit  
**Kind**: property

The user interface style adopted by the view and all of its subviews.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var overrideUserInterfaceStyle: UIUserInterfaceStyle { get set }
```

## Mentions

- [Choosing a specific interface style for your iOS app](choosing-a-specific-interface-style-for-your-ios-app.md)

#### Discussion

Use this property to force the view to always adopt a light or dark interface style. The default value of this property is [`UIUserInterfaceStyle.unspecified`](uiuserinterfacestyle/unspecified.md), which causes the view to inherit the interface style from a parent view or view controller. If you assign a different value, the new style applies to the view and all of the subviews owned by the same view controller. (If the view hierarchy contains the root view of an embedded child view controller, the child view controller and its views do not inherit the interface style.) If the view is a [`UIWindow`](uiwindow.md) object, the new style applies to everything in the window, including the root view controller and all presented content.

## See Also

- [var semanticContentAttribute: UISemanticContentAttribute](uiview/semanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [var effectiveUserInterfaceLayoutDirection: UIUserInterfaceLayoutDirection](uiview/effectiveuserinterfacelayoutdirection.md)
  The user interface layout direction appropriate for arranging the immediate content of the view.
- [class func userInterfaceLayoutDirection(for: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection](uiview/userinterfacelayoutdirection(for:).md)
  Returns the user interface direction for the given semantic content attribute.
- [class func userInterfaceLayoutDirection(for: UISemanticContentAttribute, relativeTo: UIUserInterfaceLayoutDirection) -> UIUserInterfaceLayoutDirection](uiview/userinterfacelayoutdirection(for:relativeto:).md)
  Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/overrideuserinterfacestyle)*