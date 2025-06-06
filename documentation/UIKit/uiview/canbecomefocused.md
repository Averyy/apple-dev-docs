# canBecomeFocused

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the view is currently capable of being focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canBecomeFocused: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the view can become focused; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

By default, the value of this property is [`false`](https://developer.apple.com/documentation/swift/false). This property informs the focus engine if a view is capable of being focused. Sometimes even if a view returns [`true`](https://developer.apple.com/documentation/swift/true), a view may not be focusable for the following reasons:

- The view is hidden.
- The view has alpha set to 0.
- The view has `userInteractionEnabled` set to [`false`](https://developer.apple.com/documentation/swift/false).
- The view is not currently in the view hierarchy.

## See Also

- [class var inheritedAnimationDuration: TimeInterval](uiview/inheritedanimationduration.md)
  Returns the inherited duration of the current animation.
- [var isFocused: Bool](uiview/isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
- [var focusGroupIdentifier: String?](uiview/focusgroupidentifier.md)
  The identifier of the focus group that this view belongs to.
- [var focusEffect: UIFocusEffect?](uiview/focuseffect.md)
  The visual effect to apply when the view becomes focused.
- [var focusGroupPriority: UIFocusGroupPriority](uiview/focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/canbecomefocused)*