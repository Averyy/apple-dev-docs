# getIndexValue

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn getIndexValue(
 inttype,
 UInt32 &value);
```

#### Return_value

kIOReturnSuccess if the index exists in the dictionary and is of a type appropriate for the value parameter

#### Overview

Gets the value at the specified index of the directory, in a variety of forms.

## Parameters

- `type`: on return, set to the data type
- `value`: reference to variable to store the entry's value

## See Also

- [getIndexEntry](ioconfigdirectory/1811146-getindexentry.md)
- [getIndexKey](ioconfigdirectory/1811157-getindexkey.md)
- [getIndexType](ioconfigdirectory/1811166-getindextype.md)
- [getKeySubdirectories](ioconfigdirectory/1811186-getkeysubdirectories.md)
- [getKeyType](ioconfigdirectory/1811199-getkeytype.md)
- [getKeyValue](ioconfigdirectory/1811212-getkeyvalue.md)
- [getSubdirectories](ioconfigdirectory/1811222-getsubdirectories.md)
- [update](ioconfigdirectory/1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811176-getindexvalue)*