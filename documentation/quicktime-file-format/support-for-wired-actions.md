# Support for wired actions

**Framework**: QuickTime File Format

Support wired actions in a QuickTime VR file.

#### Overview

> ❗ **Important**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

Certain actions on a QuickTime VR movie can trigger wired actions if the appropriate event handler atoms have been added to the file. This section discusses what atoms must be included in the QuickTime VR file to support wired actions.

As with sprite tracks, the presence of a certain atom in the media property atom container of the QTVR track enables the handling of wired actions. This atom is of type `kSpriteTrackPropertyHasActions`, which has a single Boolean value that must be set to `true`.

When certain events occur and the appropriate event handler atom is found in the QTVR file, then that atom is passed to QuickTime to perform any actions specified in the atom. The event handler atoms themselves must be added to the node information atom container in the QTVR track. There are two types of event handlers for QTVR nodes: global and hot spot specific. The currently supported global event handlers are `kQTEventFrameLoaded` and `kQTEventIdle`. The event handler atoms for these are located at the root level of the node information atom container. A global event handler atom’s type is set to the event type and its ID is set to `1`.

Hot spot–specific event handler atoms are located in the specific hot spot atom as a sibling to the hot spot info atom. For these atoms, the atom type is always `kQTEventType` and the ID is the `event` type. Supported hot spot–specific event types are `kQTEventMouseClick`, `kQTEventMouseClickEnd`, `kQTEventMouseClickEndTriggerButton`, and `kQTEventMouseEnter`, `kQTEventMouseExit`.

The specific actions that cause these events to be generated are described as follows:

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/support_for_wired_actions)*