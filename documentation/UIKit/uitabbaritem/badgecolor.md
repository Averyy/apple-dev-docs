# badgeColor

**Framework**: UIKit  
**Kind**: property

The background color of the item’s badge.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var badgeColor: UIColor? { get set }
```

#### Discussion

The default value is `nil`. If you don’t specify a value, the item uses [`systemRed`](uicolor/systemred.md).

## See Also

- [var badgeValue: String?](uitabbaritem/badgevalue.md)
  The text that the item’s badge displays.
- [func setBadgeTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uitabbaritem/setbadgetextattributes(_:for:).md)
  Registers text attributes that the badge uses for the specified state.
- [func badgeTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uitabbaritem/badgetextattributes(for:).md)
  Returns the badge’s text attributes for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/badgecolor)*