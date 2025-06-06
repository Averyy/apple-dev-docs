# snapPoint

**Framework**: UIKit  
**Kind**: property

The point to which to snap.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var snapPoint: CGPoint { get set }
```

#### Discussion

The initial value of this property is the value you passed in to the [`init(item:snapTo:)`](uisnapbehavior/init(item:snapto:).md) method. Changing this value updates the dynamic item and potentially puts it in motion again.

The coordinate system of the point depends on how you initialized the underlying dynamic animator, as described in the overview of [`UIDynamicAnimator`](uidynamicanimator.md).

## See Also

- [var damping: CGFloat](uisnapbehavior/damping.md)
  The amount of oscillation of a dynamic item during the conclusion of a snap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisnapbehavior/snappoint)*