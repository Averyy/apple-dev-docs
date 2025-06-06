# NewOSLMarkUPP(_:)

**Framework**: Core Services  
**Kind**: func

Creates a new universal procedure pointer to an object callback mark function.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func NewOSLMarkUPP(_ userRoutine: OSLMarkProcPtr!) -> OSLMarkUPP!
```

#### Return_value

See [`OSLMarkUPP`](oslmarkupp.md).

#### Discussion

See the [`OSLMarkProcPtr`](oslmarkprocptr.md) callback function. 

## See Also

- [func DisposeAECoerceDescUPP(AECoerceDescUPP!)](1448721-disposeaecoercedescupp.md)
  Disposes of a universal procedure pointer to a function that coerces data stored in a descriptor.
- [func DisposeAECoercePtrUPP(AECoercePtrUPP!)](1450664-disposeaecoerceptrupp.md)
  Disposes of a universal procedure pointer to a function that coerces data stored in a buffer.
- [func DisposeAEDisposeExternalUPP(AEDisposeExternalUPP!)](1447284-disposeaedisposeexternalupp.md)
  Disposes of a universal procedure pointer to a function that disposes of data supplied to the `AECreateDescFromExternalPtr` function.
- [func DisposeAEEventHandlerUPP(AEEventHandlerUPP!)](1442066-disposeaeeventhandlerupp.md)
  Disposes of a universal procedure pointer to an event handler function.
- [func DisposeOSLAccessorUPP(OSLAccessorUPP!)](1444684-disposeoslaccessorupp.md)
  Disposes of a universal procedure pointer to an object accessor function.
- [func DisposeOSLAdjustMarksUPP(OSLAdjustMarksUPP!)](1443940-disposeosladjustmarksupp.md)
  Disposes of a universal procedure pointer to an object callback adjust marks function.
- [func DisposeOSLCompareUPP(OSLCompareUPP!)](1448398-disposeoslcompareupp.md)
  Disposes of a universal procedure pointer to an object callback comparison function.
- [func DisposeOSLCountUPP(OSLCountUPP!)](1443984-disposeoslcountupp.md)
  Disposes of a universal procedure pointer to an object callback count function.
- [func DisposeOSLDisposeTokenUPP(OSLDisposeTokenUPP!)](1442670-disposeosldisposetokenupp.md)
  Disposes of a universal procedure pointer to an object callback dispose token function.
- [func DisposeOSLGetErrDescUPP(OSLGetErrDescUPP!)](1446061-disposeoslgeterrdescupp.md)
  Disposes of a universal procedure pointer to an object callback get error descriptor function.
- [func DisposeOSLGetMarkTokenUPP(OSLGetMarkTokenUPP!)](1442377-disposeoslgetmarktokenupp.md)
  Disposes of a universal procedure pointer to an object callback get mark function.
- [func DisposeOSLMarkUPP(OSLMarkUPP!)](1449253-disposeoslmarkupp.md)
  Disposes of a universal procedure pointer to an object callback mark function.
- [func InvokeAECoerceDescUPP(UnsafePointer<AEDesc>!, DescType, SRefCon!, UnsafeMutablePointer<AEDesc>!, AECoerceDescUPP!) -> OSErr](1445450-invokeaecoercedescupp.md)
  Calls a universal procedure pointer to a function that coerces data stored in a descriptor.
- [func InvokeAECoercePtrUPP(DescType, UnsafeRawPointer!, Size, DescType, SRefCon!, UnsafeMutablePointer<AEDesc>!, AECoercePtrUPP!) -> OSErr](1447079-invokeaecoerceptrupp.md)
  Calls a universal procedure pointer to a function that coerces data stored in a buffer.
- [func InvokeAEDisposeExternalUPP(UnsafeRawPointer!, Size, SRefCon!, AEDisposeExternalUPP!)](1441717-invokeaedisposeexternalupp.md)
  Calls a dispose external universal procedure pointer.
- [func InvokeAEEventHandlerUPP(UnsafePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!, SRefCon!, AEEventHandlerUPP!) -> OSErr](1446585-invokeaeeventhandlerupp.md)
  Calls an event handler universal procedure pointer.
- [func InvokeOSLAccessorUPP(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, SRefCon!, OSLAccessorUPP!) -> OSErr](1448978-invokeoslaccessorupp.md)
  Calls an object accessor universal procedure pointer.
- [func InvokeOSLAdjustMarksUPP(Int, Int, UnsafePointer<AEDesc>!, OSLAdjustMarksUPP!) -> OSErr](1448506-invokeosladjustmarksupp.md)
  Calls an object callback adjust marks universal procedure pointer.
- [func InvokeOSLCompareUPP(DescType, UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, UnsafeMutablePointer<DarwinBoolean>!, OSLCompareUPP!) -> OSErr](1443110-invokeoslcompareupp.md)
  Calls an object callback comparison universal procedure pointer.
- [func InvokeOSLCountUPP(DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<Int>!, OSLCountUPP!) -> OSErr](1448030-invokeoslcountupp.md)
  Calls an object callback count universal procedure pointer.
- [func InvokeOSLDisposeTokenUPP(UnsafeMutablePointer<AEDesc>!, OSLDisposeTokenUPP!) -> OSErr](1443963-invokeosldisposetokenupp.md)
  Calls an object callback dispose token universal procedure pointer.
- [func InvokeOSLGetErrDescUPP(UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>?>!, OSLGetErrDescUPP!) -> OSErr](1448420-invokeoslgeterrdescupp.md)
  Calls an object callback get error descriptor universal procedure pointer.
- [func InvokeOSLGetMarkTokenUPP(UnsafePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, OSLGetMarkTokenUPP!) -> OSErr](1441894-invokeoslgetmarktokenupp.md)
  Calls an object callback get mark universal procedure pointer.
- [func InvokeOSLMarkUPP(UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, Int, OSLMarkUPP!) -> OSErr](1447444-invokeoslmarkupp.md)
  Calls an object callback mark universal procedure pointer.
- [func NewAECoerceDescUPP(AECoerceDescProcPtr!) -> AECoerceDescUPP!](1445885-newaecoercedescupp.md)
  Creates a new universal procedure pointer to a function that coerces data stored in a descriptor.
- [func NewAECoercePtrUPP(AECoercePtrProcPtr!) -> AECoercePtrUPP!](1449962-newaecoerceptrupp.md)
  Creates a new universal procedure pointer to a function that coerces data stored in a buffer.
- [func NewAEDisposeExternalUPP(AEDisposeExternalProcPtr!) -> AEDisposeExternalUPP!](1447774-newaedisposeexternalupp.md)
  Creates a new universal procedure pointer to a function that disposes of data stored in a buffer.
- [func NewAEEventHandlerUPP(AEEventHandlerProcPtr!) -> AEEventHandlerUPP!](1446862-newaeeventhandlerupp.md)
  Creates a new universal procedure pointer to an event handler function.
- [func NewOSLAccessorUPP(OSLAccessorProcPtr!) -> OSLAccessorUPP!](1449584-newoslaccessorupp.md)
  Creates a new universal procedure pointer to an object accessor function.
- [func NewOSLAdjustMarksUPP(OSLAdjustMarksProcPtr!) -> OSLAdjustMarksUPP!](1443347-newosladjustmarksupp.md)
  Creates a new universal procedure pointer to an object callback adjust marks function.
- [func NewOSLCompareUPP(OSLCompareProcPtr!) -> OSLCompareUPP!](1444603-newoslcompareupp.md)
  Creates a new universal procedure pointer to an object callback comparison function.
- [func NewOSLCountUPP(OSLCountProcPtr!) -> OSLCountUPP!](1448156-newoslcountupp.md)
  Creates a new universal procedure pointer to an object callback count function.
- [func NewOSLDisposeTokenUPP(OSLDisposeTokenProcPtr!) -> OSLDisposeTokenUPP!](1450027-newosldisposetokenupp.md)
  Creates a new universal procedure pointer to an object callback dispose token function.
- [func NewOSLGetErrDescUPP(OSLGetErrDescProcPtr!) -> OSLGetErrDescUPP!](1447934-newoslgeterrdescupp.md)
  Creates a new universal procedure pointer to an object callback get error descriptor function.
- [func NewOSLGetMarkTokenUPP(OSLGetMarkTokenProcPtr!) -> OSLGetMarkTokenUPP!](1445166-newoslgetmarktokenupp.md)
  Creates a new universal procedure pointer to an object callback get mark function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446942-newoslmarkupp)*