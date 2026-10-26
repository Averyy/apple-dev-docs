# FSGetVolumeInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr FSGetVolumeInfo(FSVolumeRefNum volume, ItemCount volumeIndex, FSVolumeRefNum *actualVolume, FSVolumeInfoBitmap whichInfo, FSVolumeInfo *info, HFSUniStr255 *volumeName, FSRef *rootDirectory);
```

## See Also

### Getting and Setting Volume Information
- [FSSetVolumeInfo](./api-1565574-fssetvolumeinfo.md)
- [PBGetVolumeInfoAsync](./api-1565244-pbgetvolumeinfoasync.md)
- [PBGetVolumeInfoSync](./api-1566892-pbgetvolumeinfosync.md)
- [PBSetVolumeInfoAsync](./api-1566541-pbsetvolumeinfoasync.md)
- [PBSetVolumeInfoSync](./api-1566427-pbsetvolumeinfosync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1566350-fsgetvolumeinfo)*