# setBadgeTextAttributes(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers text attributes that the badge uses for the specified state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func setBadgeTextAttributes(_ textAttributes: [NSAttributedString.Key : Any]?, for state: UIControl.State)
```

```objc
- (void) setBadgeTextAttributes:(NSDictionary<NSString *,id> *) textAttributes forState:(UIControlState) state;
```

#### Discussion

The [`setTitleTextAttributes(_:for:)`](../uibaritem/settitletextattributes%28_,for%29.md) method allows you to customize the appearance of the item’s title. Use this method to apply similar customizations to the badge’s value to achieve a consistent appearance.

## Parameters

- `textAttributes`: A dictionary of text attributes. For a list of possible attributes, see [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md).
- `state`: The item’s state. For possible values, see [`UIControl.State`](../uicontrol/state-swift.struct.md).

## See Also

### Configuring the item’s badge
- [var badgeValue: String?](./badgevalue.md)
  The text that the item’s badge displays.
- [var badgeColor: UIColor?](./badgecolor.md)
  The background color of the item’s badge.
- [func badgeTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](./badgetextattributes%28for%29.md)
  Returns the badge’s text attributes for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/setbadgetextattributes(_:for:))*