# AEDeleteKeyDesc

**Framework**: Application Services  
**Kind**: func

Deletes a keyword-specified parameter from an Apple event record.

## Declaration

```c
OSErr AEDeleteKeyDesc (
   AERecord *theAERecord,
   AEKeyword theAEKeyword
);
```

## Return Value

A result code. See [Result Codes](../apple_event_manager.md#1656145).

## Overview

This function is declared as a macro that invokes [`AEDeleteParam`](../../coreservices/api-1444338-aedeleteparam.md), which can operate on an Apple event or an Apple event record. See the Discussion for that function for more information.

### Version-Notes

See [`AEDeleteParam`](../../coreservices/api-1444338-aedeleteparam.md).

## Parameters

- `theAERecord`: A pointer to the Apple event record to delete the parameter from.
- `theAEKeyword`: The keyword that specifies the parameter to delete. Some keyword constants are described in [Keyword Parameter Constants](../../coreservices/api-1527206-keyword_parameter_constants.md). See [`AEKeyword`](../../coreservices/aekeyword.md).

## See Also

### Deleting Descriptors
- [AEDeleteItem](../../coreservices/api-1447164-aedeleteitem.md)
  Deletes a descriptor from a descriptor list, causing all subsequent descriptors to move up one place. 
- [AEDeleteParam](../../coreservices/api-1444338-aedeleteparam.md)
  Deletes a keyword-specified parameter from an Apple event record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1806085-aedeletekeydesc)*