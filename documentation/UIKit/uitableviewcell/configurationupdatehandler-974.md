# configurationUpdateHandler

**Framework**: UIKit  
**Kind**: property

A block for handling updates to the cell’s configuration using the current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler? { get set }
```

#### Discussion

A configuration update handler provides an alternative approach to overriding [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md) in a subclass. Set a configuration update handler to update the cell’s configuration using the new state in response to a configuration state change:

```swift
cell.configurationUpdateHandler = { cell, state in
    var content = cell.defaultContentConfiguration().updated(for: state)
    content.text = "Hello world!"
    if state.isDisabled {
        content.textProperties.color = .systemGray
    }
    cell.contentConfiguration = content
}
```

Setting the value of this property calls [`setNeedsUpdateConfiguration()`](uicollectionviewcell/setneedsupdateconfiguration().md). The system calls this handler after calling [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md).

In iOS 18 and later, UIKit supports automatic trait tracking inside this closure for traits from this cell’s `traitCollection`. For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

This closure supports automatic observation tracking. For more information, see [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

## See Also

- [func updateConfiguration(using: UICellConfigurationState)](uitableviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/configurationupdatehandler-974)*