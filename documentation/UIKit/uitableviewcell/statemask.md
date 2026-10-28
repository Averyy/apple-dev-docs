# UITableViewCell.StateMask

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants used to determine the new state of a cell as it transitions between states.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct StateMask
```

```c
enum UITableViewCellStateMask : NSUInteger;
```

## Overview

The methods that use these constants are [`didTransition(to:)`](./didtransition%28to%29.md) and [`willTransition(to:)`](./willtransition%28to%29.md).

## Topics

### Constants
- [static var showingEditControl: UITableViewCell.StateMask](./statemask/showingeditcontrol.md)
  The state of a table view cell when the table view is in editing mode.
- [static var showingDeleteConfirmation: UITableViewCell.StateMask](./statemask/showingdeleteconfirmation.md)
  The state of a table view cell that shows a button requesting confirmation of a delete gesture.
- [UITableViewCellStateDefaultMask](../uitableviewcellstatemask/uitableviewcellstatedefaultmask.md)
  The normal state of a table cell.
### Initializers
- [init(rawValue: UInt)](./statemask/init%28rawvalue%29.md)
  Creates a state mask with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Adjusting to state transitions
- [func willTransition(to: UITableViewCell.StateMask)](./willtransition%28to%29.md)
  Notifies the cell that it’s about to transition to a new cell state.
- [func didTransition(to: UITableViewCell.StateMask)](./didtransition%28to%29.md)
  Notifies the cell that it transitioned to a new cell state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/statemask)*