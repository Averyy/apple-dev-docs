# controlSettings

**Framework**: QuickTime File Format  
**Kind**: property

A set of 32-bit flags that encode information about the control settings of the object.

#### Overview

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

## See Also

- [majorVersion](object_sample_atom/majorversion.md)
  The major version number of the file format.
- [minorVersion](object_sample_atom/minorversion.md)
  The minor version number of the file format.
- [movieType](object_sample_atom/movietype.md)
  The movie controller type.
- [viewStateCount](object_sample_atom/viewstatecount.md)
  The number of view states of the object.
- [defaultViewState](object_sample_atom/defaultviewstate.md)
  The 1-based index of the default view state.
- [mouseDownViewState](object_sample_atom/mousedownviewstate.md)
  The 1-based index of the mouse-down view state.
- [viewDuration](object_sample_atom/viewduration.md)
  The total movie duration of all image frames contained in an object’s view.
- [columns](object_sample_atom/columns.md)
  The number of columns in the object image array.
- [rows](object_sample_atom/rows.md)
  The number of rows in the object image array.
- [mouseMotionScale](object_sample_atom/mousemotionscale.md)
  The mouse motion scale factor.
- [minPan](object_sample_atom/minpan.md)
  The minimum pan angle, in degrees.
- [maxPan](object_sample_atom/maxpan.md)
  The maximum pan angle, in degrees.
- [defaultPan](object_sample_atom/defaultpan.md)
  The default pan angle, in degrees.
- [minTilt](object_sample_atom/mintilt.md)
  The minimum tilt angle, in degrees.
- [maxTilt](object_sample_atom/maxtilt.md)
  The maximum tilt angle, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/object_sample_atom/controlsettings)*