# updateContentUnavailableConfigurationUsingState:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the content-unavailable configuration for the provided state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (void) updateContentUnavailableConfigurationUsingState:(UIContentUnavailableConfigurationState *) state;
```

#### Discussion

Override this method to update the value of [`contentUnavailableConfiguration`](./contentunavailableconfiguration-6kqfk.md) as appropriate for the given state.

Don’t call this method directly. Instead, call [`setNeedsUpdateContentUnavailableConfiguration()`](./setneedsupdatecontentunavailableconfiguration%28%29.md) to tell the system to request an update.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view controller’s `traitCollection` and the `traitCollection` of its [`view`](./view.md). For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## Parameters

- `state`: The current configuration state for a content-unavailable view.

## See Also

### Indicating missing content
- [contentUnavailableConfiguration](./contentunavailableconfiguration-6kqfk.md)
  Setting a content unavailable configuration replaces the existing content unavailable view of the view controller with a new content unavailable view instance from the configuration, or directly applies the configuration to the existing content unavailable view if the configuration is compatible with the existing content unavailable view type. The default value is nil.
- [contentUnavailableConfigurationState](./contentunavailableconfigurationstate-9bvga.md)
  Returns the current content unavailable configuration state for the view. To add your own custom state(s), override the getter and call super to obtain an instance with the system properties set, then set your own custom states as desired.
- [func setNeedsUpdateContentUnavailableConfiguration()](./setneedsupdatecontentunavailableconfiguration%28%29.md)
  Requests that the system update the content-unavailable configuration for the latest state.
- [UIContentUnavailableConfiguration](../uicontentunavailableconfiguration-c.class.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/updatecontentunavailableconfigurationusingstate:)*