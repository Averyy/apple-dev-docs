# QuickTime image file format

**Framework**: QuickTime File Format

Store QuickTime-compressed still images.

#### Overview

> ❗ **Important**: The QuickTime Image File Format is deprecated in the QuickTime file format. The information that follows documents existing content containing QuickTime image file media and should not be used for new development.

This section describes QuickTime image files, which provide a useful container for QuickTime-compressed still images.

Most still image file formats define both how images should be stored and compressed. However, the QuickTime image file format is a container format, which describes a storage mechanism independent of compression. The QuickTime image file format uses the same atom-based structure as a QuickTime movie.

## Topics

### Storing image data
- [Atom types in QuickTime image files](atom_types_in_quicktime_image_files.md)
  Build QuickTime image files with atoms.
- [Recommended file type and suffix](recommended_file_type_and_suffix.md)
  Identify your image file with a file type and suffix.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/appendix_a_quicktime_image_file_format)*