# UITableViewHeaderFooterView.ConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias

The type of block for handling updates to the view’s configuration using the current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
typealias ConfigurationUpdateHandler = (UITableViewHeaderFooterView, UIViewConfigurationState) -> Void
```

## Parameters

- `headerFooterView`: The header footer view to configure.
- `state`: The new state to use for updating the header footer view’s configuration.

## See Also

- [var configurationState: UIViewConfigurationState](uitableviewheaderfooterview/configurationstate-7xj7r.md)
  The current configuration state of the view.
- [func setNeedsUpdateConfiguration()](uitableviewheaderfooterview/setneedsupdateconfiguration.md)
  Informs the view to update its configuration for its current state.
- [func updateConfiguration(using: UIViewConfigurationState)](uitableviewheaderfooterview/updateconfiguration(using:).md)
  Updates the view’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](uitableviewheaderfooterview/configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-swift.typealias)*