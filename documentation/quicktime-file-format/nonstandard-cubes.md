# Nonstandard cubes

**Framework**: QuickTime File Format

An atom you add to the pano sample atom container to specify cubes other than six square faces.

#### Overview

> ❗ **Important**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

Although the default representation for a cubic panorama is that of six square faces of a cube, it is possible to depart from this standard representation. When doing so, a new atom must be added to the pano sample atom container. The atom type is `'cufa'`. The atom is an array of data structures of type `QTVRCubicFaceData`. Each entry in the array describes one face of whatever polyhedron is being defined. `QTVRCubicFaceData` is defined as follows:

```c
struct QTVRCubicFaceData {
    float   orientation[4];
    float   center[2];
    float   aspect;
    float   skew;
};
typedef struct QTVRCubicFaceData    QTVRCubicFaceData;
```

The mathematical explanation of these data structures is beyond the scope of this content. The following table shows what values QuickTime VR uses for the default representation of six square sides.

| Orien- tation | Orien- tation | Orien- tation | Orien- tation | Center | Center | Aspect | Skew | Side |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `0` | `0` | `0` | `0` | `0` | `1` | `0` | # front |
| `-.5` | `0` | `.5` | `0` | `0` | `0` | `1` | `0` | # right |
| `0` | `0` | `1` | `0` | `0` | `0` | `1` | `0` | # back |
| `.5` | `0` | `.5` | `0` | `0` | `0` | `1` | `0` | # left |
| `.5` | `.5` | `0` | `0` | `0` | `0` | `1` | `0` | # top |
| `-.5` | `.5` | `0` | `0` | `0` | `0` | `1` | `0` | # bottom |

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/nonstandard_cubes)*