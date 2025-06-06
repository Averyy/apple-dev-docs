# inheritedAnimationDuration

**Framework**: UIKit  
**Kind**: property

Returns the inherited duration of the current animation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var inheritedAnimationDuration: TimeInterval { get }
```

#### Return Value

The duration of the current animation.

#### Discussion

This method only returns a non-zero value if called within a [`UIView`](uiview.md) animation block.

## See Also

- [var canBecomeFocused: Bool](uiview/canbecomefocused.md)
  A Boolean value that indicates whether the view is currently capable of being focused.
- [var isFocused: Bool](uiview/isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
- [var focusGroupIdentifier: String?](uiview/focusgroupidentifier.md)
  The identifier of the focus group that this view belongs to.
- [var focusEffect: UIFocusEffect?](uiview/focuseffect.md)
  The visual effect to apply when the view becomes focused.
- [var focusGroupPriority: UIFocusGroupPriority](uiview/focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/inheritedanimationduration)*