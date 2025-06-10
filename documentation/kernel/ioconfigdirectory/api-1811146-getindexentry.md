# getIndexEntry

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn getIndexEntry(
 intentry,
 UInt32 &value);
```

#### Return_value

kIOReturnSuccess if the index exists in the dictionary

#### Overview

Gets the entry at the specified index of the directory, as a raw UInt32.

## Parameters

- `entry`: on return, set to the entry value
- `value`: reference to variable to store the entry's value

## See Also

- [getIndexKey](ioconfigdirectory/1811157-getindexkey.md)
- [getIndexType](ioconfigdirectory/1811166-getindextype.md)
- [getIndexValue](ioconfigdirectory/1811176-getindexvalue.md)
- [getKeySubdirectories](ioconfigdirectory/1811186-getkeysubdirectories.md)
- [getKeyType](ioconfigdirectory/1811199-getkeytype.md)
- [getKeyValue](ioconfigdirectory/1811212-getkeyvalue.md)
- [getSubdirectories](ioconfigdirectory/1811222-getsubdirectories.md)
- [update](ioconfigdirectory/1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811146-getindexentry)*