# getSubdirectories

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn getSubdirectories(
 OSIterator *&iterator);
```

#### Return_value

kIOReturnSuccess if the iterator could be created

#### Overview

Creates an iterator over the subdirectories of the directory.

## Parameters

- `iterator`: on return, set to point to an OSIterator

## See Also

- [getIndexEntry](ioconfigdirectory/1811146-getindexentry.md)
- [getIndexKey](ioconfigdirectory/1811157-getindexkey.md)
- [getIndexType](ioconfigdirectory/1811166-getindextype.md)
- [getIndexValue](ioconfigdirectory/1811176-getindexvalue.md)
- [getKeySubdirectories](ioconfigdirectory/1811186-getkeysubdirectories.md)
- [getKeyType](ioconfigdirectory/1811199-getkeytype.md)
- [getKeyValue](ioconfigdirectory/1811212-getkeyvalue.md)
- [update](ioconfigdirectory/1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811222-getsubdirectories)*