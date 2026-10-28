# AEGetKeyPtr

**Framework**: Application Services  
**Kind**: func

Gets a copy of the data for a specified Apple event parameter from an Apple event record.

## Declaration

```c
OSErr AEGetKeyPtr (
   AERecord *theAERecord,
   AEKeyword theAEKeyword,
   DescType desiredType,
   DescType *actualType,
   void *dataPtr,
   Size maximumSize,
   Size *actualSize
);
```

## Return Value

A result code. See [Result Codes](../apple_event_manager.md#1656145).

## Overview

This function is declared as a macro that invokes [`AEGetParamPtr`](../../coreservices/api-1444069-aegetparamptr.md), which can operate on an Apple event or an Apple event record. See the Discussion for that function for more information.

### Version-Notes

See [`AEGetParamPtr`](../../coreservices/api-1444069-aegetparamptr.md).

## Parameters

- `theAERecord`: A pointer to the Apple event record to get the parameter data from.
- `theAEKeyword`: The keyword that specifies the desired Apple event record parameter. Some keyword constants are described in [Keyword Parameter Constants](../../coreservices/api-1527206-keyword_parameter_constants.md).
- `desiredType`: The desired descriptor type for the copied data. For a list of AppleScript’s predefined descriptor types, see [Descriptor Type Constants](../../coreservices/api-1542788-descriptor_type_constants.md).

  If the descriptor specified by the `theAEKeyword` parameter is not of the desired type, `AEGetKeyPtr` attempts to coerce the data to this type. However, if the desired type is `typeWildCard`, no coercion is performed.

  On return, you can determine the actual descriptor type by examining the `typeCode` parameter.
- `typeCode`: A pointer to a descriptor type. On return, specifies the descriptor type of the data pointed to by `dataPtr`. The returned type is either the same as the type specified by the `desiredType` parameter or, if the desired type was type wildcard, the true type of the descriptor. Specify `NULL` if you do not care about this return value. For a list of AppleScript’s predefined descriptor types, see [Descriptor Type Constants](../../coreservices/api-1542788-descriptor_type_constants.md).
- `dataPtr`: A pointer to a buffer, local variable, or other storage location created and disposed of by your application. The size in bytes must be at least as large as the value you pass in the `maximumSize` parameter. On return, contains the parameter data. Specify `NULL` if you do not care about this return value. 
- `maximumSize`: The maximum length, in bytes, of the expected Apple event record parameter data. The `AEGetKeyPtr` function will not return more data than you specify in this parameter.
- `actualSize`: A pointer to a variable of type `Size`. On return, the length, in bytes, of the data for the specified Apple event record parameter. If this value is larger than the value you passed in the `maximumSize` parameter, the buffer pointed to by `dataPtr` was not large enough to contain all of the data for the parameter, though `AEGetKeyPtr` does not write beyond the end of the buffer. If the buffer was too small, you can resize it and call `AEGetKeyPtr` again. Specify `NULL` if you do not care about this return value.

## See Also

### Getting Data or Descriptors From Apple Events and Apple Event Records
- [AEGetAttributeDesc](../../coreservices/api-1450314-aegetattributedesc.md)
  Gets a copy of the descriptor for a specified Apple event attribute from an Apple event; typically used when your application needs to pass the descriptor on to another function.
- [AEGetAttributePtr](../../coreservices/api-1445109-aegetattributeptr.md)
  Gets a copy of the data for a specified Apple event attribute from an Apple event; typically used when your application needs to work with the data directly.
- [AEGetKeyDesc](./api-1806211-aegetkeydesc.md)
  Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event record
- [AEGetParamDesc](../../coreservices/api-1449233-aegetparamdesc.md)
  Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event or an Apple event record.
- [AEGetParamPtr](../../coreservices/api-1444069-aegetparamptr.md)
  Gets a copy of the data for a specified Apple event parameter from an Apple event or an Apple event record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1806223-aegetkeyptr)*