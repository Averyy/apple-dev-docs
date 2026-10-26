# kIOStorageFeatureUnmap

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

Describes the presence of the Unmap feature.

**Availability**:
- macOS 10.7+

## Declaration

```c
#define kIOStorageFeatureUnmap
```

#### Discussion

This property describes the ability of the storage stack to delete unused data from the media. It is one of the feature entries listed under the top- level kIOStorageFeaturesKey property table. It has an OSBoolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiostoragefeatureunmap)*