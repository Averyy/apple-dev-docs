# allowsFocusDuringEditing

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the table view allows its cells to become focused in edit mode.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsFocusDuringEditing: Bool { get set }
```

#### Discussion

If you implement [`tableView(_:canFocusRowAt:)`](uitableviewdelegate/tableview(_:canfocusrowat:).md), its return value takes precedence over the value of this property.

The system determines the default value of this property according to the platform and other properties of the table view.

## See Also

- [var allowsFocus: Bool](uitableview/allowsfocus.md)
  A Boolean value that determines whether the table view allows its cells to become focused.
- [var selectionFollowsFocus: Bool](uitableview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [var remembersLastFocusedIndexPath: Bool](uitableview/rememberslastfocusedindexpath.md)
  A Boolean value that indicates whether the table view automatically returns the focus to the cell at the last focused index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/allowsfocusduringediting)*