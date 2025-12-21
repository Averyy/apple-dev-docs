# Node location atom structure ('nloc')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that describes the type of a node and its location.

#### Overview

The node location atom is the only child atom defined for the node ID atom. Its atom type is `kQTVRNodeLocationAtomType` (`'nloc'`). A node location atom describes the type of a node and its location.

The structure of a node location atom is defined by the `QTVRNodeLocationAtom` data type:

```c
typedef struct VRNodeLocationAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              nodeType;
    UInt32                              locationFlags;
    UInt32                              locationData;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRNodeLocationAtom, *QTVRNodeLocationAtomPtr;
QT
QT
```

## Topics

### Data fields
- [majorVersion](node_location_atom_structure/majorversion.md)
  The major version number of the file format.
- [minorVersion](node_location_atom_structure/minorversion.md)
  The minor version number of the file format.
- [nodeType](node_location_atom_structure/nodetype.md)
  The node type.
- [locationFlags](node_location_atom_structure/locationflags.md)
  The location flags.
- [locationData](node_location_atom_structure/locationdata.md)
  The location of the node data.
- [reserved1](node_location_atom_structure/reserved1.md)
  Reserved.
- [reserved2](node_location_atom_structure/reserved2.md)
  Reserved.

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
- [Custom cursor atom](custom_cursor_atom.md)
  An atom you use to replace the default cursors used by QuickTime VR.
- [Node information atom container](node_information_atom_container.md)
  An atom container that includes general information about the node such as the node’s type, ID, and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/node_location_atom_structure)*