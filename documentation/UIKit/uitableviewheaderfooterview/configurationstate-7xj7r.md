# configurationState

**Framework**: UIKit  
**Kind**: property

The current configuration state of the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc(_bridgedConfigurationState) @preconcurrency dynamic var configurationState: UIViewConfigurationState { get }
```

#### Discussion

To add your own custom state, see [`UIConfigurationStateCustomKey`](uiconfigurationstatecustomkey.md).

## See Also

- [func setNeedsUpdateConfiguration()](uitableviewheaderfooterview/setneedsupdateconfiguration.md)
  Informs the view to update its configuration for its current state.
- [func updateConfiguration(using: UIViewConfigurationState)](uitableviewheaderfooterview/updateconfiguration(using:).md)
  Updates the view’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](uitableviewheaderfooterview/configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.
- [UITableViewHeaderFooterView.ConfigurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the view’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationstate-7xj7r)*