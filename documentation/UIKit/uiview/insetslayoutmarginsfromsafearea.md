# insetsLayoutMarginsFromSafeArea

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var insetsLayoutMarginsFromSafeArea: Bool { get set }
```

```objc
@property (nonatomic) BOOL insetsLayoutMarginsFromSafeArea;
```

## Mentions

- [Positioning content within layout margins](../positioning-content-within-layout-margins.md)

## Discussion

When the value of this property is [`true`](../../Swift/true.md), any margins that are outside the safe area are automatically modified to fall within the safe area boundary. The default value of this property is [`true`](../../Swift/true.md). Changing the value to [`false`](../../Swift/false.md) allows your margins to remain at their original locations, even when they are outside the safe area.

## See Also

### Getting the safe area
- [Positioning content relative to the safe area](../positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [var safeAreaInsets: UIEdgeInsets](./safeareainsets.md)
  The insets that you use to determine the safe area for this view.
- [var safeAreaLayoutGuide: UILayoutGuide](./safearealayoutguide.md)
  The layout guide representing the portion of your view that is unobscured by bars and other content.
- [func safeAreaInsetsDidChange()](./safeareainsetsdidchange%28%29.md)
  Called when the safe area of the view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/insetslayoutmarginsfromsafearea)*