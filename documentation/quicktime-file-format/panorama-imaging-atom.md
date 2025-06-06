# Panorama imaging atom

**Framework**: QuickTime File Format  
**Kind**: class

An atom describes the default imaging characteristics for all the panoramic nodes in a scene.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

A panorama-imaging atom describes the default imaging characteristics for all the panoramic nodes in a scene. This atom overrides QuickTime VR’s own defaults.

The panorama-imaging atom has an atom type of `kQTVRPanoImagingAtomType` (`'impn'`). Generally, there is one panorama-imaging atom for each imaging mode, so the atom ID, while it must be unique for each atom, is ignored. QuickTime VR iterates through all the panorama-imaging atoms.

The structure of a panorama-imaging atom is defined by the `QTVRPanoImagingAtom` data type:

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
} QTVRPanoImagingAtom, *VRPanoImagingAtomPtr;
```

The imagingValidFlags field in the panorama-imaging atom structure specifies which imaging property fields in that structure are valid. You can use these bit flags to specify a value for that field:

```c
enum {
    kQTVRValidCorrection                        = 1 << 0,
    kQTVRValidQuality                           = 1 << 1,
    kQTVRValidDirectDraw                        = 1 << 2,
    kQTVRValidFirstExtraProperty                = 1 << 3
};
```

## Topics

### Data fields
- [majorVersion](panorama_imaging_atom/majorversion.md)
  The major version number of the file format.
- [minorVersion](panorama_imaging_atom/minorversion.md)
  The minor version number of the file format.
- [imagingMode](panorama_imaging_atom/imagingmode.md)
  The imaging mode to which the default values apply.
- [imagingValidFlags](panorama_imaging_atom/imagingvalidflags.md)
  A set of flags that indicate which imaging property fields in this structure are valid.
- [correction](panorama_imaging_atom/correction.md)
  The default correction mode for panoramic nodes.
- [quality](panorama_imaging_atom/quality.md)
  The default imaging quality for panoramic nodes.
- [directDraw](panorama_imaging_atom/directdraw.md)
  The default direct-drawing property for panoramic nodes.
- [imagingProperties](panorama_imaging_atom/imagingproperties.md)
  Reserved for future panorama-imaging properties.
- [reserved1](panorama_imaging_atom/reserved1.md)
  Reserved.
- [reserved2](panorama_imaging_atom/reserved2.md)
  Reserved.

## See Also

- [QTVR string atom](qtvr_string_atom.md)
  An atom that contains a string for QuickTime VR.
- [VR world atom container](vr_world_atom_container.md)
  An atom that contains name for the entire scene, the default node ID, and default imaging properties, as well as a list of the nodes contained in the QTVR track.
- [VR world header atom](vr_world_header_atom.md)
  An atom contains the name of the scene and the default node ID to be used when the file is first opened.
- [Imaging parent atom](imaging_parent_atom.md)
  An atom that is the parent atom of one or more node-specific imaging atoms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/panorama_imaging_atom)*