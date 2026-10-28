# UITableView.SelfSizingInvalidation.enabledIncludingConstraints

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A mode that enables automatic self-sizing invalidation after Auto Layout changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case enabledIncludingConstraints
```

```c
UITableViewSelfSizingInvalidationEnabledIncludingConstraints
```

## Discussion

If you use this self-sizing invalidation mode, calling [`invalidateIntrinsicContentSize()`](../../uiview/invalidateintrinsiccontentsize%28%29.md) on a self-sizing cell or its [`contentView`](../../uitableviewcell/contentview.md) causes the cell to resize if necessary. Additionally, any Auto Layout change within the [`contentView`](../../uitableviewcell/contentview.md) of a self-sizing cell automatically calls [`invalidateIntrinsicContentSize()`](../../uiview/invalidateintrinsiccontentsize%28%29.md).

## See Also

### Constants
- [UITableView.SelfSizingInvalidation.disabled](./disabled.md)
  A mode that disables self-sizing invalidation.
- [UITableView.SelfSizingInvalidation.enabled](./enabled.md)
  A mode that enables manual self-sizing invalidation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/selfsizinginvalidation-swift.enum/enabledincludingconstraints)*