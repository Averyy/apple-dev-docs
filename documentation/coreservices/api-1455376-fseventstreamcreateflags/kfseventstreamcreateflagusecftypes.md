# kFSEventStreamCreateFlagUseCFTypes

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
kFSEventStreamCreateFlagUseCFTypes = 0x00000001
```

## Discussion

The framework will invoke your callback function with CF types rather than raw C types (i.e., a CFArrayRef of CFStringRefs, rather than a raw C array of raw C string pointers). See FSEventStreamCallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1455376-fseventstreamcreateflags/kfseventstreamcreateflagusecftypes)*