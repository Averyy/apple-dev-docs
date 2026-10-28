# reserved2

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

Reserved.

## Overview

This field must be `0`.

> ❗ **Important**: A new flag has been added to the flags field of the `QTVRPanoSampleAtom` data structure. This flag controls how panoramas wrap horizontally. If `kQTVRPanoFlagAlwaysWrap` is set, then the panorama wraps horizontally, regardless of the number of degrees in the panorama. If the flag is not set, then the panorama wraps only when the panorama range is 360 degrees. This is the default behavior.

## See Also

### Data fields
- [majorVersion](./majorversion.md)
  The major version number of the file format.
- [minorVersion](./minorversion.md)
  The minor version number of the file format.
- [imageRefTrackIndex](./imagereftrackindex.md)
  The index of the image track reference.
- [hotSpotRefTrackIndex](./hotspotreftrackindex.md)
  The index of the hot spot track reference.
- [minPan](./minpan.md)
  The minimum pan angle, in degrees.
- [maxPan](./maxpan.md)
  The maximum pan angle, in degrees.
- [minTilt](./mintilt.md)
  The minimum tilt angle, in degrees.
- [maxTilt](./maxtilt.md)
  The maximum tilt angle, in degrees.
- [minFieldOfView](./minfieldofview.md)
  The minimum vertical field of view, in degrees.
- [maxFieldOfView](./maxfieldofview.md)
  The maximum vertical field of view, in degrees.
- [defaultPan](./defaultpan.md)
  The default pan angle, in degrees.
- [defaultTilt](./defaulttilt.md)
  The default tilt angle, in degrees.
- [defaultFieldOfView](./defaultfieldofview.md)
  The default vertical field of view, in degrees.
- [imageSizeX](./imagesizex.md)
  The width, in pixels, of the panorama stored in the highest resolution image track.
- [imageSizeY](./imagesizey.md)
  The height, in pixels, of the panorama stored in the highest resolution image track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/panorama_sample_atom/reserved2)*