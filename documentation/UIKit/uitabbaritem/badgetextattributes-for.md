# badgeTextAttributes(for:)

**Framework**: UIKit  
**Kind**: method

Returns the badge’s text attributes for the specified state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func badgeTextAttributes(for state: UIControl.State) -> [NSAttributedString.Key : Any]?
```

#### Discussion

Use this method to retrieve the attributes the item applies to its badge’s value for the specified state. For a list of attributes, see [`NSAttributedString.Key`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key).

## Parameters

- `state`: The item’s state. For possible values, see  .

## See Also

- [var badgeValue: String?](uitabbaritem/badgevalue.md)
  The text that the item’s badge displays.
- [var badgeColor: UIColor?](uitabbaritem/badgecolor.md)
  The background color of the item’s badge.
- [func setBadgeTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uitabbaritem/setbadgetextattributes(_:for:).md)
  Registers text attributes that the badge uses for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/badgetextattributes(for:))*