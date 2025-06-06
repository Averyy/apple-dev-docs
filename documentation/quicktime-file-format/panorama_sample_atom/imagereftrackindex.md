# imageRefTrackIndex

**Framework**: QuickTime File Format  
**Kind**: property

The index of the image track reference.

#### Overview

This is the index returned by the `AddTrackReference` function when the image track is added as a reference to the panorama track. There can be more than one image track for a given panorama track and hence multiple references. (A panorama track might have multiple image tracks if the panoramas have different characteristics, which could occur if the panoramas were shot with different size camera lenses.) The value in this field is `0` if there is no corresponding image track.

## See Also

- [majorVersion](panorama_sample_atom/majorversion.md)
  The major version number of the file format.
- [minorVersion](panorama_sample_atom/minorversion.md)
  The minor version number of the file format.
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
- [imageNumFramesX](panorama_sample_atom/imagenumframesx.md)
  The number of frames into which the panoramic image is diced horizontally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/panorama_sample_atom/imagereftrackindex)*