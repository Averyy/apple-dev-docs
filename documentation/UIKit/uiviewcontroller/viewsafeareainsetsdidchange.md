# viewSafeAreaInsetsDidChange()

**Framework**: UIKit  
**Kind**: method

Called to notify the view controller that the safe area insets of its root view changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func viewSafeAreaInsetsDidChange()
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Discussion

Use this method to update your interface to accommodate the new safe area. UIKit updates the safe area in response to size changes to system bars or when you modify the additional safe area insets of your view controller. UIKit also calls this method immediately before your view appears onscreen.

## See Also

- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [var additionalSafeAreaInsets: UIEdgeInsets](uiviewcontroller/additionalsafeareainsets.md)
  Custom insets that you specify to modify the view controller’s safe area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewsafeareainsetsdidchange())*