# FSFileOperationStatusProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.4+

## Declaration

```c
typedef void (*FSFileOperationStatusProcPtr)(FSFileOperationRef fileOp, const FSRef *currentItem, FSFileOperationStage stage, OSStatus error, CFDictionaryRef statusDictionary, void *info);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fsfileoperationstatusprocptr)*