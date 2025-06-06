# Panorama image track

**Framework**: QuickTime File Format

Store the panoramic image for a panoramic node.

#### Overview

The actual panoramic image for a panoramic node is contained in a panorama image track, which is a standard QuickTime video track. The track reference to this track is stored in the `imageRefTrackIndex` field of the panorama sample atom.

QuickTime VR 2.1 required the original panoramic image to be rotated 90 degrees counterclockwise. This orientation has changed in QuickTime VR 2.2, however, as discussed later in this section.

The rotated image is diced into smaller frames, and each diced frame is then compressed and added to the video track as a video sample. Frames can be compressed using any spatial compressor; however, temporal compression is not allowed for panoramic image tracks.

QuickTime VR 2.2 does not require the original panoramic image to be rotated 90 degrees counterclockwise, as was the case in QuickTime VR 2.1. The rotated image is still diced into smaller frames, and each diced frame is then compressed and added to the video track as a video sample.

In QuickTime 3.0, a panorama sample atom (which contains information about a single panorama) contains the `panoType` field, which indicates whether the diced panoramic image is oriented horizontally or vertically.

## See Also

- [Panorama sample atom ('pdat')](panorama_sample_atom.md)
  An atom that describes a single panorama.
- [Cylindrical panoramas](cylindrical_panoramas.md)
  Store cylindrical panoramas with horizontal orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/panorama_image_track)*