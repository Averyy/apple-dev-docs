# badgeValue

**Framework**: UIKit  
**Kind**: property

The text that the item’s badge displays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var badgeValue: String? { get set }
```

#### Discussion

The default value is `nil`.

## See Also

- [var badgeColor: UIColor?](uitabbaritem/badgecolor.md)
  The background color of the item’s badge.
- [func setBadgeTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uitabbaritem/setbadgetextattributes(_:for:).md)
  Registers text attributes that the badge uses for the specified state.
- [func badgeTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uitabbaritem/badgetextattributes(for:).md)
  Returns the badge’s text attributes for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/badgevalue)*