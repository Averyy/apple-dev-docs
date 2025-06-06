# damping

**Framework**: UIKit  
**Kind**: property

The amount of oscillation of a dynamic item during the conclusion of a snap.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var damping: CGFloat { get set }
```

#### Discussion

The valid range for damping extends from `0.0`, for maximum oscillation, through `1.0`, for minimum oscillation. The default value is `0.5`.

## See Also

- [var snapPoint: CGPoint](uisnapbehavior/snappoint.md)
  The point to which to snap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisnapbehavior/damping)*