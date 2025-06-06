# UITableViewCell.ConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias

The type of block for handling updates to the cell’s configuration using the current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
typealias ConfigurationUpdateHandler = (UITableViewCell, UICellConfigurationState) -> Void
```

## Parameters

- `cell`: The table view cell to configure.
- `state`: The new state to use for updating the cell’s configuration.

## See Also

- [var configurationState: UICellConfigurationState](uitableviewcell/configurationstate-4xwj0.md)
  The current configuration state of the cell.
- [func setNeedsUpdateConfiguration()](uitableviewcell/setneedsupdateconfiguration.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](uitableviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](uitableviewcell/configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/configurationupdatehandler-swift.typealias)*