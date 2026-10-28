# focusGroupIdentifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The identifier of the focus group that this view belongs to.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var focusGroupIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * focusGroupIdentifier;
```

## Discussion

If this property is `nil`, subviews inherit their superview’s focus group.

## See Also

### Working with focus
- [var canBecomeFocused: Bool](./canbecomefocused.md)
  A Boolean value that indicates whether the view is currently capable of being focused.
- [class var inheritedAnimationDuration: TimeInterval](./inheritedanimationduration.md)
  Returns the inherited duration of the current animation.
- [var isFocused: Bool](./isfocused.md)
  A Boolean value that indicates whether the item is currently focused.
- [var focusEffect: UIFocusEffect?](./focuseffect.md)
  The visual effect to apply when the view becomes focused.
- [var focusGroupPriority: UIFocusGroupPriority](./focusgrouppriority.md)
  The importance of the item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/focusgroupidentifier)*