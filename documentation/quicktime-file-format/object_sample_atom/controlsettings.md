# controlSettings

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A set of 32-bit flags that encode information about the control settings of the object.

## Overview

The `controlSettings` field of the object sample atom is a long integer that specifies a set of control settings for an object node. Control settings specify whether the object can wrap during panning and tilting, as well as other features of the node. The control settings are specified using these bit flags:

```c
enum QTVRControlSettings {
    kQTVRObjectWrapPanOn                        = (1 << 0),
    kQTVRObjectWrapTiltOn                       = (1 << 1),
    kQTVRObjectCanZoomOn                        = (1 << 2),
    kQTVRObjectReverseHControlOn                = (1 << 3),
    kQTVRObjectReverseVControlOn                = (1 << 4),
    kQTVRObjectSwapHVControlOn                  = (1 << 5),
    kQTVRObjectTranslationOn                    = (1 << 6)
};
```

**Constant Descriptions**

- **`kQTVRObjectWrapPanOn`**: The control setting to enable wrapping during panning. When this control setting is enabled, the user can wrap around from the current pan constraint maximum value to the pan constraint minimum value (or vice versa) using the mouse or arrow keys.
- **`kQTVRObjectWrapTiltOn`**: The control setting to enable wrapping during tilting. When this control setting is enabled, the user can wrap around from the current tilt constraint maximum value to the tilt constraint minimum value (or vice versa) using the mouse or arrow keys.
- **`kQTVRObjectCanZoomOn`**: The control setting to enable zooming. When this control setting is enabled, the user can change the current field of view using the zoom-in and zoom-out keys on the keyboard (or using the VR controller buttons).
- **`kQTVRObjectReverseHControlOn`**: The control setting to reverse the direction of the horizontal control.
- **`kQTVRObjectReverseVControlOn`**: The control setting to reverse the direction of the vertical control.
- **`kQTVRObjectSwapHVControlOn`**: The control setting to exchange the horizontal and vertical controls.
- **`kQTVRObjectTranslationOn`**: The control setting to enable translation. When this setting is enabled, the user can translate using the mouse when either the translate key is held down or the controller translation mode button is toggled on.

## See Also

### Data fields
- [majorVersion](./majorversion.md)
  The major version number of the file format.
- [minorVersion](./minorversion.md)
  The minor version number of the file format.
- [movieType](./movietype.md)
  The movie controller type.
- [viewStateCount](./viewstatecount.md)
  The number of view states of the object.
- [defaultViewState](./defaultviewstate.md)
  The 1-based index of the default view state.
- [mouseDownViewState](./mousedownviewstate.md)
  The 1-based index of the mouse-down view state.
- [viewDuration](./viewduration.md)
  The total movie duration of all image frames contained in an object’s view.
- [columns](./columns.md)
  The number of columns in the object image array.
- [rows](./rows.md)
  The number of rows in the object image array.
- [mouseMotionScale](./mousemotionscale.md)
  The mouse motion scale factor.
- [minPan](./minpan.md)
  The minimum pan angle, in degrees.
- [maxPan](./maxpan.md)
  The maximum pan angle, in degrees.
- [defaultPan](./defaultpan.md)
  The default pan angle, in degrees.
- [minTilt](./mintilt.md)
  The minimum tilt angle, in degrees.
- [maxTilt](./maxtilt.md)
  The maximum tilt angle, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/object_sample_atom/controlsettings)*