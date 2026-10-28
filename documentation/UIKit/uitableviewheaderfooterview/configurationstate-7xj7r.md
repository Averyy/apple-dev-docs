# configurationState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current configuration state of the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
@MainActor
@objc(_bridgedConfigurationState) @preconcurrency dynamic var configurationState: UIViewConfigurationState { get }
```

## Discussion

To add your own custom state, see [`UIConfigurationStateCustomKey`](../uiconfigurationstatecustomkey.md).

## See Also

### Managing the state
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Informs the view to update its configuration for its current state.
- [func updateConfiguration(using: UIViewConfigurationState)](./updateconfiguration%28using%29.md)
  Updates the view’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](./configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.
- [UITableViewHeaderFooterView.ConfigurationUpdateHandler](./configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the view’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationstate-7xj7r)*