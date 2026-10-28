# AEGetKeyDesc

**Framework**: Application Services  
**Kind**: func

Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event record

## Declaration

```c
OSErr AEGetKeyDesc (
   AERecord *theAERecord,
   AEKeyword theAEKeyword,
   DescType desiredType,
   AEDesc *result
);
```

## Return Value

A result code. See [Result Codes](../apple_event_manager.md#1656145).

## Overview

This function is declared as a macro that invokes [`AEGetParamDesc`](../../coreservices/api-1449233-aegetparamdesc.md), which can operate on an Apple event or an Apple event record. See the Discussion for that function for more information.

### Version-Notes

See [`AEGetParamDesc`](../../coreservices/api-1449233-aegetparamdesc.md).

## Parameters

- `theAERecord`: A pointer to the Apple event record to get the parameter descriptor from.
- `theAEKeyword`: A keyword that specifies the desired Apple event parameter. Some keyword constants are described in [Keyword Parameter Constants](../../coreservices/api-1527206-keyword_parameter_constants.md). See [`AEKeyword`](../../coreservices/aekeyword.md).
- `desiredType`: The descriptor type for the desired Apple event parameter. For a list of AppleScript’s predefined descriptor types, see [Descriptor Type Constants](../../coreservices/api-1542788-descriptor_type_constants.md).

  If the requested Apple event parameter is not of the desired type, the Apple Event Manager attempts to coerce it to the desired type. However, if you pass a value of `typeWildCard`, no coercion is performed, and the descriptor type of the returned descriptor is the same as the descriptor type of the Apple event parameter.

  See [`DescType`](../../coreservices/desctype.md).
- `result`: A pointer to a descriptor. On successful return, a copy of the descriptor for the specified Apple event parameter, coerced, if necessary, to the descriptor type specified by the `desiredType` parameter. On error, a null descriptor. If the function returns successfully, your application should call the [`AEDisposeDesc`](../../coreservices/api-1444208-aedisposedesc.md) function to dispose of the resulting descriptor after it has finished using it. See [`AEDesc`](../../coreservices/aedesc.md).

## See Also

### Getting Data or Descriptors From Apple Events and Apple Event Records
- [AEGetAttributeDesc](../../coreservices/api-1450314-aegetattributedesc.md)
  Gets a copy of the descriptor for a specified Apple event attribute from an Apple event; typically used when your application needs to pass the descriptor on to another function.
- [AEGetAttributePtr](../../coreservices/api-1445109-aegetattributeptr.md)
  Gets a copy of the data for a specified Apple event attribute from an Apple event; typically used when your application needs to work with the data directly.
- [AEGetKeyPtr](./api-1806223-aegetkeyptr.md)
  Gets a copy of the data for a specified Apple event parameter from an Apple event record.
- [AEGetParamDesc](../../coreservices/api-1449233-aegetparamdesc.md)
  Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event or an Apple event record.
- [AEGetParamPtr](../../coreservices/api-1444069-aegetparamptr.md)
  Gets a copy of the data for a specified Apple event parameter from an Apple event or an Apple event record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1806211-aegetkeydesc)*