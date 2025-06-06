# Sprite media handler sample QT atom container formats

**Framework**: QuickTime File Format

Set sprite media handlers in QT atom containers.

#### Overview

> ❗ **Important**: Sprite media is deprecated in the QuickTime file format. The information that follows documents existing content containing sprite media and should not be used for new development.

Sprite media is deprecated in the QuickTime file format. The information that follows documents existing content containing sprite media and should not be used for new development.

```c
[(SpriteKeySample)] =
    [(SpritePropertyAtoms)]
    [(SpriteImageAtoms)]
 
 
[(SpriteOverrideSample)] =
    [(SpritePropertyAtoms)]
 
 
[(SpriteImageAtoms)]
    kSpriteSharedDataAtomType, 1, 1
        <kSpriteVariablesContainerAtomType>, 1
            <kSpriteStringVariableAtomType>, (1..n) ID is  SpriteTrack
                            Variable ID to be set
                                                [CString]
            <kSpriteFloatingPointVariableAtomType>, (1..n)  ID is
                            SpriteTrack Variable ID to be set
                                                [float]
 
        kSpriteImagesContainerAtomType, 1, 1
            kSpriteImageAtomType, theImageID, (1 .. numImages)
                kSpriteImageDataAtomType, 1, 1
                    [ImageData is ImageDescriptionHandle prepended  to
                                                            image  data]
                <kSpriteImageRegistrationAtomType, 1, 1>
                    [FixedPoint]
                <kSpriteImageNameAtomType, 1, 1>
                    [pString]
                <kSpriteImageGroupIDAtomType, 1, 1>
                    [long]
 
 
[(SpritePropertyAtoms)]
    <kQTEventFrameLoaded>, 1, 1
        [(ActionListAtoms)]
        <kCommentAtomType>, (anyUniqueIDs), (1..numComments)
            [CString]
 
    kSpriteAtomType, theSpriteID, (1 .. numSprites)
        <kSpritePropertyMatrix, 1, 1>
            [MatrixRecord]
        <kSpritePropertyVisible, 1, 1>
            [short]
        <kSpritePropertyLayer, 1, 1>
            [short]
        <kSpritePropertyImageIndex, 1, 1>
            [short]
        <kSpritePropertyGraphicsMode, 1, 1>
            [ModifierTrackGraphicsModeRecord]
 
        <kSpriteUsesImageIDsAtomType, 1, 1>
            [array of QTAtomID's, one per image used]
 
        <kSpriteBehaviorsAtomType>, 1
 
        <kSpriteImageBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]
        <kSpriteCursorBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]
        <kSpriteStatusStringsBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]
 
        <[(SpriteActionAtoms)]>
 
 
[(SpriteActionAtoms)] =
    kQTEventType, theQTEventType, (1 .. numEventTypes)
            [(ActionListAtoms)] //see the next section Wired Action
                                //Grammar for a description
            <kCommentAtomType>, (anyUniqueIDs), (1..numComments)
                [CString]
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
- [Sprite media handler track properties QT atom container format](sprite_media_handler_track_properties_qt_atom_container_format.md)
  Set sprite media handler track properties in a QT atom container.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sprite_media_handler_sample_qt_atom_container_formats)*