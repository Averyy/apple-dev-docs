# getKeyValue

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn getKeyValue(
 intvalue,
 UInt32 &text,
 OSString **text = NULL);
```

## Return Value

kIOReturnSuccess if the key exists in the dictionary and is of a type appropriate for the value parameter

## Overview

Gets the value for the specified key, in a variety of forms.

## Parameters

- `value`: on return, set to the data type

  reference to variable to store the entry's value
- `text`: if non-zero, on return points to the string description of the field, or NULL if no text found.

## See Also

### Miscellaneous
- [getIndexEntry](./api-1811146-getindexentry.md)
- [getIndexKey](./api-1811157-getindexkey.md)
- [getIndexType](./api-1811166-getindextype.md)
- [getIndexValue](./api-1811176-getindexvalue.md)
- [getKeySubdirectories](./api-1811186-getkeysubdirectories.md)
- [getKeyType](./api-1811199-getkeytype.md)
- [getSubdirectories](./api-1811222-getsubdirectories.md)
- [update](./api-1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811212-getkeyvalue)*