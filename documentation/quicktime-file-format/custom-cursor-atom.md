# Custom cursor atom

**Framework**: QuickTime File Format

An atom you use to replace the default cursors used by QuickTime VR.

#### Overview

> ❗ **Important**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

The hot spot information atom, discussed in [`Hot spot information atom ('hsin')`](hot_spot_information_atom.md), allows you to indicate custom cursor IDs for particular hot spots that replace the default cursors used by QuickTime VR. QuickTime VR allows you to store your custom cursors in the VR world of the movie file.

> **Note**: The use of resource forks for the storage of QuickTime media is deprecated in the QuickTime file format. The information that follows documents existing content and should not be used for new development. In Mac OS with a two-fork file system, custom cursors could be stored in the resource fork of the movie file. However, this implementation does not work on any other operating system platform (such as Windows).

The cursor parent atom is the parent of all of the custom cursor atoms stored in the VR world. Its atom type is `kQTVRCursorParentAtomType` (`'vrcp'`). The child atoms of the cursor parent are either cursor atoms or color cursor atoms. Their atom types are `kQTVRCursorAtomType` (`'CURS'`) and `kQTVRColorCursorAtomType` (`'crsr'`). These atoms are stored exactly as cursors or color cursors would be stored as a resource.

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
- [Node information atom container](node_information_atom_container.md)
  An atom container that includes general information about the node such as the node’s type, ID, and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/custom_cursor_atom)*