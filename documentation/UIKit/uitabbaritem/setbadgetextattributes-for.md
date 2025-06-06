# setBadgeTextAttributes(_:for:)

**Framework**: UIKit  
**Kind**: method

Registers text attributes that the badge uses for the specified state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBadgeTextAttributes(_ textAttributes: [NSAttributedString.Key : Any]?, for state: UIControl.State)
```

#### Discussion

The [`setTitleTextAttributes(_:for:)`](uibaritem/settitletextattributes(_:for:).md) method allows you to customize the appearance of the item’s title. Use this method to apply similar customizations to the badge’s value to achieve a consistent appearance.

## Parameters

- `textAttributes`: A dictionary of text attributes. For a list of possible attributes, see  .
- `state`: The item’s state. For possible values, see  .

## See Also

- [var badgeValue: String?](uitabbaritem/badgevalue.md)
  The text that the item’s badge displays.
- [var badgeColor: UIColor?](uitabbaritem/badgecolor.md)
  The background color of the item’s badge.
- [func badgeTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uitabbaritem/badgetextattributes(for:).md)
  Returns the badge’s text attributes for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/setbadgetextattributes(_:for:))*