# updateConfiguration(using:)

**Framework**: UIKit  
**Kind**: method

Updates the cell’s configuration using the current state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc(_bridgedUpdateConfigurationUsingState:) @preconcurrency dynamic func updateConfiguration(using state: UICellConfigurationState)
```

#### Discussion

Avoid calling this method directly. Instead, use [`setNeedsUpdateConfiguration()`](uitableviewcell/setneedsupdateconfiguration().md) to request an update.

Override this method in a subclass to update the cell’s configuration using the provided state.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this cell’s `traitCollection`. For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

## See Also

- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](uitableviewcell/configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/updateconfiguration(using:))*