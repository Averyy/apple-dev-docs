# AEPutKeyDesc

**Framework**: Application Services  
**Kind**: func

Inserts a descriptor and a keyword into an Apple event record as an Apple event parameter.

## Declaration

```c
OSErr AEPutKeyDesc (
   AERecord *theAERecord,
   AEKeyword theAEKeyword,
   const AEDesc *theAEDesc
);
```

#### Return Value

A result code. See [Result Codes](../apple_event_manager.md#1656145).

#### Overview

This function is declared as a macro that invokes [`AEPutParamDesc`](../../coreservices/api-1447576-aeputparamdesc.md), which can operate on an Apple event or an Apple event record. See the Discussion for that function for more information.

##### Version-Notes

See [`AEPutParamDesc`](../../coreservices/api-1447576-aeputparamdesc.md).

## Parameters

- `theAERecord`: A pointer to the Apple event record to add a parameter to.
- `theAEKeyword`: The keyword specifying the parameter to add. If the Apple event record already has a parameter with this keyword, the parameter is replaced.

  Some keyword constants are described in [Keyword Parameter Constants](../../coreservices/api-1527206-keyword_parameter_constants.md).

  See [`AEKeyword`](../../coreservices/aekeyword.md).
- `theAEDesc`: A pointer to the descriptor for the parameter to add. See [`AEDesc`](../../coreservices/aedesc.md).

## See Also

### Adding Parameters and Attributes to Apple Events and Apple Event Records
- [AEPutAttributeDesc](../../coreservices/api-1441790-aeputattributedesc.md)
  Adds a descriptor and a keyword to an Apple event as an attribute.
- [AEPutAttributePtr](../../coreservices/api-1445940-aeputattributeptr.md)
  Adds a pointer to data, a descriptor type, and a keyword to an Apple event as an attribute.
- [AEPutKeyPtr](./api-1805645-aeputkeyptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event record as an Apple event parameter.
- [AEPutParamDesc](../../coreservices/api-1447576-aeputparamdesc.md)
  Inserts a descriptor and a keyword into an Apple event or Apple event record as an Apple event parameter.
- [AEPutParamPtr](../../coreservices/api-1449263-aeputparamptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event or Apple event record as an Apple event parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1805634-aeputkeydesc)*