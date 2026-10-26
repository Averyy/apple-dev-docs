# FSVolumeEjectProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.2+

## Declaration

```c
typedef void (*FSVolumeEjectProcPtr)(FSVolumeOperation volumeOp, void *clientData, OSStatus err, FSVolumeRefNum volumeRefNum, pid_t dissenter);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fsvolumeejectprocptr)*