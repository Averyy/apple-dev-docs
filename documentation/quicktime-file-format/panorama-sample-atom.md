# Panorama sample atom ('pdat')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that describes a single panorama.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

A panorama sample atom has an atom type of `kQTVRPanoSampleDataAtomType` (`'pdat'`). It describes a single panorama, including track reference indexes of the scene and hot spot tracks and information about the default viewing angles and the source panoramic image.

The structure of a panorama sample atom is defined by the `QTVRPanoSampleAtom` data type:

```c
typedef struct VRPanoSampleAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              imageRefTrackIndex;
    UInt32                              hotSpotRefTrackIndex;
    Float32                             minPan;
    Float32                             maxPan;
    Float32                             minTilt;
    Float32                             maxTilt;
    Float32                             minFieldOfView;
    Float32                             maxFieldOfView;
    Float32                             defaultPan;
    Float32                             defaultTilt;
    Float32                             defaultFieldOfView;
    UInt32                              imageSizeX;
    UInt32                              imageSizeY;
    UInt16                              imageNumFramesX;
    UInt16                              imageNumFramesY;
    UInt32                              hotSpotSizeX;
    UInt32                              hotSpotSizeY;
    UInt16                              hotSpotNumFramesX;
    UInt16                              hotSpotNumFramesY;
    UInt32                              flags;
    OSType                              panoType;
    UInt32                              reserved2;
} VRPanoSampleAtom, *VRPanoSampleAtomPtr;
```

The minimum and maximum values in the panorama sample atom describe the physical limits of the panoramic image. QuickTime VR allows you to set further constraints on what portion of the image a user can see by calling the `QTVRSetConstraints` routine. You can also preset image constraints by adding constraint atoms to the panorama sample atom container. The three constraint atom types are `kQTVRPanConstraintAtomType`, `kQTVRTiltConstraintAtomType`, and `kQTVRFOVConstraintAtomType`. Each of these atom types share a common structure defined by the `QTVRAngleRangeAtom` data type:

```c
typedef struct QTVRAngleRangeAtom {
    Float32                             minimumAngle;
    Float32                             maximumAngle;
} QTVRAngleRangeAtom, *QTVRAngleRangeAtomPtr;
```

## Topics

### Data fields
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
- [imageNumFramesX](panorama_sample_atom/imagenumframesx.md)
  The number of frames into which the panoramic image is diced horizontally.
- [imageNumFramesY](panorama_sample_atom/imagenumframesy.md)
  The number of frames into which the panoramic image is diced vertically.
- [hotSpotSizeX](panorama_sample_atom/hotspotsizex.md)
  The width, in pixels, of the panorama stored in the highest resolution hot spot image track.
- [hotSpotSizeY](panorama_sample_atom/hotspotsizey.md)
  The height, in pixels, of the panorama stored in the highest resolution hot spot image track.
- [hotSpotNumFramesX](panorama_sample_atom/hotspotnumframesx.md)
  The number of frames into which the panoramic image is diced horizontally for the hot spot image track.
- [hotSpotNumFramesY](panorama_sample_atom/hotspotnumframesy.md)
  The number of frames into which the panoramic image is diced vertically for the hot spot image track.
- [flags](panorama_sample_atom/flags.md)
  A set of panorama flags.
- [panoType](panorama_sample_atom/panotype.md)
  An OSType describing the type of panorama.
- [reserved2](panorama_sample_atom/reserved2.md)
  Reserved.

## See Also

- [Panorama image track](panorama_image_track.md)
  Store the panoramic image for a panoramic node.
- [Cylindrical panoramas](cylindrical_panoramas.md)
  Store cylindrical panoramas with horizontal orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/panorama_sample_atom)*