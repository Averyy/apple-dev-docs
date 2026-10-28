# getIndexEntry

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn getIndexEntry(
 intentry,
 UInt32 &value);
```

## Return Value

kIOReturnSuccess if the index exists in the dictionary

## Overview

Gets the entry at the specified index of the directory, as a raw UInt32.

## Parameters

- `entry`: on return, set to the entry value
- `value`: reference to variable to store the entry's value

## See Also

### Miscellaneous
- [getIndexKey](./api-1811157-getindexkey.md)
- [getIndexType](./api-1811166-getindextype.md)
- [getIndexValue](./api-1811176-getindexvalue.md)
- [getKeySubdirectories](./api-1811186-getkeysubdirectories.md)
- [getKeyType](./api-1811199-getkeytype.md)
- [getKeyValue](./api-1811212-getkeyvalue.md)
- [getSubdirectories](./api-1811222-getsubdirectories.md)
- [update](./api-1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811146-getindexentry)*