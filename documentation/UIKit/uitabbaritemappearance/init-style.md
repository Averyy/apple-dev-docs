# init(style:)

**Framework**: UIKit  
**Kind**: init

Creates an appearance object with appropriate default values for a tab bar, displaying its items with the specified layout style.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(style: UITabBarItemAppearance.Style)
```

#### Return Value

A new appearance object containing appropriate default values for the specified layout style.

## Parameters

- `style`: The layout style for the appearance attributes. UIKit uses this value to configure the default appearance attributes. For a list of possible values, see  .

## See Also

- [convenience init()](uitabbaritemappearance/init.md)
  Creates an appearance object with default values for a stacked tab bar item.
- [init(coder: NSCoder)](uitabbaritemappearance/init(coder:).md)
  Creates an appearance object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemappearance/init(style:))*