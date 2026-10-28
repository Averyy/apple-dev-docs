# MDImporter

**Framework**: Core Services  
**Role**: API Collection

## Overview

An MDImporter is responsible for returning the metadata containedwith a file. The Spotlight server is notified when a file is changedand loads the appropriate importer to extract the metadata. An importeris implemented as a CFPlugin.

## Topics

### Callbacks
- [ImporterImportData](./mdimporter/importerimportdata.md)
  Defines a pointer toan importer import callback that imports importers.
### Constants
- [kMDImporterTypeID](./mdimporter/kmdimportertypeid.md)
  Type ID of an importer plug-in.
- [kMDImporterInterfaceID](./mdimporter/kmdimporterinterfaceid.md)
  Interface required by a importer plug-in.

## See Also

### Related Documentation
- [Spotlight Overview](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/MetadataIntro.html#//apple_ref/doc/uid/TP40001268)
- [Spotlight Importer Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/MDImporters.html#//apple_ref/doc/uid/TP40001267)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mdimporter)*