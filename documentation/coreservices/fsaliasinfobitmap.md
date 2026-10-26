# FSAliasInfoBitmap

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Returned by the `FSCopyAliasInfo` function to indicate which fields of the alias information structure contain valid data.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.2+

## Declaration

```c
typedef UInt32 FSAliasInfoBitmap;
```

## Topics

### Constants
- [kFSAliasInfoNone](./api-1444335-anonymous/kfsaliasinfonone.md)
  None of the alias information is valid.
- [kFSAliasInfoVolumeCreateDate](./api-1444335-anonymous/kfsaliasinfovolumecreatedate.md)
  The volume creation date in the `volumeCreateDate` field is valid.
- [kFSAliasInfoTargetCreateDate](./api-1444335-anonymous/kfsaliasinfotargetcreatedate.md)
  The creation date of the alias target, in the `targetCreateDate` field, is valid.
- [kFSAliasInfoFinderInfo](./api-1444335-anonymous/kfsaliasinfofinderinfo.md)
  The file type and creator information, in the `fileType` and `fileCreator` fields, is valid.
- [kFSAliasInfoIsDirectory](./api-1444335-anonymous/kfsaliasinfoisdirectory.md)
  The information in the `isDirectory` field is valid.
- [kFSAliasInfoIDs](./api-1444335-anonymous/kfsaliasinfoids.md)
  The parent directory ID and alias target ID, in the `parentDirID` and `nodeID` fields, are valid.
- [kFSAliasInfoFSInfo](./api-1444335-anonymous/kfsaliasinfofsinfo.md)
  The filesystem ID and signature, in the `filesystemID` and `signature` fields, are valid.
- [kFSAliasInfoVolumeFlags](./api-1444335-anonymous/kfsaliasinfovolumeflags.md)
  The volume information, in the `volumeIsBootVolume`, `volumeIsAutomounted`, `volumeIsEjectable`, and `volumeHasPersistentFileIDs` fields, is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fsaliasinfobitmap)*