# Sprite media handler track properties QT atom container format

**Framework**: QuickTime File Format

Set sprite media handler track properties in a QT atom container.

#### Overview

> ❗ **Important**: Sprite media is deprecated in the QuickTime file format. The information that follows documents existing content containing sprite media and should not be used for new development.

Sprite media is deprecated in the QuickTime file format. The information that follows documents existing content containing sprite media and should not be used for new development.

```c
[(SpriteTrackProperties)]
    <kSpriteTrackPropertyBackgroundColor, 1, 1>
        [RGBColor]
    <kSpriteTrackPropertyOffscreenBitDepth, 1, 1>
        [short]
    <kSpriteTrackPropertySampleFormat, 1, 1>
        [long]
    <kSpriteTrackPropertyScaleSpritesToScaleWorld, 1, 1>
        [Boolean]
    <kSpriteTrackPropertyHasActions, 1, 1>
        [Boolean]
    <kSpriteTrackPropertyVisible, 1, 1>
        [Boolean]
    <kSpriteTrackPropertyQTIdleEventsFrequency, 1, 1>
        [UInt32]
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sprite_media_handler_track_properties_qt_atom_container_format)*