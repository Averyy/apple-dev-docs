# Constants

**Framework**: QuickTime File Format

#### Vr World Atom Types

```c
enum {
    kQTVRWorldHeaderAtomType    = FOUR_CHAR_CODE('vrsc'),
    kQTVRImagingParentAtomType  = FOUR_CHAR_CODE('imgp'),
    kQTVRPanoImagingAtomType    = FOUR_CHAR_CODE('impn'),
    kQTVRObjectImagingAtomType  = FOUR_CHAR_CODE('imob'),
    kQTVRNodeParentAtomType     = FOUR_CHAR_CODE('vrnp'),
    kQTVRNodeIDAtomType         = FOUR_CHAR_CODE('vrni'),
    kQTVRNodeLocationAtomType   = FOUR_CHAR_CODE('nloc')
};
```

#### Node Information Atom Types

```c
enum {
    kQTVRNodeHeaderAtomType     = FOUR_CHAR_CODE('ndhd'),
    kQTVRHotSpotParentAtomType  = FOUR_CHAR_CODE('hspa'),
    kQTVRHotSpotAtomType        = FOUR_CHAR_CODE('hots'),
    kQTVRHotSpotInfoAtomType    = FOUR_CHAR_CODE('hsin'),
    kQTVRLinkInfoAtomType       = FOUR_CHAR_CODE('link')
};
```

#### Miscellaneous Atom Types

```c
enum {
    kQTVRStringAtomType             = FOUR_CHAR_CODE('vrsg'),
    kQTVRPanoSampleDataAtomType     = FOUR_CHAR_CODE('pdat'),
    kQTVRObjectInfoAtomType         = FOUR_CHAR_CODE('obji'),
    kQTVRAltImageTrackRefAtomType   = FOUR_CHAR_CODE('imtr'),
    kQTVRAltHotSpotTrackRefAtomType = FOUR_CHAR_CODE('hstr'),
    kQTVRAngleRangeAtomType         = FOUR_CHAR_CODE('arng'),
    kQTVRTrackRefArrayAtomType      = FOUR_CHAR_CODE('tref'),
    kQTVRPanConstraintAtomType      = FOUR_CHAR_CODE('pcon'),
    kQTVRTiltConstraintAtomType     = FOUR_CHAR_CODE('tcon'),
    kQTVRFOVConstraintAtomType      = FOUR_CHAR_CODE('fcon'),
    kQTVRCubicViewAtomType          = FOUR_CHAR_CODE('cuvw'),
    kQTVRCubicFaceDataAtomType      = FOUR_CHAR_CODE('cufa')
};
```

#### Track Reference Types

```c
enum {
    kQTVRImageTrackRefType      = FOUR_CHAR_CODE('imgt'),
    kQTVRHotSpotTrackRefType    = FOUR_CHAR_CODE('hott')
};
```

#### Imaging Property Valid Flags

```c
enum {
    kQTVRValidCorrection                        = 1 << 0,
    kQTVRValidQuality                           = 1 << 1,
    kQTVRValidDirectDraw                        = 1 << 2,
    kQTVRValidFirstExtraProperty                = 1 << 3
};
```

#### Link Hot Spot Valid Bits

```c
enum {
    kQTVRValidPan                               = 1 << 0,
    kQTVRValidTilt                              = 1 << 1,
    kQTVRValidFOV                               = 1 << 2,
    kQTVRValidViewCenter                        = 1 << 3
};
```

#### Animation Settings

```c
enum QTVRAnimationSettings {
    kQTVRObjectAnimateViewFramesOn              = (1 << 0),
    kQTVRObjectPalindromeViewFramesOn           = (1 << 1),
    kQTVRObjectStartFirstViewFrameOn            = (1 << 2),
    kQTVRObjectAnimateViewsOn                   = (1 << 3),
    kQTVRObjectPalindromeViewsOn                = (1 << 4),
    kQTVRObjectSyncViewToFrameRate              = (1 << 5),
    kQTVRObjectDontLoopViewFramesOn             = (1 << 6),
    kQTVRObjectPlayEveryViewFrameOn             = (1 << 7)
};
```

#### Control Settings

```c
enum QTVRControlSettings {
    kQTVRObjectWrapPanOn                        = (1 << 0),
    kQTVRObjectWrapTiltOn                       = (1 << 1),
    kQTVRObjectCanZoomOn                        = (1 << 2),
    kQTVRObjectReverseHControlOn                = (1 << 3),
    kQTVRObjectReverseVControlOn                = (1 << 4),
    kQTVRObjectSwapHVControlOn                  = (1 << 5),
    kQTVRObjectTranslationOn                    = (1 << 6)
};
```

#### Controller Subtype and Id

```c
enum {
    kQTControllerType                           = FOUR_CHAR_CODE('ctyp').
    kQTControllerID                             = 1
};
```

#### Object Controller Types

```c
enum ObjectUITypes {
    kGrabberScrollerUI                          = 1,
    kOldJoyStickUI                              = 2,
    kJoystickUI                                 = 3,
    kGrabberUI                                  = 4,
    kAbsoluteUI                                 = 5
};
```

#### Node Location Flag

```c
enum {
    kQTVRSameFile                               = 0
};
```

#### Panorama Sample Flag

```c
enum {
    kQTVRPanoFlagHorizontal                     = 1 << 0,
    kQTVRPanoFlagAlwaysWrap                     = 1 << 2
};
```

## See Also

- [Data types](data_types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/constants)*