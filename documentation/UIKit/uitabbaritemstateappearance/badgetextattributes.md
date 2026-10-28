# badgeTextAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

String attributes to apply to the text of the item’s badge.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var badgeTextAttributes: [NSAttributedString.Key : Any] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSDictionary<NSString *,id> * badgeTextAttributes;
```

## Discussion

If you don’t specify font or color attributes for the text, UIKit supplies appropriate default values. For a list of possible keys, see [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md).

## See Also

### Configuring the badge appearance
- [var badgeBackgroundColor: UIColor?](./badgebackgroundcolor.md)
  The background color of the badge.
- [var badgeTitlePositionAdjustment: UIOffset](./badgetitlepositionadjustment.md)
  The additional amount by which to offset the badge’s title horizontally and vertically.
- [var badgePositionAdjustment: UIOffset](./badgepositionadjustment.md)
  The additional amount by which to offset the badge horizontally and vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemstateappearance/badgetextattributes)*