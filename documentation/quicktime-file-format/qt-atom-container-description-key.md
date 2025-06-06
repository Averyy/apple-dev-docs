# QT atom container description key

**Framework**: QuickTime File Format

Build QT atom container-based data structures.

#### Overview

Because QT atom container–based data structures are widely used in QuickTime, a description key is presented here. Its usage is illustrated in the following sections, [`Sprite media handler track properties QT atom container format`](sprite_media_handler_track_properties_qt_atom_container_format.md) and [`Sprite media handler sample QT atom container formats`](sprite_media_handler_sample_qt_atom_container_formats.md).

```c
[(QTAtomFormatName)] =
atomType_1, id, index
    data
atomType_n, id, index
    data
```

The atoms may be required or optional:

```c
 // optional atom
 // required atom
<atomType>
atomType
```

The atom ID may be a number if it is required to be a constant, or it may be a list of valid atom IDs, indicating that multiple atoms of this type are allowed.

```c
3               // one atom with id of 3
(1..3)          // three atoms with id's of 1, 2, and 3
(1, 5, 7)       // three atoms with id's of 1, 5, and 7
(anyUniqueIDs)  // multiple atoms each with a unique id
```

The atom index may be a `1` if only one atom of this type is allowed, or it may be a range from `1` to some constant or variable.

```c
1               // one atom of this type is allowed, index is always  1
(1..3)          // three atoms with indexes 1, 2, and 3
(1..numAtoms)   // numAtoms atoms with indexes of 1 to numAtoms
```

The data may be leaf data in which its data type is listed inside of brackets [], or it may be a nested tree of atoms.

```c
[theDataType]   // leaf data of type theDataType
childAtoms      // a nested tree of atoms
```

Nested `QTAtom` format definitions [(AtomFormatName)] may appear in a definition.

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
- [Node information atom container](node_information_atom_container.md)
  An atom container that includes general information about the node such as the node’s type, ID, and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/qt_atom_container_description_key)*