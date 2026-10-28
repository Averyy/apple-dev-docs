# kIOStorageFeatureForceUnitAccess

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

Describes the presence of the Force Unit Access feature.

**Availability**:
- macOS 10.5+

## Declaration

```c
#define kIOStorageFeatureForceUnitAccess
```

## Discussion

This property describes the ability of the storage stack to force a request to access the media. It is one of the feature entries listed under the top- level kIOStorageFeaturesKey property table. It has an OSBoolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiostoragefeatureforceunitaccess)*