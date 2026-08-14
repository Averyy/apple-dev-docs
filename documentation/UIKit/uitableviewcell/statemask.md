# UITableViewCell.StateMask

**Framework**: UIKit  
**Kind**: struct

Constants used to determine the new state of a cell as it transitions between states.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct StateMask
```

#### Overview

The methods that use these constants are [`didTransition(to:)`](uitableviewcell/didtransition(to:).md) and [`willTransition(to:)`](uitableviewcell/willtransition(to:).md).

## Topics

### Constants
- [static var showingEditControl: UITableViewCell.StateMask](uitableviewcell/statemask/showingeditcontrol.md)
  The state of a table view cell when the table view is in editing mode.
- [static var showingDeleteConfirmation: UITableViewCell.StateMask](uitableviewcell/statemask/showingdeleteconfirmation.md)
  The state of a table view cell that shows a button requesting confirmation of a delete gesture.
### Initializers
- [init(rawValue: UInt)](uitableviewcell/statemask/init(rawvalue:).md)
  Creates a state mask with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func willTransition(to: UITableViewCell.StateMask)](uitableviewcell/willtransition(to:).md)
  Notifies the cell that it’s about to transition to a new cell state.
- [func didTransition(to: UITableViewCell.StateMask)](uitableviewcell/didtransition(to:).md)
  Notifies the cell that it transitioned to a new cell state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/statemask)*