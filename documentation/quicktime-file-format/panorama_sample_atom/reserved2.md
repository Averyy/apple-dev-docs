# reserved2

**Framework**: QuickTime File Format  
**Kind**: property

Reserved.

#### Overview

This field must be `0`.

> ❗ **Important**: A new flag has been added to the flags field of the `QTVRPanoSampleAtom` data structure. This flag controls how panoramas wrap horizontally. If `kQTVRPanoFlagAlwaysWrap` is set, then the panorama wraps horizontally, regardless of the number of degrees in the panorama. If the flag is not set, then the panorama wraps only when the panorama range is 360 degrees. This is the default behavior.

A new flag has been added to the flags field of the `QTVRPanoSampleAtom` data structure. This flag controls how panoramas wrap horizontally. If `kQTVRPanoFlagAlwaysWrap` is set, then the panorama wraps horizontally, regardless of the number of degrees in the panorama. If the flag is not set, then the panorama wraps only when the panorama range is 360 degrees. This is the default behavior.

## See Also

- [majorVersion](panorama_sample_atom/majorversion.md)
  The major version number of the file format.
- [minorVersion](panorama_sample_atom/minorversion.md)
  The minor version number of the file format.
- [imageRefTrackIndex](panorama_sample_atom/imagereftrackindex.md)
  The index of the image track reference.
- [hotSpotRefTrackIndex](panorama_sample_atom/hotspotreftrackindex.md)
  The index of the hot spot track reference.
- [minPan](panorama_sample_atom/minpan.md)
  The minimum pan angle, in degrees.
- [maxPan](panorama_sample_atom/maxpan.md)
  The maximum pan angle, in degrees.
- [minTilt](panorama_sample_atom/mintilt.md)
  The minimum tilt angle, in degrees.
- [maxTilt](panorama_sample_atom/maxtilt.md)
  The maximum tilt angle, in degrees.
- [minFieldOfView](panorama_sample_atom/minfieldofview.md)
  The minimum vertical field of view, in degrees.
- [maxFieldOfView](panorama_sample_atom/maxfieldofview.md)
  The maximum vertical field of view, in degrees.
- [defaultPan](panorama_sample_atom/defaultpan.md)
  The default pan angle, in degrees.
- [defaultTilt](panorama_sample_atom/defaulttilt.md)
  The default tilt angle, in degrees.
- [defaultFieldOfView](panorama_sample_atom/defaultfieldofview.md)
  The default vertical field of view, in degrees.
- [imageSizeX](panorama_sample_atom/imagesizex.md)
  The width, in pixels, of the panorama stored in the highest resolution image track.
- [imageSizeY](panorama_sample_atom/imagesizey.md)
  The height, in pixels, of the panorama stored in the highest resolution image track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/panorama_sample_atom/reserved2)*