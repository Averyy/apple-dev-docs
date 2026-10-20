# safeAreaInsetsDidChange()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when the safe area of the view changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func safeAreaInsetsDidChange()
```

```objc
- (void) safeAreaInsetsDidChange;
```

## See Also

### Getting the safe area
- [Positioning content relative to the safe area](../positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [var safeAreaInsets: UIEdgeInsets](./safeareainsets.md)
  The insets that you use to determine the safe area for this view.
- [var safeAreaLayoutGuide: UILayoutGuide](./safearealayoutguide.md)
  The layout guide representing the portion of your view that is unobscured by bars and other content.
- [var insetsLayoutMarginsFromSafeArea: Bool](./insetslayoutmarginsfromsafearea.md)
  A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/safeareainsetsdidchange())*