# UITableView.SeparatorInsetReference.fromAutomaticInsets

**Framework**: UIKit  
**Kind**: case

An inset value that indicates the starting position is based on the default separator insets.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case fromAutomaticInsets
```

#### Discussion

When using this style, the values in the [`separatorInset`](uitableview/separatorinset.md) property are interpreted as offsets from the default insets provided by the table view. The table view normally uses its layout margins as the default cell inset value. However, these insets may be modified by other factors, such as the when the [`cellLayoutMarginsFollowReadableWidth`](uitableview/celllayoutmarginsfollowreadablewidth.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [UITableView.SeparatorInsetReference.fromCellEdges](uitableview/separatorinsetreference-swift.enum/fromcelledges.md)
  An inset value that’s relative to the edge of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/separatorinsetreference-swift.enum/fromautomaticinsets)*