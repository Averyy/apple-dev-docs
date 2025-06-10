# from

**Framework**: UIKit  
**Kind**: property

A key that identifies the view controller that’s visible at the beginning of the transition, or at the end of a canceled transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let from: UITransitionContextViewControllerKey
```

#### Discussion

This view controller is typically the one presenting the “to” view controller or is the one being replaced by the “to” view controller.

## See Also

- [static let to: UITransitionContextViewControllerKey](uitransitioncontextviewcontrollerkey/to.md)
  A key that identifies the view controller that’s visible at the end of a completed transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitransitioncontextviewcontrollerkey/from)*