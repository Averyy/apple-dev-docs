# FSPathMoveObjectToTrashAsync

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+ - Deprecated in 10.8

## Declaration

```c
OSStatus FSPathMoveObjectToTrashAsync(FSFileOperationRef fileOp, const char *sourcePath, OptionBits flags, FSPathFileOperationStatusProcPtr callback, CFTimeInterval statusChangeInterval, FSFileOperationClientContext *clientContext);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565270-fspathmoveobjecttotrashasync)*