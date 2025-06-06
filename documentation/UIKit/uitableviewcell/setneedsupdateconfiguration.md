# setNeedsUpdateConfiguration()

**Framework**: UIKit  
**Kind**: method

Informs the cell to update its configuration for its current state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setNeedsUpdateConfiguration()
```

#### Discussion

You call this method when you need the cell to update its configuration according to the current configuration state. The system calls this method automatically when the cell’s [`configurationState`](uitableviewcell/configurationstate-4xwj0.md) changes, as well as in other circumstances that may require an update. The system might combine multiple requests into a single update.

If you add custom states to the cell’s configuration state, make sure to call this method every time those custom states change.

## See Also

- [var configurationState: UICellConfigurationState](uitableviewcell/configurationstate-4xwj0.md)
  The current configuration state of the cell.
- [func updateConfiguration(using: UICellConfigurationState)](uitableviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](uitableviewcell/configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UITableViewCell.ConfigurationUpdateHandler](uitableviewcell/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the cell’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/setneedsupdateconfiguration())*