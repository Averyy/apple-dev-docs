# disabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance data to apply to the tab bar item when it’s disabled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var disabled: UITabBarItemStateAppearance { get }
```

```objc
@property (nonatomic, strong, readonly) UITabBarItemStateAppearance * disabled;
```

## Discussion

To set the attributes for this state, get the object in this property and modify it.

## See Also

### Configuring attributes for different item states
- [var normal: UITabBarItemStateAppearance](./normal.md)
  The appearance data to apply to the tab bar item when it’s enabled, unselected, and not the focused item.
- [var selected: UITabBarItemStateAppearance](./selected.md)
  The appearance data to apply to the tab bar item when it’s selected.
- [var focused: UITabBarItemStateAppearance](./focused.md)
  The appearance data to apply to the tab bar item when it’s focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemappearance/disabled)*