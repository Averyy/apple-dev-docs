# flags

**Framework**: QuickTime File Format  
**Kind**: property

A set of panorama flags.

#### Overview

`kQTVRPanoFlagHorizontal` has been superseded by the `panoType` field. It is used only when the `panoType` field is `nil` to indicate a horizontally-oriented cylindrical panorama. `kQTVRPanoFlagAlwaysWrap` is set if the panorama should wrap horizontally, regardless of whether or not the pan range is 360 degrees. Note that these flags are currently supported only under OS X.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/panorama_sample_atom/flags)*