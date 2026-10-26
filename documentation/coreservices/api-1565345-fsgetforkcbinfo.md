# FSGetForkCBInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr FSGetForkCBInfo(FSIORefNum desiredRefNum, FSVolumeRefNum volume, short *iterator, FSIORefNum *actualRefNum, FSForkInfo *forkInfo, FSRef *ref, HFSUniStr255 *outForkName);
```

## See Also

### Obtaining Fork Control Block Information
- [PBGetForkCBInfoSync](./api-1566258-pbgetforkcbinfosync.md)
- [PBGetForkCBInfoAsync](./api-1566027-pbgetforkcbinfoasync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565345-fsgetforkcbinfo)*