# Track references for object tracks

**Framework**: QuickTime File Format

Specify track references for object tracks.

#### Overview

> ❗ **Important**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

The track references to an object’s image and hot spot tracks are not handled the same way as track references to panoramas. The track reference types are the same (`kQTVRImageTrackRefType` and `kQTVRHotSpotTrackRefAtomType`), but the location of the reference indexes is different. There is no entry in the object sample atom for the track reference indexes. Instead, separate atoms using the `VRTrackRefEntry` structure are stored as siblings to the object sample atom. The types of these atoms are `kQTVRImageTrackRefAtomType` and `kQTVRHotSpotTrackRefAtomType`. If either of these atoms is not present, then the reference index to the corresponding track is assumed to be `1`.

> **Note**: The `trackResolution` field in the `VRTrackRefEntry` structure is ignored for object tracks.

The actual views of an object for an object node are contained in an object image track, which is usually a standard QuickTime video track. (An object image track can also be any type of track that is capable of displaying an image, such as a QuickTime 3D track.)

As described in Chapter 1 of [`QuickTime VR`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/0Preface/QTVR-preface.html#//apple_ref/doc/uid/TP40000944), these views are often captured by moving a camera around the object in a defined pattern of pan and tilt angles. The views must then be ordered into an object image array, which is stored as a one-dimensional sequence of frames in the movie’s video track.

For object movies containing frame animation, each animated view in the object image array consists of the animating frames. It is not necessary that each view in the object image array contain the same number of frames, but the view duration of all views in the object movie must be the same.

For object movies containing alternate view states, alternate view states are stored as separate object image arrays that immediately follow the preceding view state in the object image track. Each state does not need to contain the same number of frames. However, the total movie time of each view state in an object node must be the same.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_references_for_object_tracks)*