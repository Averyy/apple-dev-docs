# setNeedsUpdateContentUnavailableConfiguration()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Requests that the system update the content-unavailable configuration for the latest state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func setNeedsUpdateContentUnavailableConfiguration()
```

```objc
- (void) setNeedsUpdateContentUnavailableConfiguration;
```

## See Also

### Indicating missing content
- [var contentUnavailableConfiguration: (any UIContentConfiguration)?](./contentunavailableconfiguration-4b95e.md)
  The current content-unavailable configuration of the view controller.
- [var contentUnavailableConfigurationState: UIContentUnavailableConfigurationState](./contentunavailableconfigurationstate-7sczw.md)
  The current configuration state of the content-unavailable view.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](./updatecontentunavailableconfiguration%28using%29.md)
  Updates the content-unavailable configuration for the provided state.
- [struct UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.
- [contentUnavailableConfiguration](./contentunavailableconfiguration-6kqfk.md)
  Setting a content unavailable configuration replaces the existing content unavailable view of the view controller with a new content unavailable view instance from the configuration, or directly applies the configuration to the existing content unavailable view if the configuration is compatible with the existing content unavailable view type. The default value is nil.
- [contentUnavailableConfigurationState](./contentunavailableconfigurationstate-9bvga.md)
  Returns the current content unavailable configuration state for the view. To add your own custom state(s), override the getter and call super to obtain an instance with the system properties set, then set your own custom states as desired.
- [- updateContentUnavailableConfigurationUsingState:](./updatecontentunavailableconfigurationusingstate_.md)
  Updates the content-unavailable configuration for the provided state.
- [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-c.class.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdatecontentunavailableconfiguration())*