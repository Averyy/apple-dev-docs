# imageRefTrackIndex

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

The index of the image track reference.

#### Overview

This is the index returned by the `AddTrackReference` function when the image track is added as a reference to the panorama track. There can be more than one image track for a given panorama track and hence multiple references. (A panorama track might have multiple image tracks if the panoramas have different characteristics, which could occur if the panoramas were shot with different size camera lenses.) The value in this field is `0` if there is no corresponding image track.

## See Also

### Data fields
- [majorVersion](./majorversion.md)
  The major version number of the file format.
- [minorVersion](./minorversion.md)
  The minor version number of the file format.
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
- [imageNumFramesX](./imagenumframesx.md)
  The number of frames into which the panoramic image is diced horizontally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/panorama_sample_atom/imagereftrackindex)*