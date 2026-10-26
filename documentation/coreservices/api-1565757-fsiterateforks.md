# FSIterateForks

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr FSIterateForks(const FSRef *ref, CatPositionRec *forkIterator, HFSUniStr255 *forkName, SInt64 *forkSize, UInt64 *forkPhysicalSize);
```

## See Also

### Iterating Over Named Forks
- [PBIterateForksSync](./api-1566093-pbiterateforkssync.md)
- [PBIterateForksAsync](./api-1566251-pbiterateforksasync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565757-fsiterateforks)*