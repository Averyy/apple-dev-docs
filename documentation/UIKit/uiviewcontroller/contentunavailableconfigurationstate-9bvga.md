# contentUnavailableConfigurationState

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the current content unavailable configuration state for the view. To add your own custom state(s), override the getter and call super to obtain an instance with the system properties set, then set your own custom states as desired.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) UIContentUnavailableConfigurationState * contentUnavailableConfigurationState;
```

## See Also

### Indicating missing content
- [contentUnavailableConfiguration](./contentunavailableconfiguration-6kqfk.md)
  Setting a content unavailable configuration replaces the existing content unavailable view of the view controller with a new content unavailable view instance from the configuration, or directly applies the configuration to the existing content unavailable view if the configuration is compatible with the existing content unavailable view type. The default value is nil.
- [func setNeedsUpdateContentUnavailableConfiguration()](./setneedsupdatecontentunavailableconfiguration%28%29.md)
  Requests that the system update the content-unavailable configuration for the latest state.
- [- updateContentUnavailableConfigurationUsingState:](./updatecontentunavailableconfigurationusingstate_.md)
  Updates the content-unavailable configuration for the provided state.
- [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-c.class.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/contentunavailableconfigurationstate-9bvga)*