# to

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key that identifies the view controller that’s visible at the end of a completed transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static let to: UITransitionContextViewControllerKey
```

```c
extern UITransitionContextViewControllerKey const UITransitionContextToViewControllerKey;
```

## Discussion

This view controller is the one being presented.

## See Also

### Keys
- [static let from: UITransitionContextViewControllerKey](./from.md)
  A key that identifies the view controller that’s visible at the beginning of the transition, or at the end of a canceled transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitransitioncontextviewcontrollerkey/to)*