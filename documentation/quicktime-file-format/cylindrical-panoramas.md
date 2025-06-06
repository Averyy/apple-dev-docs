# Cylindrical panoramas

**Framework**: QuickTime File Format

Store cylindrical panoramas with horizontal orientation.

#### Overview

The primary change to cylindrical panoramas in QuickTime VR 2.2 is that the panorama, as stored in the image track of the movie, can be oriented horizontally. This means that the panorama does not need to be rotated 90 degrees counterclockwise, as required previously.

To indicate a horizontal orientation, the field in the `VRPanoSampleAtom` data structure formerly called `reserved1` has been renamed `panoType`. Its type is `OSType`. The `panoType` field value for a horizontally oriented cylinder is `kQTVRHorizontalCylinder` (`'hcyl'`), while a vertical cylinder is `kQTVRVerticalCylinder` (`'vcyl'`). For compatibility with older QuickTime VR files, when the `panoType` field is `nil`, then a cylinder is assumed, with the low order bit of the flags field set to 1 to indicate if the cylinder is horizontal and 0 if the cylinder is vertical.

One consequence of reorienting the panorama horizontally is that, when the panorama is divided into separate tiles, the order of the samples in the file is now the reverse of what it was for vertical cylinders. Since vertical cylinders were rotated 90 degrees counterclockwise, the first tile added to the image track was the rightmost tile in the panorama. For unrotated horizontal cylinders, the first tile added to the image track is the left-most tile in the panorama.

## See Also

- [Panorama sample atom ('pdat')](panorama_sample_atom.md)
  An atom that describes a single panorama.
- [Panorama image track](panorama_image_track.md)
  Store the panoramic image for a panoramic node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/cylindrical_panoramas)*