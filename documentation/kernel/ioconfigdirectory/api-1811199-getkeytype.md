# getKeyType

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn getKeyType(
 int key,
 IOConfigKeyType &type);
```

## Return Value

kIOReturnSuccess if the key exists in the dictionary

## Overview

Gets the data type for the specified key

## Parameters

- `type`: on return, set to the data type

## See Also

### Miscellaneous
- [getIndexEntry](./api-1811146-getindexentry.md)
- [getIndexKey](./api-1811157-getindexkey.md)
- [getIndexType](./api-1811166-getindextype.md)
- [getIndexValue](./api-1811176-getindexvalue.md)
- [getKeySubdirectories](./api-1811186-getkeysubdirectories.md)
- [getKeyValue](./api-1811212-getkeyvalue.md)
- [getSubdirectories](./api-1811222-getsubdirectories.md)
- [update](./api-1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811199-getkeytype)*