# canBecomeFocused

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view is currently capable of being focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var canBecomeFocused: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canBecomeFocused;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the view can become focused; [`false`](../../Swift/false.md) otherwise.

By default, the value of this property is [`false`](../../Swift/false.md). This property informs the focus engine if a view is capable of being focused. Sometimes even if a view returns [`true`](../../Swift/true.md), a view may not be focusable for the following reasons:

- The view is hidden.
- The view has alpha set to 0.
- The view has `userInteractionEnabled` set to [`false`](../../Swift/false.md).
- The view is not currently in the view hierarchy.

## See Also

### Working with focus
- [class var inheritedAnimationDuration: TimeInterval](./inheritedanimationduration.md)
  Returns the inherited duration of the current animation.
- [var isFocused: Bool](./isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
- [var focusGroupIdentifier: String?](./focusgroupidentifier.md)
  The identifier of the focus group that this view belongs to.
- [var focusEffect: UIFocusEffect?](./focuseffect.md)
  The visual effect to apply when the view becomes focused.
- [var focusGroupPriority: UIFocusGroupPriority](./focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/canbecomefocused)*