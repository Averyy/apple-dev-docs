# Hot spot image tracks

**Framework**: QuickTime File Format

Identify hot spots in a panorama with a hot spot image track.

#### Overview

> ❗ **Important**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

When a panorama contains hot spots, the movie file contains a hot spot image track, a video track that contains a parallel panorama, with the hot spots designated by regions filled with color. Each diced frame of the hot spot panoramic image must be compressed with a lossless compressor (such as QuickTime’s graphics compressor). The dimensions of the hot spot panoramic image are usually the same as those of the image track’s panoramic image, but this is not required. The dimensions must, however, have the same aspect ratio as the image track’s panoramic image. A hot spot image track should be 8 bits deep.

## Topics

### Hot spot image tracks
- [Low-resolution image tracks](low-resolution_image_tracks.md)
  Create low resolution image tracks for low memory conditions.
- [Track reference entry structure](track_reference_entry_structure.md)
  A data structure you use to specify information about any low-resolution image tracks contained in a movie.

## See Also

- [Sprite media](sprite_media.md)
  Sprite media is used to store character-based animation data in QuickTime movies.
- [Sprite track properties](sprite_track_properties.md)
  Define properties that apply to an entire sprite track.
- [Sprite track media format](sprite_track_media_format.md)
  A media format for that stores sprite track information in atoms.
- [Sprite media atom and data types](sprite_media_atom_and_data_types.md)
  Atoms that represent sprite media and data types.
- [Sprite button behaviors](sprite_button_behaviors.md)
  Specify simple button behaviors for sprites in a sprite track.
- [QT atom container description key](qt_atom_container_description_key.md)
  Build QT atom container-based data structures.
- [Sprite media handler track properties QT atom container format](sprite_media_handler_track_properties_qt_atom_container_format.md)
  Set sprite media handler track properties in a QT atom container.
- [Sprite media handler sample QT atom container formats](sprite_media_handler_sample_qt_atom_container_formats.md)
  Set sprite media handlers in QT atom containers.
- [Wired action grammar](wired_action_grammar.md)
  Embed QT event handlers in their media samples.
- [Tween media](tween_media.md)
  Store pairs of values to be interpolated between in QuickTime movies using tween media.
- [3D media](3d_media.md)
  Store 3D image data in a base media in QuickTime movies.
- [VR media](vr_media.md)
  Atoms that describe the QuickTime VR world.
- [Node parent atom](node_parent_atom.md)
  An atom that is the parent of one or more node ID atoms.
- [Node location atom structure ('nloc')](node_location_atom_structure.md)
  An atom that describes the type of a node and its location.
- [Custom cursor atom](custom_cursor_atom.md)
  An atom you use to replace the default cursors used by QuickTime VR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hot_spot_image_tracks)*