# update

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn update(
 UInt32 offset,
 const UInt32 *&romBase) = 0;
```

#### Return Value

kIOReturnSuccess if the specified offset is now accessable at romBase[offset].

#### Overview

makes sure that the ROM has at least the specified capacity, and that the ROM is uptodate from its start to at least the specified quadlet offset.

## See Also

### Miscellaneous
- [getIndexEntry](./api-1811146-getindexentry.md)
- [getIndexKey](./api-1811157-getindexkey.md)
- [getIndexType](./api-1811166-getindextype.md)
- [getIndexValue](./api-1811176-getindexvalue.md)
- [getKeySubdirectories](./api-1811186-getkeysubdirectories.md)
- [getKeyType](./api-1811199-getkeytype.md)
- [getKeyValue](./api-1811212-getkeyvalue.md)
- [getSubdirectories](./api-1811222-getsubdirectories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811231-update)*