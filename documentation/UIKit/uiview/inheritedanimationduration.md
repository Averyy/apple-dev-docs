# inheritedAnimationDuration

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Returns the inherited duration of the current animation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class var inheritedAnimationDuration: TimeInterval { get }
```

```objc
@property (class, nonatomic, readonly) NSTimeInterval inheritedAnimationDuration;
```

## Return Value

The duration of the current animation.

## Discussion

This method only returns a non-zero value if called within a [`UIView`](../uiview.md) animation block.

## See Also

### Working with focus
- [var canBecomeFocused: Bool](./canbecomefocused.md)
  A Boolean value that indicates whether the view is currently capable of being focused.
- [var isFocused: Bool](./isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
- [var focusGroupIdentifier: String?](./focusgroupidentifier.md)
  The identifier of the focus group that this view belongs to.
- [var focusEffect: UIFocusEffect?](./focuseffect.md)
  The visual effect to apply when the view becomes focused.
- [var focusGroupPriority: UIFocusGroupPriority](./focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/inheritedanimationduration)*