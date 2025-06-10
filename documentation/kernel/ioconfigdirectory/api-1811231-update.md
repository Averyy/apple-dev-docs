# update

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn update(
 UInt32 offset,
 const UInt32 *&romBase) = 0;
```

#### Return_value

kIOReturnSuccess if the specified offset is now accessable at romBase[offset].

#### Overview

makes sure that the ROM has at least the specified capacity, and that the ROM is uptodate from its start to at least the specified quadlet offset.

## See Also

- [getIndexEntry](ioconfigdirectory/1811146-getindexentry.md)
- [getIndexKey](ioconfigdirectory/1811157-getindexkey.md)
- [getIndexType](ioconfigdirectory/1811166-getindextype.md)
- [getIndexValue](ioconfigdirectory/1811176-getindexvalue.md)
- [getKeySubdirectories](ioconfigdirectory/1811186-getkeysubdirectories.md)
- [getKeyType](ioconfigdirectory/1811199-getkeytype.md)
- [getKeyValue](ioconfigdirectory/1811212-getkeyvalue.md)
- [getSubdirectories](ioconfigdirectory/1811222-getsubdirectories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811231-update)*