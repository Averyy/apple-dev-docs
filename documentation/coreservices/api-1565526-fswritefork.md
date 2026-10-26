# FSWriteFork

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr FSWriteFork(FSIORefNum forkRefNum, UInt16 positionMode, SInt64 positionOffset, ByteCount requestCount, const void *buffer, ByteCount *actualCount);
```

## See Also

### Reading, Writing, and Closing Files
- [FSReadFork](./api-1565997-fsreadfork.md)
- [PBReadForkAsync](./api-1566703-pbreadforkasync.md)
- [PBReadForkSync](./api-1566739-pbreadforksync.md)
- [PBWriteForkSync](./api-1565632-pbwriteforksync.md)
- [PBWriteForkAsync](./api-1566491-pbwriteforkasync.md)
- [FSCloseFork](./api-1566900-fsclosefork.md)
- [PBCloseForkSync](./api-1566173-pbcloseforksync.md)
- [PBCloseForkAsync](./api-1565189-pbcloseforkasync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565526-fswritefork)*