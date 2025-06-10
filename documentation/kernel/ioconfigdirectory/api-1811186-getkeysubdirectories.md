# getKeySubdirectories

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn getKeySubdirectories(
 intkey,
 OSIterator *&iterator);
```

#### Return_value

kIOReturnSuccess if the iterator could be created

#### Overview

Creates an iterator over subdirectories of a given type of the directory.

## Parameters

- `key`: type of subdirectory to iterate over
- `iterator`: on return, set to point to an OSIterator

## See Also

- [getIndexEntry](ioconfigdirectory/1811146-getindexentry.md)
- [getIndexKey](ioconfigdirectory/1811157-getindexkey.md)
- [getIndexType](ioconfigdirectory/1811166-getindextype.md)
- [getIndexValue](ioconfigdirectory/1811176-getindexvalue.md)
- [getKeyType](ioconfigdirectory/1811199-getkeytype.md)
- [getKeyValue](ioconfigdirectory/1811212-getkeyvalue.md)
- [getSubdirectories](ioconfigdirectory/1811222-getsubdirectories.md)
- [update](ioconfigdirectory/1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811186-getkeysubdirectories)*