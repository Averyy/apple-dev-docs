# isFocused

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item is currently focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isFocused: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isFocused) BOOL focused;
```

#### Discussion

This is a convenience property that checks whether the item is equal to the value in the [`UIScreen`](../uiscreen.md) class’s [`focusedView`](../uiscreen/focusedview.md) property.

## See Also

### Working with focus
- [var canBecomeFocused: Bool](./canbecomefocused.md)
  A Boolean value that indicates whether the view is currently capable of being focused.
- [class var inheritedAnimationDuration: TimeInterval](./inheritedanimationduration.md)
  Returns the inherited duration of the current animation.
- [var focusGroupIdentifier: String?](./focusgroupidentifier.md)
  The identifier of the focus group that this view belongs to.
- [var focusEffect: UIFocusEffect?](./focuseffect.md)
  The visual effect to apply when the view becomes focused.
- [var focusGroupPriority: UIFocusGroupPriority](./focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/isfocused)*