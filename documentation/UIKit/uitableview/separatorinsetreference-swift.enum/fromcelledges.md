# UITableView.SeparatorInsetReference.fromCellEdges

**Framework**: UIKit  
**Kind**: case

An inset value that’s relative to the edge of the cell.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case fromCellEdges
```

#### Discussion

When this style is active, setting the left and right insets to `0.0` would result in a separator to extend from the entire distance between the left and right edges of the cell. Setting the insets to other values would inset the separator by the specified amount.

## See Also

- [UITableView.SeparatorInsetReference.fromAutomaticInsets](uitableview/separatorinsetreference-swift.enum/fromautomaticinsets.md)
  An inset value that indicates the starting position is based on the default separator insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/separatorinsetreference-swift.enum/fromcelledges)*