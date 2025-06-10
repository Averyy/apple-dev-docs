# getIndexType

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn getIndexType(
 int index,
 IOConfigKeyType &type);
```

#### Return_value

kIOReturnSuccess if the index exists in the dictionary

#### Overview

Gets the data type for entry at the specified index

## Parameters

- `type`: on return, set to the data type

## See Also

- [getIndexEntry](ioconfigdirectory/1811146-getindexentry.md)
- [getIndexKey](ioconfigdirectory/1811157-getindexkey.md)
- [getIndexValue](ioconfigdirectory/1811176-getindexvalue.md)
- [getKeySubdirectories](ioconfigdirectory/1811186-getkeysubdirectories.md)
- [getKeyType](ioconfigdirectory/1811199-getkeytype.md)
- [getKeyValue](ioconfigdirectory/1811212-getkeyvalue.md)
- [getSubdirectories](ioconfigdirectory/1811222-getsubdirectories.md)
- [update](ioconfigdirectory/1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811166-getindextype)*