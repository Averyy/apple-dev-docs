# FSVolumeMountProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.2+

## Declaration

```c
typedef void (*FSVolumeMountProcPtr)(FSVolumeOperation volumeOp, void *clientData, OSStatus err, FSVolumeRefNum mountedVolumeRefNum);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fsvolumemountprocptr)*