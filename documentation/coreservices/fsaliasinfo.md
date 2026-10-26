# FSAliasInfo

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Defines an information block passed to the `FSCopyAliasInfo` function.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.2+

## Declaration

```c
typedef struct FSAliasInfo {
    ...
} FSAliasInfo;
```

## Topics

### Instance Properties
- [fileCreator](./fsaliasinfo/api-1444368-filecreator.md)
  The creator code of the target.
- [fileType](./fsaliasinfo/api-1444341-filetype.md)
  The file type of the target.
- [filesystemID](./fsaliasinfo/api-1444355-filesystemid.md)
  The filesystem ID.
- [isDirectory](./fsaliasinfo/api-1444331-isdirectory.md)
  A Boolean value indicating whether the alias target is a directory.
- [nodeID](./fsaliasinfo/api-1444299-nodeid.md)
  The ID of the file or directory that is the alias target.
- [parentDirID](./fsaliasinfo/api-1444444-parentdirid.md)
  The directory ID of the target’s parent directory.
- [signature](./fsaliasinfo/api-1444305-signature.md)
  The volume signature of the volume on which the target resides.
- [targetCreateDate](./fsaliasinfo/api-1444351-targetcreatedate.md)
  The creation date of the alias target.
- [volumeCreateDate](./fsaliasinfo/api-1444411-volumecreatedate.md)
  The creation date of the volume on which the alias target resides.
- [volumeHasPersistentFileIDs](./fsaliasinfo/api-1444322-volumehaspersistentfileids.md)
  A Boolean value indicating whether the volume has persistent file ID’s.
- [volumeIsAutomounted](./fsaliasinfo/api-1444329-volumeisautomounted.md)
  A Boolean value indicating whether the volume is automounted.
- [volumeIsBootVolume](./fsaliasinfo/api-1444347-volumeisbootvolume.md)
  A Boolean value indicating whether the volume is the boot volume.
- [volumeIsEjectable](./fsaliasinfo/api-1444281-volumeisejectable.md)
  A Boolean value indicating whether the volume is ejectable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fsaliasinfo)*