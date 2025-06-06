# willTransition(to:)

**Framework**: UIKit  
**Kind**: method

Notifies the cell that it’s about to transition to a new cell state.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func willTransition(to state: UITableViewCell.StateMask)
```

#### Discussion

Subclasses of `UITableViewCell` can implement this method to animate additional changes to a cell when it is changing state. `UITableViewCell` calls this method whenever a cell transitions between states, such as from a normal state (the default) to editing mode. The custom cell can set up and position any new views that appear with the new state. The cell then receives a [`layoutSubviews()`](uiview/layoutsubviews().md) message (`UIView`) in which it can position these new views in their final locations for the new state. Subclasses must always call `super` when overriding this method.

Note that when the user swipes a cell to delete it, the cell transitions to the state identified by the [`showingDeleteConfirmation`](uitableviewcell/statemask/showingdeleteconfirmation.md) constant but the [`showingEditControl`](uitableviewcell/statemask/showingeditcontrol.md) is not set.

## Parameters

- `state`: A bit mask indicating the state or combination of states the cell is transitioning to.

## See Also

- [var editingAccessoryType: UITableViewCell.AccessoryType](uitableviewcell/editingaccessorytype.md)
  The type of standard accessory view for the cell to use in the table view’s editing state.
- [var editingAccessoryView: UIView?](uitableviewcell/editingaccessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
- [var accessoryView: UIView?](uitableviewcell/accessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [var accessoryType: UITableViewCell.AccessoryType](uitableviewcell/accessorytype-swift.property.md)
  The type of standard accessory view for the cell to use in the table view’s normal state.
- [func didTransition(to: UITableViewCell.StateMask)](uitableviewcell/didtransition(to:).md)
  Notifies the cell that it transitioned to a new cell state.
- [UITableViewCell.StateMask](uitableviewcell/statemask.md)
  Constants used to determine the new state of a cell as it transitions between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/willtransition(to:))*