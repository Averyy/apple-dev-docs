# Node information atom container

**Framework**: QuickTime File Format

An atom container that includes general information about the node such as the node’s type, ID, and name.

#### Overview

> ❗ **Important**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

The node information atom container includes general information about the node such as the node’s type, ID, and name. The node information atom container also contains the list of hot spot atoms for the node. A QuickTime VR movie contains one node information atom container for each node in the file. The routine `QTVRGetNodeInfo` allows you to obtain the node information atom container for the current node or for any other node in the movie.

The following shows the structure of the node information atom container.

```None
Node information
├── Node header
├── Name string
├── Comment string
└── Hot spot parent
    ├── Hot spot
    │   ├── Hot spot information
    │   ├── Name string
    │   ├── Comment string
    │   └── Link hot spot information
    ├── Hot spot
    │   ├── Hot spot information
    │   ├── Name string
    │   ├── Comment string
    │   └── Link hot spot information
    ├── ...
```

## Topics

### Specifying node information
- [Node header atom ('ndhd')](node_header_atom.md)
  An atom that describes the type and ID of a node, as well as other information about the node.
- [Hot spot parent atom ('hspa')](hot_spot_parent_atom.md)
  An atom that is the parent for all hot spot atoms for the node.
- [Hot spot information atom ('hsin')](hot_spot_information_atom.md)
  An atom that contains general information about a hot spot.
- [Specific information atom](specific_information_atom.md)
  An atom that identified the hot spot type.
- [Link hot spot atom ('link')](link_hot_spot_atom.md)
  An atom that specifies information for a link hot spot.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/node_information_atom_container)*