# FxParameterFlags

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

These constants specify the characteristics of parameters display.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
typealias FxParameterFlags = UInt32
```

```c
typedef UInt32 FxParameterFlags;
```

#### Discussion

Not all of the flags are meaningfully to all of the parameter types. The only flags, for example, that apply to group parameters are [`kFxParameterFlag_COLLAPSED`](./kfxparameterflag_collapsed.md), [`kFxParameterFlag_DONT_DISPLAY_IN_DASHBOARD`](./kfxparameterflag_dont_display_in_dashboard.md), [`kFxParameterFlag_HIDDEN`](./kfxparameterflag_hidden.md), and [`kFxParameterFlag_DISABLED`](./kfxparameterflag_disabled.md).

You are unable to give a group parameter a custom user interface.

## Topics

### Constants
- [var kFxParameterFlag_DEFAULT: Int](./kfxparameterflag_default.md)
  Convenience constant. No flags set.
- [var kFxParameterFlag_NOT_ANIMATABLE: Int](./kfxparameterflag_not_animatable.md)
  This parameter’s value is constant across time and cannot be animated.
- [var kFxParameterFlag_HIDDEN: Int](./kfxparameterflag_hidden.md)
  This parameter displays no UI to the user, but its value is saved/loaded.
- [var kFxParameterFlag_DISABLED: Int](./kfxparameterflag_disabled.md)
  This parameter is dimmed and disabled.
- [var kFxParameterFlag_COLLAPSED: Int](./kfxparameterflag_collapsed.md)
  This group parameter’s subgroup is closed and its sub-parameters are not visible in the Inspector.
- [var kFxParameterFlag_DONT_SAVE: Int](./kfxparameterflag_dont_save.md)
  This parameter’s values are not saved or loaded.
- [var kFxParameterFlag_DONT_DISPLAY_IN_DASHBOARD: Int](./kfxparameterflag_dont_display_in_dashboard.md)
  This parameter is not visible in the dashboard controls.
- [var kFxParameterFlag_CUSTOM_UI: Int](./kfxparameterflag_custom_ui.md)
  This parameter uses a custom user interface that replaces the standard parameter UI.
- [var kFxParameterFlag_IGNORE_MINMAX: Int](./kfxparameterflag_ignore_minmax.md)
  This parameter’s range is unbounded.

## See Also

### Constants
- [typealias FxHistogramChannel](./fxhistogramchannel.md)
  Constants used to identify which channel a histogram operation should apply to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparameterflags)*