# Sprite media atom and data types

**Framework**: QuickTime File Format

Atoms that represent sprite media and data types.

#### Overview

> ❗ **Important**: Sprite media is deprecated in the QuickTime file format. The information that follows documents existing content containing sprite media and should not be used for new development.

The following constants represent atom types for sprite media:

```c
enum {
    kSpriteAtomType                     = 'sprt',
    kSpriteImagesContainerAtomType      = 'imct',
    kSpriteImageAtomType                = 'imag',
    kSpriteImageDataAtomType            = 'imda',
    kSpriteImageDataRefAtomType         = 'imre',
    kSpriteImageDataRefTypeAtomType     = 'imrt',
    kSpriteImageGroupIDAtomType         = 'imgr',
    kSpriteImageRegistrationAtomType    = 'imrg',
    kSpriteImageDefaultImageIndexAtomType ='defi',
    kSpriteSharedDataAtomType           = 'dflt',
    kSpriteNameAtomType                 = 'name',
    kSpriteImageNameAtomType            = 'name',
    kSpriteUsesImageIDsAtomType         = 'uses',
    kSpriteBehaviorsAtomType            = 'beha',
    kSpriteImageBehaviorAtomType        = 'imag',
    kSpriteCursorBehaviorAtomType       = 'crsr',
    kSpriteStatusStringsBehaviorAtomType = 'sstr',
    kSpriteVariablesContainerAtomType    = 'vars',
    kSpriteStringVariableAtomType        = 'strv',
    kSpriteFloatingPointVariableAtomType = 'flov'
    kSpriteSharedDataAtomType           = 'dflt',
    kSpriteURLLinkAtomType              = 'url '
    kSpritePropertyMatrix               = 1
    kSpritePropertyVisible              = 4
    kSpritePropertyLayer                = 5
    kSpritePropertyGraphicsMode         = 6
    kSpritePropertyImageIndex           = 100
    kSpritePropertyBackgroundColor      = 101
    kSpritePropertyOffscreenBitDepth    = 102
    kSpritePropertySampleFormat         = 103
};
```

> ❗ **Important**: You must assign group IDs to your sprite sample if you want a sprite to display images with non-equivalent image descriptions (i.e., images with different dimensions).

For each of the following atom types (added to QuickTime 4) — except `kSpriteBehaviorsAtomType` — you fill in the structure `QTSpriteButtonBehaviorStruct`, which contains a value for each of the four states.

> **Note**: All sprite media — specifically the leaf data in the QT atom containers for sample and sprite track properties — should be written in big-endian format.

Although QuickTime does not currently use this atom internally, tools that edit sprite media can use the information provided to optimize certain operations, such as cut, copy, and paste.

> ❗ **Important**: You must assign group IDs to your sprite sample if you want a sprite to display images with non-equivalent image descriptions (that is, images with different dimensions).

You use the following atom types, which were added to QuickTime 4, to specify that an image is referenced and how to access it.

The following constants represent formats of a sprite track. The value of the constant indicates how override samples in a sprite track should be interpreted. You set a sprite track’s format by creating a `kSpriteTrackPropertySampleFormat` atom.

```c
enum {
    kKeyFrameAndSingleOverride      = 1L << 1,
    kKeyFrameAndAllOverrides        = 1L << 2
};
```

## See Also

- [Sprite media](sprite_media.md)
  Sprite media is used to store character-based animation data in QuickTime movies.
- [Sprite track properties](sprite_track_properties.md)
  Define properties that apply to an entire sprite track.
- [Sprite track media format](sprite_track_media_format.md)
  A media format for that stores sprite track information in atoms.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sprite_media_atom_and_data_types)*