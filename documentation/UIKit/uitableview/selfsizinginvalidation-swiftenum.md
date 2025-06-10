# UITableView.SelfSizingInvalidation

**Framework**: UIKit  
**Kind**: enum

Constants that describe modes for invalidating the size of self-sizing table view cells.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum SelfSizingInvalidation
```

#### Overview

Use these constants with the [`selfSizingInvalidation`](uitableview/selfsizinginvalidation-swift.property.md) property.

## Topics

### Constants
- [UITableView.SelfSizingInvalidation.disabled](uitableview/selfsizinginvalidation-swift.enum/disabled.md)
  A mode that disables self-sizing invalidation.
- [UITableView.SelfSizingInvalidation.enabled](uitableview/selfsizinginvalidation-swift.enum/enabled.md)
  A mode that enables manual self-sizing invalidation.
- [UITableView.SelfSizingInvalidation.enabledIncludingConstraints](uitableview/selfsizinginvalidation-swift.enum/enabledincludingconstraints.md)
  A mode that enables automatic self-sizing invalidation after Auto Layout changes.
### Initializers
- [init?(rawValue: Int)](uitableview/selfsizinginvalidation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var selfSizingInvalidation: UITableView.SelfSizingInvalidation](uitableview/selfsizinginvalidation-swift.property.md)
  The mode that the table view uses for invalidating the size of self-sizing cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/selfsizinginvalidation-swift.enum)*