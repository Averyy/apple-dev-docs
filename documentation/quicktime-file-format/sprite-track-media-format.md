# Sprite track media format

**Framework**: QuickTime File Format

A media format for that stores sprite track information in atoms.

#### Overview

> ❗ **Important**: Sprite media is deprecated in the QuickTime file format. The information that follows documents existing content containing sprite media and should not be used for new development.

The sprite track media format is hierarchical and based on QT atoms and atom containers. A sprite track is defined by one or more key frame samples, each followed by any number of override samples. A key frame sample and its subsequent override samples define a scene in the sprite track. A key frame sample is a QT atom container that contains atoms defining the sprites in the scene and their initial properties. The override samples are other QT atom containers that contain atoms that modify sprite properties, thereby animating the sprites in the scene. In addition to defining properties for individual sprites, you can also define properties that apply to an entire sprite track.

The QT atom container contains one child atom for each sprite in the key frame sample. Each sprite atom has a type of `kSpriteAtomType`. The sprite IDs are numbered from `1` to the number of sprites defined by the key frame sample (`numSprites`).

Each sprite atom contains leaf atoms that define the properties of the sprite. For example, the `kSpritePropertyLayer` property defines a sprite’s layer. Each sprite property atom has an atom type that corresponds to the property and an ID of `1`.

In addition to the sprite atoms, the QT atom container contains one atom of type `kSpriteSharedDataAtomType` with an ID of `1`. The atoms contained by the shared data atom describe data that is shared by all sprites. The shared data atom contains one atom of type `kSpriteImagesContainerAtomType` with an ID of `1`.

The image container atom contains one atom of type `kImageAtomType` for each image in the key frame sample. The image atom IDs are numbered from `1` to the number of images (`numImages`). Each image atom contains a leaf atom that holds the image data (type `kSpriteImageDataAtomType`) and an optional leaf atom (type `kSpriteNameAtomType`) that holds the name of the image.

#### Sprite Media Format Atoms

The sprite track’s sample format enables you to store the atoms necessary to describe action lists that are executed in response to QuickTime events. [`QT atom container description key`](qt_atom_container_description_key.md) defines a grammar for constructing valid action sprite samples, which may include complex expressions.

Both key frame samples and override samples support the sprite action atoms. Override samples override actions at the QuickTime event level. In effect, what you do by overriding is to completely replace one event handler and all its actions with another. The sprite track’s `kSpriteTrackPropertySampleFormat` property has no effect on how actions are performed. The behavior is similar to the default `kKeyFrameAndSingleOverride` format where, if in a given override sample there is no handler for the event, the key frame’s handler is used, if there is one.

#### Sprite Media Format Extensions

This section describes some of the atom types and IDs used to extend the sprite track’s media format, thus enabling action sprite capabilities.

A complete description of the grammar for sprite media handler samples, including action sprite extensions, is included in the section [`Sprite media handler track properties QT atom container format`](sprite_media_handler_track_properties_qt_atom_container_format.md).

> ❗ **Important**: Some sprite track property atoms were added in QuickTime 4. In particular, you must set the `kSpriteTrackPropertyHasActions` track property in order for your sprite actions to be executed.

#### Sprite Track Property Atoms

The following constants represent atom types for sprite track properties. These atoms are applied to the whole track, not just to a single sample.

## See Also

- [Sprite media](sprite_media.md)
  Sprite media is used to store character-based animation data in QuickTime movies.
- [Sprite track properties](sprite_track_properties.md)
  Define properties that apply to an entire sprite track.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sprite_track_media_format)*