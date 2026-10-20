# movieType

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

The movie controller type.

#### Overview

The movieType field of the object sample atom structure specifies an object controller type, that is, the user interface to be used to manipulate the object.

QuickTime VR supports the following controller types:

```c
enum ObjectUITypes {
    kGrabberScrollerUI                          = 1,
    kOldJoyStickUI                              = 2,
    kJoystickUI                                 = 3,
    kGrabberUI                                  = 4,
    kAbsoluteUI                                 = 5
};
```

**Constant Descriptions**

- **`kGrabberScrollerUI`**: The default controller, which displays a hand for dragging and rotation arrows when the cursor is along the edges of the object window.
- **`kOldJoyStickUI`**: A joystick controller, which displays a joystick-like interface for spinning the object. With this controller, the direction of panning is reversed from the direction of the grabber.
- **`kJoystickUI`**: A joystick controller, which displays a joystick-like interface for spinning the object. With this controller, the direction of panning is consistent with the direction of the grabber.
- **`kGrabberUI`**: A grabber-only interface, which displays a hand for dragging but does not display rotation arrows when the cursor is along the edges of the object window.
- **`kAbsoluteUI`**: An absolute controller, which displays a finger for pointing. The absolute controller switches views based on a row-and-column grid mapped into the object window.

## See Also

### Data fields
- [majorVersion](./majorversion.md)
  The major version number of the file format.
- [minorVersion](./minorversion.md)
  The minor version number of the file format.
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
- [defaultTilt](./defaulttilt.md)
  The default tilt angle, in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/object_sample_atom/movietype)*