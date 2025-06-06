# focusEffect

**Framework**: UIKit  
**Kind**: property

The visual effect to apply when the view becomes focused.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var focusEffect: UIFocusEffect? { get set }
```

#### Discussion

If this property is `nil`, the system doesn’t apply an effect when the view becomes focused.

## See Also

- [var canBecomeFocused: Bool](uiview/canbecomefocused.md)
  A Boolean value that indicates whether the view is currently capable of being focused.
- [class var inheritedAnimationDuration: TimeInterval](uiview/inheritedanimationduration.md)
  Returns the inherited duration of the current animation.
- [var isFocused: Bool](uiview/isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
- [var focusGroupIdentifier: String?](uiview/focusgroupidentifier.md)
  The identifier of the focus group that this view belongs to.
- [var focusGroupPriority: UIFocusGroupPriority](uiview/focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/focuseffect)*