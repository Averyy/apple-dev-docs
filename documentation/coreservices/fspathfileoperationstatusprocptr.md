# FSPathFileOperationStatusProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.4+

## Declaration

```c
typedef void (*FSPathFileOperationStatusProcPtr)(FSFileOperationRef fileOp, const char *currentItem, FSFileOperationStage stage, OSStatus error, CFDictionaryRef statusDictionary, void *info);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fspathfileoperationstatusprocptr)*