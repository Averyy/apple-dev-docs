# from

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key that identifies the view shown at the beginning of the transition, or at the end of a canceled transition.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static let from: UITransitionContextViewKey
```

```c
extern UITransitionContextViewKey const UITransitionContextFromViewKey;
```

#### Discussion

This view is typically the presenting view controller’s view.

## See Also

### Keys
- [static let to: UITransitionContextViewKey](./to.md)
  A key that identifies the view shown at the end of a completed transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitransitioncontextviewkey/from)*