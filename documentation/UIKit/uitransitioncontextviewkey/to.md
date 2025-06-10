# to

**Framework**: UIKit  
**Kind**: property

A key that identifies the view shown at the end of a completed transition.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let to: UITransitionContextViewKey
```

#### Discussion

This view is typically the presented view controller’s view but may also be an ancestor of that view.

## See Also

- [static let from: UITransitionContextViewKey](uitransitioncontextviewkey/from.md)
  A key that identifies the view shown at the beginning of the transition, or at the end of a canceled transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitransitioncontextviewkey/to)*