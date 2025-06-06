# animationSettings

**Framework**: QuickTime File Format  
**Kind**: property

A set of 32-bit flags that encode information about the animation settings of the object.

#### Overview

The `animationSettings` field of the object sample atom is a long integer that specifies a set of animation settings for an object node. Animation settings specify characteristics of the movie while it is playing. Use these constants to specify animation settings:

```c
enum QTVRAnimationSettings {
    kQTVRObjectAnimateViewFramesOn              = (1 << 0),
    kQTVRObjectPalindromeViewFramesOn           = (1 << 1),
    kQTVRObjectStartFirstViewFrameOn            = (1 << 2),
    kQTVRObjectAnimateViewsOn                   = (1 << 3),
    kQTVRObjectPalindromeViewsOn                = (1 << 4),
    kQTVRObjectSyncViewToFrameRate              = (1 << 5),
    kQTVRObjectDontLoopViewFramesOn             = (1 << 6),
    kQTVRObjectPlayEveryViewFrameOn             = (1 << 7)
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/object_sample_atom/animationsettings)*