# setNeedsUpdateConfiguration()

**Framework**: UIKit  
**Kind**: method

Informs the view to update its configuration for its current state.

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

You call this method when you need the view to update its configuration according to the current configuration state. The system calls this method automatically when the view’s [`configurationState`](uitableviewheaderfooterview/configurationstate-7xj7r.md) changes, as well as in other circumstances that may require an update. The system might combine multiple requests into a single update.

If you add custom states to the view’s configuration state, make sure to call this method every time those custom states change.

## See Also

- [var configurationState: UIViewConfigurationState](uitableviewheaderfooterview/configurationstate-7xj7r.md)
  The current configuration state of the view.
- [func updateConfiguration(using: UIViewConfigurationState)](uitableviewheaderfooterview/updateconfiguration(using:).md)
  Updates the view’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](uitableviewheaderfooterview/configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.
- [UITableViewHeaderFooterView.ConfigurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the view’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/setneedsupdateconfiguration())*