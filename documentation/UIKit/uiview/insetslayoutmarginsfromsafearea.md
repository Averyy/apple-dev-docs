# insetsLayoutMarginsFromSafeArea

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var insetsLayoutMarginsFromSafeArea: Bool { get set }
```

## Mentions

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), any margins that are outside the safe area are automatically modified to fall within the safe area boundary. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true). Changing the value to [`false`](https://developer.apple.com/documentation/Swift/false) allows your margins to remain at their original locations, even when they are outside the safe area.

## See Also

- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [var safeAreaInsets: UIEdgeInsets](uiview/safeareainsets.md)
  The insets that you use to determine the safe area for this view.
- [var safeAreaLayoutGuide: UILayoutGuide](uiview/safearealayoutguide.md)
  The layout guide representing the portion of your view that is unobscured by bars and other content.
- [func safeAreaInsetsDidChange()](uiview/safeareainsetsdidchange.md)
  Called when the safe area of the view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/insetslayoutmarginsfromsafearea)*