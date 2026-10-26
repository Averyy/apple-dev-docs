# kFxParameterFlag_USE_FULL_VIEW_WIDTH

**Framework**: Professional Video Applications  
**Kind**: var  
**Role**: Global Variable

This parameter uses the full width of the view.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
var kFxParameterFlag_USE_FULL_VIEW_WIDTH: Int { get }
```

```c
kFxParameterFlag_USE_FULL_VIEW_WIDTH
```

#### Discussion

This flag is only valid for parameters that also set [`kFxParameterFlag_CUSTOM_UI`](./kfxparameterflag_custom_ui.md). Of course, not all of the flags apply meaningfully to all of the parameter types. The only flags, for example, that apply to Group parameters are [`kFxParameterFlag_COLLAPSED`](./kfxparameterflag_collapsed.md), [`kFxParameterFlag_DONT_DISPLAY_IN_DASHBOARD`](./kfxparameterflag_dont_display_in_dashboard.md), `HIDDEN`, and `DISABLED`. You can’t give a group parameter a custom UI.

## See Also

### Constants
- [var kFxParameterFlag_COLLAPSED: Int](./kfxparameterflag_collapsed.md)
  This group parameter’s subgroup is closed and its sub-parameters are not visible in the Inspector.
- [var kFxParameterFlag_CURVE_EDITOR_HIDDEN: Int](./kfxparameterflag_curve_editor_hidden.md)
- [var kFxParameterFlag_CUSTOM_UI: Int](./kfxparameterflag_custom_ui.md)
  This parameter uses a custom user interface that replaces the standard parameter UI.
- [var kFxParameterFlag_DEFAULT: Int](./kfxparameterflag_default.md)
  Convenience constant. No flags set.
- [var kFxParameterFlag_DISABLED: Int](./kfxparameterflag_disabled.md)
  This parameter is dimmed and disabled.
- [var kFxParameterFlag_DONT_DISPLAY_IN_DASHBOARD: Int](./kfxparameterflag_dont_display_in_dashboard.md)
  This parameter is not visible in the dashboard controls.
- [var kFxParameterFlag_DONT_SAVE: Int](./kfxparameterflag_dont_save.md)
  This parameter’s values are not saved or loaded.
- [var kFxParameterFlag_HIDDEN: Int](./kfxparameterflag_hidden.md)
  This parameter displays no UI to the user, but its value is saved/loaded.
- [var kFxParameterFlag_IGNORE_MINMAX: Int](./kfxparameterflag_ignore_minmax.md)
  This parameter’s range is unbounded.
- [var kFxParameterFlag_NOT_ANIMATABLE: Int](./kfxparameterflag_not_animatable.md)
  This parameter’s value is constant across time and cannot be animated.
- [var kFxParameterFlag_DONT_REMAP_COLORS: Int](./kfxparameterflag_dont_remap_colors.md)
  Indicates that the host must not remap colors to sRGB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxparameterflag_use_full_view_width)*