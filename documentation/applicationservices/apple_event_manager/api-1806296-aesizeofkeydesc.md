# AESizeOfKeyDesc

**Framework**: Application Services  
**Kind**: func

Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord`.

## Declaration

```c
OSErr AESizeOfKeyDesc (
   const AppleEvent *theAERecord,
   AEKeyword theAEKeyword,
   DescType *typeCode,
   Size *dataSize
);
```

#### Return Value

A result code. See [Result Codes](../apple_event_manager.md#1656145).

#### Overview

This function is declared as a macro that invokes [`AESizeOfParam`](../../coreservices/api-1449998-aesizeofparam.md), which can operate on an Apple event or an Apple event record. See the Discussion for that function for more information.

##### Version-Notes

See [`AESizeOfParam`](../../coreservices/api-1449998-aesizeofparam.md).

## Parameters

- `theAERecord`: A pointer to the Apple event record to get the parameter data from.
- `theAEKeyword`: The keyword that specifies the desired parameter. Some keyword parameter constants are described in [Keyword Parameter Constants](../../coreservices/api-1527206-keyword_parameter_constants.md). See [`AEKeyword`](../../coreservices/aekeyword.md).
- `typeCode`: A pointer to a descriptor type. On return, specifies the descriptor type of the Apple event parameter. For a list of AppleScript’s predefined descriptor types, see [Descriptor Type Constants](../../coreservices/api-1542788-descriptor_type_constants.md). See [`DescType`](../../coreservices/desctype.md).
- `dataSize`: A pointer to a size variable. On return, the length, in bytes, of the data in the Apple event parameter.

## See Also

### Getting the Sizes and Descriptor Types of Descriptors
- [AESizeOfAttribute](../../coreservices/api-1445764-aesizeofattribute.md)
  Gets the size and descriptor type of an Apple event attribute from a descriptor of type `AppleEvent`.
- [AESizeOfNthItem](../../coreservices/api-1447307-aesizeofnthitem.md)
  Gets the data size and descriptor type of the descriptor at a specified position in a descriptor list.
- [AESizeOfParam](../../coreservices/api-1449998-aesizeofparam.md)
  Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord` or `AppleEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1806296-aesizeofkeydesc)*