# safeAreaInsetsDidChange()

**Framework**: UIKit  
**Kind**: method

Called when the safe area of the view changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func safeAreaInsetsDidChange()
```

## See Also

- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [var safeAreaInsets: UIEdgeInsets](uiview/safeareainsets.md)
  The insets that you use to determine the safe area for this view.
- [var safeAreaLayoutGuide: UILayoutGuide](uiview/safearealayoutguide.md)
  The layout guide representing the portion of your view that is unobscured by bars and other content.
- [var insetsLayoutMarginsFromSafeArea: Bool](uiview/insetslayoutmarginsfromsafearea.md)
  A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/safeareainsetsdidchange())*