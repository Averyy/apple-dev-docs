# getKeyValue

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn getKeyValue(
 intvalue,
 UInt32 &text,
 OSString **text = NULL);
```

#### Return_value

kIOReturnSuccess if the key exists in the dictionary and is of a type appropriate for the value parameter

#### Overview

Gets the value for the specified key, in a variety of forms.

## Parameters

- `value`: reference to variable to store the entry's value
- `text`: if non-zero, on return points to the string description of the field, or NULL if no text found.

## See Also

- [getIndexEntry](ioconfigdirectory/1811146-getindexentry.md)
- [getIndexKey](ioconfigdirectory/1811157-getindexkey.md)
- [getIndexType](ioconfigdirectory/1811166-getindextype.md)
- [getIndexValue](ioconfigdirectory/1811176-getindexvalue.md)
- [getKeySubdirectories](ioconfigdirectory/1811186-getkeysubdirectories.md)
- [getKeyType](ioconfigdirectory/1811199-getkeytype.md)
- [getSubdirectories](ioconfigdirectory/1811222-getsubdirectories.md)
- [update](ioconfigdirectory/1811231-update.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioconfigdirectory/1811212-getkeyvalue)*