# UITableViewCell.ConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The type of block for handling updates to the cell’s configuration using the current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
typealias ConfigurationUpdateHandler = (UITableViewCell, UICellConfigurationState) -> Void
```

## Parameters

- `cell`: The table view cell to configure.
- `state`: The new state to use for updating the cell’s configuration.

## See Also

### Managing the state
- [var configurationState: UICellConfigurationState](./configurationstate-4xwj0.md)
  The current configuration state of the cell.
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](./updateconfiguration%28using%29.md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](./configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/configurationupdatehandler-swift.typealias)*