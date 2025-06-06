# Object sample atom

**Framework**: QuickTime File Format  
**Kind**: class

An atom that describes a single object.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

An object sample atom describes a single object, including information about the default viewing angles and the view settings. The structure of an object sample atom is defined by the `QTVRObjectSampleAtom` data type:

```c
typedef struct VRObjectSampleAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt16                              movieType;
    UInt16                              viewStateCount;
    UInt16                              defaultViewState;
    UInt16                              mouseDownViewState;
    UInt32                              viewDuration;
    UInt32                              columns;
    UInt32                              rows;
    Float32                             mouseMotionScale;
    Float32                             minPan;
    Float32                             maxPan;
    Float32                             defaultPan;
    Float32                             minTilt;
    Float32                             maxTilt;
    Float32                             defaultTilt;
    Float32                             minFieldOfView;
    Float32                             fieldOfView;
    Float32                             defaultFieldOfView;
    Float32                             defaultViewCenterH;
    Float32                             defaultViewCenterV;
    Float32                             viewRate;
    Float32                             frameRate;
    UInt32                              animationSettings;
    UInt32                              controlSettings;
} VRObjectSampleAtom, *VRObjectSampleAtomPtr;
QT
QT
QT
```

## Topics

### Data fields
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
- [defaultTilt](object_sample_atom/defaulttilt.md)
  The default tilt angle, in degrees.
- [minFieldOfView](object_sample_atom/minfieldofview.md)
  The minimum field of view to which the object can zoom.
- [fieldOfView](object_sample_atom/fieldofview.md)
  The image field of view, in degrees, for the entire object.
- [defaultFieldOfView](object_sample_atom/defaultfieldofview.md)
  The default field of view for the object.
- [defaultViewCenterH](object_sample_atom/defaultviewcenterh.md)
  The default horizontal view center.
- [defaultViewCenterV](object_sample_atom/defaultviewcenterv.md)
  The default vertical view center.
- [viewRate](object_sample_atom/viewrate.md)
  The view rate.
- [frameRate](object_sample_atom/framerate.md)
  The frame rate.
- [animationSettings](object_sample_atom/animationsettings.md)
  A set of 32-bit flags that encode information about the animation settings of the object.
- [controlSettings](object_sample_atom/controlsettings.md)
  A set of 32-bit flags that encode information about the control settings of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/object_sample_atom)*