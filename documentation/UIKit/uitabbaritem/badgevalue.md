# badgeValue

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text that the item’s badge displays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var badgeValue: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * badgeValue;
```

#### Discussion

The default value is `nil`.

## See Also

### Configuring the item’s badge
- [var badgeColor: UIColor?](./badgecolor.md)
  The background color of the item’s badge.
- [func setBadgeTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](./setbadgetextattributes%28_,for%29.md)
  Registers text attributes that the badge uses for the specified state.
- [func badgeTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](./badgetextattributes%28for%29.md)
  Returns the badge’s text attributes for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/badgevalue)*