# InvokeCMMIterateUPP

**Framework**: Application Services  
**Kind**: func

Invokes a universal procedure pointer (UPP) to a progress-monitoring callback for the [`CMIterateCMMInfo`](colorsync_manager/1805185-cmiteratecmminfo.md) function.

## Declaration

```swift
func InvokeCMMIterateUPP(_ iterateData: UnsafeMutablePointer<CMMInfo>, _ refCon: UnsafeMutablePointer<Void>, _ userUPP: CMMIterateUPP) -> OSErr
```

#### Overview

In most cases, you do not need to call this function as ColorSync Manager invokes your callback for you. See the [`CMMIterateProcPtr`](cmmiterateprocptr.md) callback for more information and for a description of the parameters.

## See Also

- [NewCMBitmapCallBackUPP](colorsync_manager/1805297-newcmbitmapcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a bitmap callback.
- [DisposeCMBitmapCallBackUPP](colorsync_manager/1805300-disposecmbitmapcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a bitmap callback.
- [InvokeCMBitmapCallBackUPP](colorsync_manager/1805303-invokecmbitmapcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a bitmap callback.
- [NewCMConcatCallBackUPP](colorsync_manager/1805306-newcmconcatcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a progress-monitoring callback.
- [DisposeCMConcatCallBackUPP](colorsync_manager/1805310-disposecmconcatcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a progress-monitoring callback.
- [InvokeCMConcatCallBackUPP](colorsync_manager/1805312-invokecmconcatcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback.
- [NewCMFlattenUPP](colorsync_manager/1805315-newcmflattenupp.md)
  Creates a new universal procedure pointer (UPP) to a data-flattening callback.
- [DisposeCMFlattenUPP](colorsync_manager/1805318-disposecmflattenupp.md)
  Disposes of a universal procedure pointer (UPP) to a data-flattening callback.
- [InvokeCMFlattenUPP](colorsync_manager/1805320-invokecmflattenupp.md)
  Invokes a universal procedure pointer (UPP) to a data-flattening callback.
- [NewCMMIterateUPP](colorsync_manager/1805322-newcmmiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a progress-monitoring callback for the `CMIterateCMMInfo` function.
- [DisposeCMMIterateUPP](colorsync_manager/1805323-disposecmmiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a progress-monitoring callback for the `CMIterateCMMInfo` function.
- [NewCMProfileIterateUPP](colorsync_manager/1805339-newcmprofileiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-iteration callback.
- [DisposeCMProfileIterateUPP](colorsync_manager/1805341-disposecmprofileiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-iteration callback.
- [InvokeCMProfileIterateUPP](colorsync_manager/1805343-invokecmprofileiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-iteration callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805325-invokecmmiterateupp)*