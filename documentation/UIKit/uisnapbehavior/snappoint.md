# snapPoint

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The point to which to snap.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var snapPoint: CGPoint { get set }
```

```objc
@property (nonatomic, assign) CGPoint snapPoint;
```

#### Discussion

The initial value of this property is the value you passed in to the [`init(item:snapTo:)`](./init%28item,snapto%29.md) method. Changing this value updates the dynamic item and potentially puts it in motion again.

The coordinate system of the point depends on how you initialized the underlying dynamic animator, as described in the overview of [`UIDynamicAnimator`](../uidynamicanimator.md).

## See Also

### Configuring a snap behavior
- [var damping: CGFloat](./damping.md)
  The amount of oscillation of a dynamic item during the conclusion of a snap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisnapbehavior/snappoint)*