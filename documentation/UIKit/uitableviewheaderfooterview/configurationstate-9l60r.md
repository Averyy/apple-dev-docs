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
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) UIViewConfigurationState * configurationState;
```

## Discussion

To add your own custom state, see [`UIConfigurationStateCustomKey`](../uiconfigurationstatecustomkey.md).

## See Also

### Managing the state
- [func setNeedsUpdateConfiguration()](./setneedsupdateconfiguration%28%29.md)
  Informs the view to update its configuration for its current state.
- [- updateConfigurationUsingState:](./updateconfigurationusingstate_.md)
  Updates the view’s configuration using the current state.
- [configurationUpdateHandler](./configurationupdatehandler-3oji2.md)
  A block for handling updates to the view’s configuration using the current state.
- [UITableViewHeaderFooterViewConfigurationUpdateHandler](../uitableviewheaderfooterviewconfigurationupdatehandler.md)
  The type of block for handling updates to the view’s configuration using the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationstate-9l60r)*