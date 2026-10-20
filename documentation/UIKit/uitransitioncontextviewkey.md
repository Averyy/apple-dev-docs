# UITransitionContextViewKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The keys you use to identify the views involved in a transition.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct UITransitionContextViewKey
```

```c
typedef NSString * UITransitionContextViewKey;
```

## Topics

### Keys
- [static let from: UITransitionContextViewKey](./uitransitioncontextviewkey/from.md)
  A key that identifies the view shown at the beginning of the transition, or at the end of a canceled transition.
- [static let to: UITransitionContextViewKey](./uitransitioncontextviewkey/to.md)
  A key that identifies the view shown at the end of a completed transition.
### Initializers
- [init(rawValue: String)](./uitransitioncontextviewkey/init%28rawvalue%29.md)
  Creates a key to identify the views in a transition.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct UITransitionContextViewControllerKey](./uitransitioncontextviewcontrollerkey.md)
  The keys you use to identify the view controllers involved in a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitransitioncontextviewkey)*