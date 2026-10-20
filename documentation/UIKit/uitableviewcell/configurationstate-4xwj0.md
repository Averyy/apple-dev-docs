# configurationState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current configuration state of the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
@MainActor
@objc(_bridgedConfigurationState) @preconcurrency dynamic var configurationState: UICellConfigurationState { get }
```

#### Discussion

To add your own custom state, see [`UIConfigurationStateCustomKey`](../uiconfigurationstatecustomkey.md).

## See Also

### Managing the state
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](./updateconfiguration%28using%29.md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](./configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UITableViewCell.ConfigurationUpdateHandler](./configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the cell’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/configurationstate-4xwj0)*