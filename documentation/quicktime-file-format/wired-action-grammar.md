# Wired action grammar

**Framework**: QuickTime File Format

Embed QT event handlers in their media samples.

#### Overview

The wired action grammar shown in this section allows QT event handlers to be expressed in a QuickTime movie. The sprite, text, VR, 3D, and Flash media handlers all support the embedding of QT event handlers in their media samples.

```c
[(ActionListAtoms)] =
    kAction, (anyUniqueIDs), (1..numActions)
        kWhichAction    1, 1
            [long whichActionConstant]
        <kActionParameter>  (anyUniqueIDs), (1..numParameters)
            [(parameterData)] ( whichActionConstant, paramIndex  )
    // either leaf data or child atoms
        <kActionFlags>  parameterID,  (1..numParamsWithFlags)
            [long actionFlags]
        <kActionParameterMinValue>  parameterID,  (1.. numParamsWithMin)
            [data depends on param type]
        <kActionParameterMaxValue>  parameterID,  (1.. numParamsWithMax)
            [data depends on param type]
        [(ActionTargetAtoms)]
 
        <kCommentAtomType>, (anyUniqueIDs), (1..numComments)
            [CString]
 
[(ActionTargetAtoms)] =
    <kActionTarget>
        <kTargetMovie>
            [no data]
    <kTargetChildMovieTrackName>
        <PString childMovieTrackName>
    <kTargetChildMovieTrack>
        [IDlong childMovieTrackID]
    <kTargetChildMovieTrackIndex>
            [long childMovieTrackIndex]
        <kTargetChildMovieMovieName>
            [PString childMovieName]
        <kTargetChildMovieMovieID>
            [long childMovieID]
        <kTargetTrackName>
            [PString trackName]
        <kTargetTrackType>
            [OSType trackType]
        <kTargetTrackIndex>
            [long trackIndex]
            OR
            [(kExpressionAtoms)]
        <kTargetTrackID>
            [long trackID]
            OR
            [(kExpressionAtoms)]
        <kTargetSpriteName>
            [PString spriteName]
        <kTargetSpriteIndex>
            [short spriteIndex]
            OR
            [(kExpressionAtoms)]
        <kTargetSpriteID>
            [QTAtomID spriteIID]
            OR
            [(kExpressionAtoms)]
        <kTargetQD3DNamedObjectName>
            [CString objectName]
 
[(kExpressionAtoms)] =
    kExpressionContainerAtomType, 1, 1
        <kOperatorAtomType, theOperatorType, 1>
            kOperandAtomType, (anyUniqueIDs), (1..numOperands)
                [(OperandAtoms)]
        OR
        <kOperandAtomType, 1, 1>
            [(OperandAtoms)]
[(ActionTargetAtoms)] =
    <kActionTarget>
 
        <kTargetMovieName>
            [Pstring MovieName]
        OR
        <kTargetMovieID>
            [long MovieID]
            OR
            [(kExpressionAtoms)]
 
[(OperandAtoms)] =
    <kOperandExpression> 1, 1
        [(kExpressionAtoms)]        // allows for recursion
    OR
    <kOperandConstant> 1, 1
        [ float theConstant ]
    OR
    <kOperandSpriteTrackVariable> 1, 1
        [(ActionTargetAtoms)]
        kActionParameter, 1, 1
            [QTAtomID spriteVariableID]
    OR
    <kOperandKeyIsDown> 1, 1
        kActionParameter, 1, 1
            [UInt16 modifierKeys]
        kActionParameter, 2, 2
            [UInt8 asciiCharCode]
    OR
    <kOperandRandom> 1, 1
        kActionParameter, 1, 1
            [short minimum]
        kActionParameter, 2, 2
            [short maximum]
    OR
    <any other operand atom type>
        [(ActionTargetAtoms)]
```

The format for parameter data depends on the action and parameter index.

In most cases, the `kActionParameter` atom is a leaf atom containing data; for a few parameters, it contains child atoms.

`whichAction` corresponds to the action type that is specified by the leaf data of a `kWhichAction` atom.

`paramIndex` is the index of the parameter’s `kActionParameter` atom.

```c
[(parameterData)] ( whichAction, paramIndex ) =
{
    kActionMovieSetVolume:
        param1:     short volume
 
    kActionMovieSetRate
        param1:     Fixed rate
 
    kActionMovieSetLoopingFlags
        param1:     long loopingFlags
 
    kActionMovieGoToTime
        param1:     TimeValue time
 
    kActionMovieGoToTimeByName
        param1:     Str255 timeName
 
    kActionMovieGoToBeginning
        no params
 
    kActionMovieGoToEnd
        no params
 
    kActionMovieStepForward
        no params
 
    kActionMovieStepBackward
        no params
 
    kActionMovieSetSelection
        param1:     TimeValue startTime
        param2:     TimeValue endTime
 
    kActionMovieSetSelectionByName
        param1:     Str255 startTimeName
        param2:     Str255 endTimeName
 
    kActionMoviePlaySelection
        param1:     Boolean selectionOnly
 
    kActionMovieSetLanguage
        param1:     long language
 
    kActionMovieChanged
        no params
 
    kActionTrackSetVolume
        param1:     short volume
 
    kActionTrackSetBalance
        param1:     short balance
 
    kActionTrackSetEnabled
        param1:     Boolean enabled
 
    kActionTrackSetMatrix
        param1:     MatrixRecord matrix
 
    kActionTrackSetLayer
        param1:     short layer
 
    kActionTrackSetClip
        param1:     RgnHandle clip
 
    kActionSpriteSetMatrix
        param1:     MatrixRecord matrix
 
    kActionSpriteSetImageIndex
        parm1:      short imageIndex
 
    kActionSpriteSetVisible
        param1:     short visible
 
    kActionSpriteSetLayer
        param1:     short layer
 
    kActionSpriteSetGraphicsMode
        param1:     ModifierTrackGraphicsModeRecord graphicsMode
 
    kActionSpritePassMouseToCodec
        no params
 
    kActionSpriteClickOnCodec
        param1:     Point localLoc
 
    kActionSpriteTranslate
        param1:     Fixed x
        param2:     Fixed y
        param3:     Boolean isRelative
 
    kActionSpriteScale
        param1:     Fixed xScale
        param2:     Fixed yScale
 
    kActionSpriteRotate
        param1:     Fixed degrees
 
    kActionSpriteStretch
        param1:     Fixed p1x
        param2:     Fixed p1y
        param3:     Fixed p2x
        param4:     Fixed p2y
        param5:     Fixed p3x
        param6:     Fixed p3y
        param7:     Fixed p4x
        param8:     Fixed p4y
 
 
    kActionQTVRSetPanAngle
        param1:     float panAngle
 
    kActionQTVRSetTiltAngle
        param1:     float tileAngle
 
    kActionQTVRSetFieldOfView
        param1:     float fieldOfView
 
    kActionQTVRShowDefaultView
        no params
 
    kActionQTVRGoToNodeID
        param1:     UInt32 nodeID
 
    kActionMusicPlayNote
        param1:     long sampleDescIndex
        param2:     long partNumber
        param3:     long delay
        param4:     long pitch
        param5:     long velocity
        param6:     long duration
 
    kActionMusicSetController
        param1:     long sampleDescIndex
        param2:     long partNumber
        param3:     long delay
        param4:     long controller
        param5:     long value
 
    kActionCase
        param1:     [(CaseStatementActionAtoms)]
 
    kActionWhile
        param1:     [(WhileStatementActionAtoms)]
 
    kActionGoToURL
        param1:     CString urlLink
 
    kActionSendQTEventToSprite
        param1:     [(SpriteTargetAtoms)]
        param2:     QTEventRecord theEvent
 
    kActionDebugStr
        param1:     Str255 theMessageString
 
    kActionPushCurrentTime
        no params
 
    kActionPushCurrentTimeWithLabel
        param1:     Str255 theLabel
 
    kActionPopAndGotoTopTime
        no params
 
    kActionPopAndGotoLabeledTime
        param1:     Str255 theLabel
 
    kActionSpriteTrackSetVariable
        param1:     QTAtomID variableID
        param2:     float value
 
    kActionApplicationNumberAndString
        param1:     long aNumber
        param2:     Str255 aString
}
```

Both [(CaseStatementActionAtoms)] and [(WhileStatementActionAtoms)] are child atoms of a `kActionParameter 1, 1` atom.

```c
[(CaseStatementActionAtoms)] =
    kConditionalAtomType, (anyUniqueIDs), (1..numCases)
        [(kExpressionAtoms)]
        kActionListAtomType 1, 1
            [(ActionListAtoms)] // may contain nested conditional  actions
 
[(WhileStatementActionAtoms)] =
    kConditionalAtomType, 1, 1
        [(kExpressionAtoms)]
        kActionListAtomType 1, 1
            [(ActionListAtoms)] // may contain nested conditional  actions
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
- [Sprite media handler sample QT atom container formats](sprite_media_handler_sample_qt_atom_container_formats.md)
  Set sprite media handlers in QT atom containers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/wired_action_grammar)*