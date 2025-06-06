# badgePositionAdjustment

**Framework**: UIKit  
**Kind**: property

The additional amount by which to offset the badge horizontally and vertically.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var badgePositionAdjustment: UIOffset { get set }
```

#### Discussion

Use this property to specify the distance, in points, by which to offset the badge from its default position over its item. Positive values move the title down and to the right. Negative values move the title up and to the left.

## See Also

- [var badgeTextAttributes: [NSAttributedString.Key : Any]](uitabbaritemstateappearance/badgetextattributes.md)
  String attributes to apply to the text of the item’s badge.
- [var badgeBackgroundColor: UIColor?](uitabbaritemstateappearance/badgebackgroundcolor.md)
  The background color of the badge.
- [var badgeTitlePositionAdjustment: UIOffset](uitabbaritemstateappearance/badgetitlepositionadjustment.md)
  The additional amount by which to offset the badge’s title horizontally and vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemstateappearance/badgepositionadjustment)*