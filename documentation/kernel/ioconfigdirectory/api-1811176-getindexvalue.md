# getIndexValue

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn getIndexValue(
 inttype,
 UInt32 &value);
```

#### Return Value

kIOReturnSuccess if the index exists in the dictionary and is of a type appropriate for the value parameter

#### Overview

Gets the value at the specified index of the directory, in a variety of forms.

## Parameters

- `type`: on return, set to the data type
- `value`: reference to variable to store the entry's value

## See Also

### Miscellaneous
- [getIndexEntry](./api-1811146-getindexentry.md)
- [getIndexKey](./api-1811157-getindexkey.md)
- [getIndexType](./api-1811166-getindextype.md)
- [getKeySubdirectories](./api-1811186-getkeysubdirectories.md)
- [getKeyType](./api-1811199-getkeytype.md)
- [getKeyValue](./api-1811212-getkeyvalue.md)
- [getSubdirectories](./api-1811222-getsubdirectories.md)
- [update](./api-1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811176-getindexvalue)*