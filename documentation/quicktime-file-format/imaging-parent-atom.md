# Imaging parent atom

**Framework**: QuickTime File Format  
**Kind**: class

An atom that is the parent atom of one or more node-specific imaging atoms.

#### Overview

The imaging parent atom is the parent atom of one or more node-specific imaging atoms. Its atom type is `kQTVRImagingParentAtomType` (`'imgp'`). Only panoramas have an imaging atom defined.

## See Also

- [QTVR string atom](qtvr_string_atom.md)
  An atom that contains a string for QuickTime VR.
- [VR world atom container](vr_world_atom_container.md)
  An atom that contains name for the entire scene, the default node ID, and default imaging properties, as well as a list of the nodes contained in the QTVR track.
- [VR world header atom](vr_world_header_atom.md)
  An atom contains the name of the scene and the default node ID to be used when the file is first opened.
- [Panorama imaging atom](panorama_imaging_atom.md)
  An atom describes the default imaging characteristics for all the panoramic nodes in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/imaging_parent_atom)*