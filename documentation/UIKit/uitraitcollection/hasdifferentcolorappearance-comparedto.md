# hasDifferentColorAppearance(comparedTo:)

**Framework**: UIKit  
**Kind**: method

Queries whether changing between the specified and current trait collections would affect color values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func hasDifferentColorAppearance(comparedTo traitCollection: UITraitCollection?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the colors in the two trait collections differ, or [`false`](https://developer.apple.com/documentation/Swift/false) if they have the same component values.

#### Discussion

Use this method to determine whether changing the traits of the current environment would also change the colors in your interface. For example, changing the [`userInterfaceStyle`](uitraitcollection/userinterfacestyle.md) or [`accessibilityContrast`](uitraitcollection/accessibilitycontrast.md) property usually changes the colors of your interface.

## Parameters

- `traitCollection`: A trait collection that you want to compare to the current trait collection.

## See Also

- [func containsTraits(in: UITraitCollection?) -> Bool](uitraitcollection/containstraits(in:).md)
  Queries whether a trait collection contains all of another trait collection’s values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/hasdifferentcolorappearance(comparedto:))*