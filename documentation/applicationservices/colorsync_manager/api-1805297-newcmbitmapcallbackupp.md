# NewCMBitmapCallBackUPP

**Framework**: Application Services  
**Kind**: func

Creates a new universal procedure pointer (UPP) to a bitmap callback.

## Declaration

```swift
func NewCMBitmapCallBackUPP(_ userRoutine: CMBitmapCallBackProcPtr) -> CMBitmapCallBackUPP
```

#### Return_value

The universal procedure pointer.

## Parameters

- `userRoutine`: A pointer to your bitmap callback function.

## See Also

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
- [InvokeCMMIterateUPP](colorsync_manager/1805325-invokecmmiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback for the [`CMIterateCMMInfo`](colorsync_manager/1805185-cmiteratecmminfo.md) function.
- [NewCMProfileIterateUPP](colorsync_manager/1805339-newcmprofileiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-iteration callback.
- [DisposeCMProfileIterateUPP](colorsync_manager/1805341-disposecmprofileiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-iteration callback.
- [InvokeCMProfileIterateUPP](colorsync_manager/1805343-invokecmprofileiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-iteration callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805297-newcmbitmapcallbackupp)*