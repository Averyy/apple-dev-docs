# getSubdirectories

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn getSubdirectories(
 OSIterator *&iterator);
```

#### Return Value

kIOReturnSuccess if the iterator could be created

#### Overview

Creates an iterator over the subdirectories of the directory.

## Parameters

- `iterator`: on return, set to point to an OSIterator

## See Also

### Miscellaneous
- [getIndexEntry](./api-1811146-getindexentry.md)
- [getIndexKey](./api-1811157-getindexkey.md)
- [getIndexType](./api-1811166-getindextype.md)
- [getIndexValue](./api-1811176-getindexvalue.md)
- [getKeySubdirectories](./api-1811186-getkeysubdirectories.md)
- [getKeyType](./api-1811199-getkeytype.md)
- [getKeyValue](./api-1811212-getkeyvalue.md)
- [update](./api-1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811222-getsubdirectories)*