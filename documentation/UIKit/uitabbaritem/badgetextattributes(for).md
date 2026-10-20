# badgeTextAttributes(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the badge’s text attributes for the specified state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func badgeTextAttributes(for state: UIControl.State) -> [NSAttributedString.Key : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) badgeTextAttributesForState:(UIControlState) state;
```

#### Discussion

Use this method to retrieve the attributes the item applies to its badge’s value for the specified state. For a list of attributes, see [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md).

## Parameters

- `state`: The item’s state. For possible values, see [`UIControl.State`](../uicontrol/state-swift.struct.md).

## See Also

### Configuring the item’s badge
- [var badgeValue: String?](./badgevalue.md)
  The text that the item’s badge displays.
- [var badgeColor: UIColor?](./badgecolor.md)
  The background color of the item’s badge.
- [func setBadgeTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](./setbadgetextattributes%28_,for%29.md)
  Registers text attributes that the badge uses for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/badgetextattributes(for:))*