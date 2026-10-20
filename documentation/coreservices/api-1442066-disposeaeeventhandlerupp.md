# DisposeAEEventHandlerUPP(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Disposes of a universal procedure pointer to an event handler function.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func DisposeAEEventHandlerUPP(_ userUPP: AEEventHandlerUPP!)
```

```c
void DisposeAEEventHandlerUPP(AEEventHandlerUPP userUPP);
```

#### Discussion

See the [`AEEventHandlerProcPtr`](./aeeventhandlerprocptr.md) callback function. 

## See Also

### Creating, Calling, and Deleting Universal Procedure Pointers
- [func DisposeAECoerceDescUPP(AECoerceDescUPP!)](./api-1448721-disposeaecoercedescupp.md)
  Disposes of a universal procedure pointer to a function that coerces data stored in a descriptor.
- [func DisposeAECoercePtrUPP(AECoercePtrUPP!)](./api-1450664-disposeaecoerceptrupp.md)
  Disposes of a universal procedure pointer to a function that coerces data stored in a buffer.
- [func DisposeAEDisposeExternalUPP(AEDisposeExternalUPP!)](./api-1447284-disposeaedisposeexternalupp.md)
  Disposes of a universal procedure pointer to a function that disposes of data supplied to the `AECreateDescFromExternalPtr` function.
- [func DisposeOSLAccessorUPP(OSLAccessorUPP!)](./api-1444684-disposeoslaccessorupp.md)
  Disposes of a universal procedure pointer to an object accessor function.
- [func DisposeOSLAdjustMarksUPP(OSLAdjustMarksUPP!)](./api-1443940-disposeosladjustmarksupp.md)
  Disposes of a universal procedure pointer to an object callback adjust marks function.
- [func DisposeOSLCompareUPP(OSLCompareUPP!)](./api-1448398-disposeoslcompareupp.md)
  Disposes of a universal procedure pointer to an object callback comparison function.
- [func DisposeOSLCountUPP(OSLCountUPP!)](./api-1443984-disposeoslcountupp.md)
  Disposes of a universal procedure pointer to an object callback count function.
- [func DisposeOSLDisposeTokenUPP(OSLDisposeTokenUPP!)](./api-1442670-disposeosldisposetokenupp.md)
  Disposes of a universal procedure pointer to an object callback dispose token function.
- [func DisposeOSLGetErrDescUPP(OSLGetErrDescUPP!)](./api-1446061-disposeoslgeterrdescupp.md)
  Disposes of a universal procedure pointer to an object callback get error descriptor function.
- [func DisposeOSLGetMarkTokenUPP(OSLGetMarkTokenUPP!)](./api-1442377-disposeoslgetmarktokenupp.md)
  Disposes of a universal procedure pointer to an object callback get mark function.
- [func DisposeOSLMarkUPP(OSLMarkUPP!)](./api-1449253-disposeoslmarkupp.md)
  Disposes of a universal procedure pointer to an object callback mark function.
- [func InvokeAECoerceDescUPP(UnsafePointer<AEDesc>!, DescType, SRefCon!, UnsafeMutablePointer<AEDesc>!, AECoerceDescUPP!) -> OSErr](./api-1445450-invokeaecoercedescupp.md)
  Calls a universal procedure pointer to a function that coerces data stored in a descriptor.
- [func InvokeAECoercePtrUPP(DescType, UnsafeRawPointer!, Size, DescType, SRefCon!, UnsafeMutablePointer<AEDesc>!, AECoercePtrUPP!) -> OSErr](./api-1447079-invokeaecoerceptrupp.md)
  Calls a universal procedure pointer to a function that coerces data stored in a buffer.
- [func InvokeAEDisposeExternalUPP(UnsafeRawPointer!, Size, SRefCon!, AEDisposeExternalUPP!)](./api-1441717-invokeaedisposeexternalupp.md)
  Calls a dispose external universal procedure pointer.
- [func InvokeAEEventHandlerUPP(UnsafePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!, SRefCon!, AEEventHandlerUPP!) -> OSErr](./api-1446585-invokeaeeventhandlerupp.md)
  Calls an event handler universal procedure pointer.
- [func InvokeOSLAccessorUPP(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, SRefCon!, OSLAccessorUPP!) -> OSErr](./api-1448978-invokeoslaccessorupp.md)
  Calls an object accessor universal procedure pointer.
- [func InvokeOSLAdjustMarksUPP(Int, Int, UnsafePointer<AEDesc>!, OSLAdjustMarksUPP!) -> OSErr](./api-1448506-invokeosladjustmarksupp.md)
  Calls an object callback adjust marks universal procedure pointer.
- [func InvokeOSLCompareUPP(DescType, UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, UnsafeMutablePointer<DarwinBoolean>!, OSLCompareUPP!) -> OSErr](./api-1443110-invokeoslcompareupp.md)
  Calls an object callback comparison universal procedure pointer.
- [func InvokeOSLCountUPP(DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<Int>!, OSLCountUPP!) -> OSErr](./api-1448030-invokeoslcountupp.md)
  Calls an object callback count universal procedure pointer.
- [func InvokeOSLDisposeTokenUPP(UnsafeMutablePointer<AEDesc>!, OSLDisposeTokenUPP!) -> OSErr](./api-1443963-invokeosldisposetokenupp.md)
  Calls an object callback dispose token universal procedure pointer.
- [func InvokeOSLGetErrDescUPP(UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>?>!, OSLGetErrDescUPP!) -> OSErr](./api-1448420-invokeoslgeterrdescupp.md)
  Calls an object callback get error descriptor universal procedure pointer.
- [func InvokeOSLGetMarkTokenUPP(UnsafePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, OSLGetMarkTokenUPP!) -> OSErr](./api-1441894-invokeoslgetmarktokenupp.md)
  Calls an object callback get mark universal procedure pointer.
- [func InvokeOSLMarkUPP(UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, Int, OSLMarkUPP!) -> OSErr](./api-1447444-invokeoslmarkupp.md)
  Calls an object callback mark universal procedure pointer.
- [func NewAECoerceDescUPP(AECoerceDescProcPtr!) -> AECoerceDescUPP!](./api-1445885-newaecoercedescupp.md)
  Creates a new universal procedure pointer to a function that coerces data stored in a descriptor.
- [func NewAECoercePtrUPP(AECoercePtrProcPtr!) -> AECoercePtrUPP!](./api-1449962-newaecoerceptrupp.md)
  Creates a new universal procedure pointer to a function that coerces data stored in a buffer.
- [func NewAEDisposeExternalUPP(AEDisposeExternalProcPtr!) -> AEDisposeExternalUPP!](./api-1447774-newaedisposeexternalupp.md)
  Creates a new universal procedure pointer to a function that disposes of data stored in a buffer.
- [func NewAEEventHandlerUPP(AEEventHandlerProcPtr!) -> AEEventHandlerUPP!](./api-1446862-newaeeventhandlerupp.md)
  Creates a new universal procedure pointer to an event handler function.
- [func NewOSLAccessorUPP(OSLAccessorProcPtr!) -> OSLAccessorUPP!](./api-1449584-newoslaccessorupp.md)
  Creates a new universal procedure pointer to an object accessor function.
- [func NewOSLAdjustMarksUPP(OSLAdjustMarksProcPtr!) -> OSLAdjustMarksUPP!](./api-1443347-newosladjustmarksupp.md)
  Creates a new universal procedure pointer to an object callback adjust marks function.
- [func NewOSLCompareUPP(OSLCompareProcPtr!) -> OSLCompareUPP!](./api-1444603-newoslcompareupp.md)
  Creates a new universal procedure pointer to an object callback comparison function.
- [func NewOSLCountUPP(OSLCountProcPtr!) -> OSLCountUPP!](./api-1448156-newoslcountupp.md)
  Creates a new universal procedure pointer to an object callback count function.
- [func NewOSLDisposeTokenUPP(OSLDisposeTokenProcPtr!) -> OSLDisposeTokenUPP!](./api-1450027-newosldisposetokenupp.md)
  Creates a new universal procedure pointer to an object callback dispose token function.
- [func NewOSLGetErrDescUPP(OSLGetErrDescProcPtr!) -> OSLGetErrDescUPP!](./api-1447934-newoslgeterrdescupp.md)
  Creates a new universal procedure pointer to an object callback get error descriptor function.
- [func NewOSLGetMarkTokenUPP(OSLGetMarkTokenProcPtr!) -> OSLGetMarkTokenUPP!](./api-1445166-newoslgetmarktokenupp.md)
  Creates a new universal procedure pointer to an object callback get mark function.
- [func NewOSLMarkUPP(OSLMarkProcPtr!) -> OSLMarkUPP!](./api-1446942-newoslmarkupp.md)
  Creates a new universal procedure pointer to an object callback mark function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442066-disposeaeeventhandlerupp)*