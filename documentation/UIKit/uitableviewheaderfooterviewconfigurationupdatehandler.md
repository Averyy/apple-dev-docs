# UITableViewHeaderFooterViewConfigurationUpdateHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The type of block for handling updates to the view’s configuration using the current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```c
typedef void (^)(__kindof UITableViewHeaderFooterView *, UIViewConfigurationState *) UITableViewHeaderFooterViewConfigurationUpdateHandler;
```

## Parameters

- `cell`: The header footer view to configure.
- `state`: The new state to use for updating the header footer view’s configuration.

## See Also

### Managing the state
- [configurationState](./uitableviewheaderfooterview/configurationstate-9l60r.md)
  The current configuration state of the view.
- [func setNeedsUpdateConfiguration()](./uitableviewheaderfooterview/setneedsupdateconfiguration%28%29.md)
  Informs the view to update its configuration for its current state.
- [- updateConfigurationUsingState:](./uitableviewheaderfooterview/updateconfigurationusingstate_.md)
  Updates the view’s configuration using the current state.
- [configurationUpdateHandler](./uitableviewheaderfooterview/configurationupdatehandler-3oji2.md)
  A block for handling updates to the view’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterviewconfigurationupdatehandler)*