# kIOStorageCategory

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

kIOStorageCategory is a value for IOService's kIOMatchCategoryKey property.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOStorageCategory
```

#### Discussion

The kIOStorageCategory value is the standard value for the IOService property kIOMatchCategoryKey ("IOMatchCategory") for all storage drivers. All storage objects that expect to drive new content (that is, produce new media objects) are expected to compete within the kIOStorageCategory namespace.

See the IOService documentation for more information on match categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiostoragecategory)*