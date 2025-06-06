# Data types

**Framework**: QuickTime File Format

#### Overview

```c
typedef float                                       Float32;
```

#### Sample Description Header Structure

```c
typedef struct QTVRSampleDescription {
    UInt32                              size;
    UInt32                              type;
    UInt32                              reserved1;
    UInt16                              reserved2;
    UInt16                              dataRefIndex;
    UInt32                              data;
} QTVRSampleDescription, *QTVRSampleDescriptionPtr, **QTVRSampleDescriptionHandle;
```

#### String Atom Structure

```c
typedef struct QTVRStringAtom {
    UInt16                              stringUsage;
    UInt16                              stringLength;
    unsigned char                       string[4];
} QTVRStringAtom, *QTVRStringAtomPtr;
```

#### Vr World Header Atom Structure

```c
typedef struct QTVRWorldHeaderAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    QTAtomID                            nameAtomID;
    UInt32                              defaultNodeID;
    UInt32                              vrWorldFlags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRWorldHeaderAtom, *QTVRWorldHeaderAtomPtr;
```

#### Panorama Imaging Atom Structure

```c
typedef struct QTVRPanoImagingAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              imagingMode;
    UInt32                              imagingValidFlags;
    UInt32                              correction;
    UInt32                              quality;
    UInt32                              directDraw;
    UInt32                              imagingProperties[6];
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRPanoImagingAtom, *QTVRPanoImagingAtomPtr;
```

#### Node Location Atom Structure

```c
typedef struct QTVRNodeLocationAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              nodeType;
    UInt32                              locationFlags;
    UInt32                              locationData;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRNodeLocationAtom, *QTVRNodeLocationAtomPtr;
```

#### Node Header Atom Structure

```c
typedef struct QTVRNodeHeaderAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              nodeType;
    QTAtomID                            nodeID;
    QTAtomID                            nameAtomID;
    QTAtomID                            commentAtomID;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRNodeHeaderAtom, *QTVRNodeHeaderAtomPtr;
```

#### Hot Spot Information Atom Structure

```c
typedef struct QTVRHotSpotInfoAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              hotSpotType;
    QTAtomID                            nameAtomID;
    QTAtomID                            commentAtomID;
    SInt32                              cursorID[3];
    Float32                             bestPan;
    Float32                             bestTilt;
    Float32                             bestFOV;
    FloatPoint                          bestViewCenter;
    Rect                                hotSpotRect;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRHotSpotInfoAtom, *QTVRHotSpotInfoAtomPtr;
```

#### Link Hot Spot Atom Structure

```c
typedef struct QTVRLinkHotSpotAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              toNodeID;
    UInt32                              fromValidFlags;
    Float32                             fromPan;
    Float32                             fromTilt;
    Float32                             fromFOV;
    FloatPoint                          fromViewCenter;
    UInt32                              toValidFlags;
    Float32                             toPan;
    Float32                             toTilt;
    Float32                             toFOV;
    FloatPoint                          toViewCenter;
    Float32                             distance;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRLinkHotSpotAtom, *QTVRLinkHotSpotAtomPtr;
```

#### Angle Range Atom Structure

```c
typedef struct QTVRAngleRangeAtom {
    Float32                             minimumAngle;
    Float32                             maximumAngle;
} QTVRAngleRangeAtom, *QTVRAngleRangeAtomPtr;
```

#### Panorama Sample Atom Structure

```c
typedef struct QTVRPanoSampleAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              imageRefTrackIndex;
    UInt32                              hotSpotRefTrackIndex;
    Float32                             minPan;
    Float32                             maxPan;
    Float32                             minTilt;
    Float32                             maxTilt;
    Float32                             minFieldOfView;
    Float32                             maxFieldOfView;
    Float32                             defaultPan;
    Float32                             defaultTilt;
    Float32                             defaultFieldOfView;
    UInt32                              imageSizeX;
    UInt32                              imageSizeY;
    UInt16                              imageNumFramesX;
    UInt16                              imageNumFramesY;
    UInt32                              hotSpotSizeX;
    UInt32                              hotSpotSizeY;
    UInt16                              hotSpotNumFramesX;
    UInt16                              hotSpotNumFramesY;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRPanoSampleAtom, *QTVRPanoSampleAtomPtr;
```

#### Cubic View Atom Structure

```c
struct QTVRCubicViewAtom {
    Float32         minPan;
    Float32         maxPan;
    Float32         minTilt;
    Float32         maxTilt;
    Float32         minFieldOfView;
    Float32         maxFieldOfView;
 
    Float32         defaultPan;
    Float32         defaultTilt;
    Float32         defaultFieldOfView;
};
typedef struct QTVRCubicViewAtom    QTVRCubicViewAtom;
```

#### Cubic Face Data Atom Structure

```c
struct QTVRCubicFaceData {
    float   orientation[4];
    float   center[2];
    float   aspect;
    float   skew;
};
typedef struct QTVRCubicFaceData    QTVRCubicFaceData;
```

#### Object Sample Atom Structure

```c
typedef struct QTVRObjectSampleAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt16                              movieType;
    UInt16                              viewStateCount;
    UInt16                              defaultViewState;
    UInt16                              mouseDownViewState;
    UInt32                              viewDuration;
    UInt32                              columns;
    UInt32                              rows;
    Float32                             mouseMotionScale;
    Float32                             minPan;
    Float32                             maxPan;
    Float32                             defaultPan;
    Float32                             minTilt;
    Float32                             maxTilt;
    Float32                             defaultTilt;
    Float32                             minFieldOfView;
    Float32                             fieldOfView;
    Float32                             defaultFieldOfView;
    Float32                             defaultViewCenterH;
    Float32                             defaultViewCenterV;
    Float32                             viewRate;
    Float32                             frameRate;
    UInt32                              animationSettings;
    UInt32                              controlSettings;
} QTVRObjectSampleAtom, *QTVRObjectSampleAtomPtr;
```

#### Track Reference Entry Structure

```c
struct QTVRTrackRefEntry {
    UInt32                      trackRefType;
    UInt16                      trackResolution;
    UInt32                      trackRefIndex;
};
typedef struct QTVRTrackRefEntry QTVRTrackRefEntry;
```

## See Also

- [Constants](constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/data_types)*