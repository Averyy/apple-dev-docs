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

**Constant Descriptions**

- **`kSpriteAtomType`**: The atom is a parent atom that describes a sprite. It contains atoms that describe properties of the sprite. Optionally, it may also include an atom of type `kSpriteNameAtomType` that defines the name of the sprite.
- **`kSpriteImagesContainerAtomType`**: The atom is a parent atom that contains atoms of type `kSpriteImageAtomType`.
- **`kSpriteImageAtomType`**: The atom is a parent atom that contains an atom of type `kSpriteImageDataAtomType`. Optionally, it may also include an atom of type `kSpriteNameAtomType` that defines the name of the image.
- **`kSpriteImageDataAtomType`**: The atom is a leaf atom that contains image data.
- **`kSpriteSharedDataAtomType`**: The atom is a parent atom that contains shared sprite data, such as an atom container of type `kSpriteImagesContainerAtomType`.
- **`kSpriteNameAtomType`**: The atom is a leaf atom that contains the name of a sprite or an image. The leaf data is composed of one or more ASCII characters.
- **`kSpritePropertyImageIndex`**: A leaf atom containing the image index property which is of type `short`. This atom is a child atom of `kSpriteAtom`.
- **`kSpritePropertyLayer`**: A leaf atom containing the layer property which is of type `short`. This atom is a child atom of `kSpriteAtom`.
- **`kSpritePropertyMatrix`**: A leaf atom containing the matrix property which is of type `MatrixRecord`. This atom is a child atom of `kSpriteAtom`.
- **`kSpritePropertyVisible`**: A leaf atom containing the visible property which is of type `short`. This atom is a child atom of `kSpriteAtom`.
- **`kSpritePropertyGraphicsMode`**: A leaf atom containing the graphics mode property which is of type `ModifyerTrackGraphicsModeRecord`. This atom is a child atom of `kSpriteAtom`.
- **`kSpritePropertyBackgroundColor`**: A leaf atom containing the background color property which is of type `RGBColor`. This atom is used in a sprite track’s `MediaPropertyAtom` atom container.
- **`kSpritePropertyOffscreenBitDepth`**: A leaf atom containing the preferred offscreen bit depth which is of type `short`. This atom is used in a sprite track’s `MediaPropertyAtom` atom container.
- **`kSpritePropertySampleFormat`**: A leaf atom containing the sample format property, which is of type `short`. This atom is used in a sprite track’s `MediaPropertyAtom` atom container.
- **`kSpriteImageRegistrationAtomType`**: Sprite images have a default registration point of `0, 0`. To specify a different point, add an atom of type `kSpriteImageRegistrationAtomType` as a child atom of the `kSpriteImageAtomType` and set its leaf data to a `FixedPoint` value with the desired registration point.
- **`kSpriteImageGroupIDAtomType`**: You must assign group IDs to sets of equivalent images in your key frame sample. For example, if the sample contains ten images where the first two images are equivalent, and the last eight images are equivalent, then you could assign a group ID of `1000` to the first two images, and a group ID of `1001` to the last eight images. This divides the images in the sample into two sets. The actual ID does not matter, it just needs to be a unique positive integer. Each image in a sprite media key frame sample is assigned to a group. Add an atom of type `kSpriteImageGroupIDAtomType` as a child of the `kSpriteImageAtomType` atom and set its leaf data to a `long` value containing the group ID.

> ❗ **Important**: You must assign group IDs to your sprite sample if you want a sprite to display images with non-equivalent image descriptions (i.e., images with different dimensions).

For each of the following atom types (added to QuickTime 4) — except `kSpriteBehaviorsAtomType` — you fill in the structure `QTSpriteButtonBehaviorStruct`, which contains a value for each of the four states.

- **`kSpriteBehaviorsAtomType`**: This is the parent atom of `kSpriteImageBehaviorAtomType`, `kSpriteCursorBehaviorAtomType`, and `kSpriteStatusStringsBehaviorAtomType`.
- **`kSpriteImageBehaviorAtomType`**: Specifies the `imageIndex`.
- **`kSpriteCursorBehaviorAtomType`**: Specifies the `cursorID`.
- **`kSpriteStatusStringsBehaviorAtomType`**: Specifies an ID of a string variable contained in a sprite track to display in the status area of the browser.

> **Note**: All sprite media — specifically the leaf data in the QT atom containers for sample and sprite track properties — should be written in big-endian format.

- **`kSpriteUsesImageIDsAtomType`**: This atom allows a sprite to specify which images it uses — in other words, the subset of images that its `imageIndex` property can refer to. You add an atom of type `kSpriteUsesImageIDsAtomType` as a child of a `kSpriteAtomType` atom, setting its leaf data to an array of QT atom IDs. This array contains the IDs of the images used, not the indices.

Although QuickTime does not currently use this atom internally, tools that edit sprite media can use the information provided to optimize certain operations, such as cut, copy, and paste.

- **`kSpriteImageRegistrationAtomType`**: Sprite images have a default registration point of `0, 0`. To specify a different point, you add an atom of type `kSpriteImageRegistrationAtomType` as a child atom of the `kSpriteImageAtomType` and set its leaf data to a `FixedPoint` value with the desired registration point.
- **`kSpriteImageGroupIDAtomType`**: You must assign group IDs to sets of equivalent images in your key frame sample. For example, if the sample contains ten images where the first two images are equivalent, and the last eight images are equivalent, then you could assign a group ID of `1000` to the first two images, and a group ID of `1001` to the last eight images. This divides the images in the sample into two sets. The actual ID does not matter; it just needs to be a unique positive integer. Each image in a sprite media key frame sample is assigned to a group. You add an atom of type `kSpriteImageGroupIDAtomType` as a child of the `kSpriteImageAtomType` atom and set its leaf data to a `long` value containing the group ID.

> ❗ **Important**: You must assign group IDs to your sprite sample if you want a sprite to display images with non-equivalent image descriptions (that is, images with different dimensions).

You use the following atom types, which were added to QuickTime 4, to specify that an image is referenced and how to access it.

- **`kSpriteImageDataRefAtomType`**: Add this atom as a child of the `kSpriteImageAtomType` atom instead of a `kSpriteImageDataAtomType`. Its ID should be `1`. Its data should contain the data reference (similar to the `dataRef` parameter of `GetDataHandler`).
- **`kSpriteImageDataRefTypeAtomType`**: Add this atom as a child of the `kSpriteImageAtomType` atom. Its ID should be `1`. Its data should contain the data reference type (similar to the `dataRefType` parameter of `GetDataHandler`).
- **`kSpriteImageDefaultImageIndexAtomType`**: You may optionally add this atom as a child of the `kSpriteImageAtomType` atom. Its ID should be `1`. Its data should contain a `short`, which specifies an image index of a traditional image to use while waiting for the referenced image to load.

The following constants represent formats of a sprite track. The value of the constant indicates how override samples in a sprite track should be interpreted. You set a sprite track’s format by creating a `kSpriteTrackPropertySampleFormat` atom.

```c
enum {
    kKeyFrameAndSingleOverride      = 1L << 1,
    kKeyFrameAndAllOverrides        = 1L << 2
};
```

**Constant Descriptions**

- **`kKeyFrameAndSingleOverride`**: The current state of the sprite track is defined by the most recent key frame sample and the current override sample. This is the default format.
- **`kKeyFrameAndAllOverrides`**: The current state of the sprite track is defined by the most recent key frame sample and all subsequent override samples up to and including the current override sample.

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