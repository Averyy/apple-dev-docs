# Sprite media

**Framework**: QuickTime File Format

Sprite media is used to store character-based animation data in QuickTime movies.

#### Overview

> ❗ **Important**: Sprite media is deprecated in the QuickTime file format. The information that follows documents existing content containing sprite media and should not be used for new development.

It has a media type of `'sprt'`.

#### Sprite Sample Description

The sprite sample description uses the standard sample description header, as described in [`Sample description atom ('stsd')`](sample_description_atom.md).

The data format field in the sample description is always set to `'sprt'`. The sprite media handler adds no additional fields to the sample description.

#### Sprite Sample Data

All sprite samples are stored in QT atom structures. The sprite media uses both key frames and differenced frames. The key frames contain all of the sprite’s image data, and the initial settings for each of the sprite’s properties.

A key frame always contains a shared data atom of type `'dflt'`. This atom contains data to be shared between the sprites, consisting mainly of image data and sample descriptions. The shared data atom contains a single sprite image container atom, with an atom type value of `'imct'` and an ID value of `1`.

The sprite image container atom stores one or more sprite image atoms of type `'imag'`. Each sprite image atom contains an image sample description immediately followed by the sprite’s compressed image data. The sprite image atoms should have ID numbers starting at `1` and counting consecutively upward.

The key frame also must contain definitions for each sprite in atoms of type `'sprt'`. Sprite atoms should have ID numbers start at `1` and count consecutively upward. Each sprite atom contains a list of properties. The following table shows all currently defined sprite properties.

| Property name | Value | Description |
| --- | --- | --- |
| `kSpritePropertyMatrix` | `1` | Describes the sprite’s location and scaling within its sprite world or sprite track. By modifying a sprite’s matrix, you can modify the sprite’s location so that it appears to move in a smooth path on the screen or so that it jumps from one place to another. You can modify a sprite’s size, so that it shrinks, grows, or stretches. Depending on which image compressor is used to create the sprite images, other transformations, such as rotation, may be supported as well. Translation-only matrices provide the best performance. |
| `kSpritePropertyVisible` | `4` | Specifies whether or not the sprite is visible. To make a sprite visible, you set the sprite’s visible property to `true`. |
| `kSpritePropertyLayer` | `5` | Contains a 16-bit integer value specifying the layer into which the sprite is to be drawn. Sprites with lower layer numbers appear in front of sprites with higher layer numbers. To designate a sprite as a background sprite, you should assign it the special layer number `kBackgroundSpriteLayerNum`. |
| `kSpritePropertyGraphicsMode` | `6` | Specifies a graphics mode and blend color that indicates how to blend a sprite with any sprites behind it and with the background. To set a sprite’s graphics mode, you call `SetSpriteProperty`, passing a pointer to a `ModifierTrackGraphicsModeRecord` structure. |
| `kSpritePropertyActionHandlingSpriteID` | `8` | Specifies another sprite by ID that delegates QT events. |
| `kSpritePropertyImageIndex` | `100` | Contains the atom ID of the sprite’s image atom. |

The override sample differs from the key frame sample in two ways. First, the override sample does not contain a shared data atom. All shared data must appear in the key frame. Second, only those sprite properties that change need to be specified. If none of a sprite’s properties change in a given frame, then the sprite does not need an atom in the differenced frame.

The override sample can be used in one of two ways: combined, as with video key frames, to construct the current frame; or the current frame can be derived by combining only the key frame and the current override sample.

Refer to the section [`Sprite track media format`](sprite_track_media_format.md) for information on how override samples are indicated in the file, using `kSpriteTrackPropertySampleFormat` and the default behavior of the `kKeyFrameAndSingleOverride` format.

## See Also

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
- [Node information atom container](node_information_atom_container.md)
  An atom container that includes general information about the node such as the node’s type, ID, and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sprite_media)*