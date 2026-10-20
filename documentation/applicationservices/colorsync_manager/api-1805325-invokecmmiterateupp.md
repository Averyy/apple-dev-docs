# InvokeCMMIterateUPP

**Framework**: Application Services  
**Kind**: func

Invokes a universal procedure pointer (UPP) to a progress-monitoring callback for the [CMIterateCMMInfo](./api-1805185-cmiteratecmminfo.md) function.

## Declaration

```swift
func InvokeCMMIterateUPP(_ iterateData: UnsafeMutablePointer<CMMInfo>, _ refCon: UnsafeMutablePointer<Void>, _ userUPP: CMMIterateUPP) -> OSErr
```

```c
OSErr InvokeCMMIterateUPP (
   CMMInfo *iterateData,
   void *refCon,
   CMMIterateUPP userUPP
);
```

#### Overview

In most cases, you do not need to call this function as ColorSync Manager invokes your callback for you. See the [`CMMIterateProcPtr`](../cmmiterateprocptr.md) callback for more information and for a description of the parameters.

## See Also

### Working With Universal Procedure Pointers
- [NewCMBitmapCallBackUPP](./api-1805297-newcmbitmapcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a bitmap callback.
- [DisposeCMBitmapCallBackUPP](./api-1805300-disposecmbitmapcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a bitmap callback.
- [InvokeCMBitmapCallBackUPP](./api-1805303-invokecmbitmapcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a bitmap callback.
- [NewCMConcatCallBackUPP](./api-1805306-newcmconcatcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a progress-monitoring callback.
- [DisposeCMConcatCallBackUPP](./api-1805310-disposecmconcatcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a progress-monitoring callback.
- [InvokeCMConcatCallBackUPP](./api-1805312-invokecmconcatcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback.
- [NewCMFlattenUPP](./api-1805315-newcmflattenupp.md)
  Creates a new universal procedure pointer (UPP) to a data-flattening callback.
- [DisposeCMFlattenUPP](./api-1805318-disposecmflattenupp.md)
  Disposes of a universal procedure pointer (UPP) to a data-flattening callback.
- [InvokeCMFlattenUPP](./api-1805320-invokecmflattenupp.md)
  Invokes a universal procedure pointer (UPP) to a data-flattening callback.
- [NewCMMIterateUPP](./api-1805322-newcmmiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a progress-monitoring callback for the `CMIterateCMMInfo` function.
- [DisposeCMMIterateUPP](./api-1805323-disposecmmiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a progress-monitoring callback for the `CMIterateCMMInfo` function.
- [NewCMProfileIterateUPP](./api-1805339-newcmprofileiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-iteration callback.
- [DisposeCMProfileIterateUPP](./api-1805341-disposecmprofileiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-iteration callback.
- [InvokeCMProfileIterateUPP](./api-1805343-invokecmprofileiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-iteration callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805325-invokecmmiterateupp)*