# UITransitionContextViewControllerKey

**Framework**: UIKit  
**Kind**: struct

The keys you use to identify the view controllers involved in a transition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct UITransitionContextViewControllerKey
```

## Topics

### Keys
- [static let from: UITransitionContextViewControllerKey](uitransitioncontextviewcontrollerkey/from.md)
  A key that identifies the view controller that’s visible at the beginning of the transition, or at the end of a canceled transition.
- [static let to: UITransitionContextViewControllerKey](uitransitioncontextviewcontrollerkey/to.md)
  A key that identifies the view controller that’s visible at the end of a completed transition.
### Initializers
- [init(rawValue: String)](uitransitioncontextviewcontrollerkey/init(rawvalue:).md)
  Creates a key to identify the view controllers in a transition.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct UITransitionContextViewKey](uitransitioncontextviewkey.md)
  The keys you use to identify the views involved in a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitransitioncontextviewcontrollerkey)*