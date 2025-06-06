# focusGroupPriority

**Framework**: UIKit  
**Kind**: property

The importance of the item within a focus group, used by the focus system to determine the group’s primary item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var focusGroupPriority: UIFocusGroupPriority { get set }
```

#### Discussion

The system automatically assigns each focusable item in a focus group one of the predefined system priorities. The visible item with the highest priority is the group’s primary item.

You can override the default priority of an item to customize the primary item of a group. When setting a custom priority, you can only increase the item’s priority above its system-provided value, not decrease it. The system-provided priority is always the minimum priority applied for the item. The system ignores any priority lower than `0`.

## See Also

- [var canBecomeFocused: Bool](uiview/canbecomefocused.md)
  A Boolean value that indicates whether the view is currently capable of being focused.
- [class var inheritedAnimationDuration: TimeInterval](uiview/inheritedanimationduration.md)
  Returns the inherited duration of the current animation.
- [var isFocused: Bool](uiview/isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
- [var focusGroupIdentifier: String?](uiview/focusgroupidentifier.md)
  The identifier of the focus group that this view belongs to.
- [var focusEffect: UIFocusEffect?](uiview/focuseffect.md)
  The visual effect to apply when the view becomes focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/focusgrouppriority)*