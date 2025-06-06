# configurationState

**Framework**: UIKit  
**Kind**: property

The current configuration state of the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc(_bridgedConfigurationState) @preconcurrency dynamic var configurationState: UICellConfigurationState { get }
```

#### Discussion

To add your own custom state, see [`UIConfigurationStateCustomKey`](uiconfigurationstatecustomkey.md).

## See Also

- [func setNeedsUpdateConfiguration()](uitableviewcell/setneedsupdateconfiguration.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](uitableviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](uitableviewcell/configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UITableViewCell.ConfigurationUpdateHandler](uitableviewcell/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the cell’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/configurationstate-4xwj0)*