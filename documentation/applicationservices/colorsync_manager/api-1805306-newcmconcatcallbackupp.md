# NewCMConcatCallBackUPP

**Framework**: Application Services  
**Kind**: func

Creates a new universal procedure pointer (UPP) to a progress-monitoring callback.

## Declaration

```swift
func NewCMConcatCallBackUPP(_ userRoutine: CMConcatCallBackProcPtr) -> CMConcatCallBackUPP
```

```c
CMConcatCallBackUPP NewCMConcatCallBackUPP (
   CMConcatCallBackProcPtr userRoutine
);
```

#### Return Value

The universal procedure pointer.

#### Overview

The callback protects against the appearance of a stalled machine during lengthy color world processing. If a CMM takes more than several seconds to process the information and create a color world, it will call the callback, if one is provided, and pass it the `refCon` provided. Passed to the functions `NCWNewLinkProfile` or `NCWConcatColorWorld` function .

## Parameters

- `userRoutine`: A pointer to your progress-monitoring callback function.

## See Also

### Working With Universal Procedure Pointers
- [NewCMBitmapCallBackUPP](./api-1805297-newcmbitmapcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a bitmap callback.
- [DisposeCMBitmapCallBackUPP](./api-1805300-disposecmbitmapcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a bitmap callback.
- [InvokeCMBitmapCallBackUPP](./api-1805303-invokecmbitmapcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a bitmap callback.
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
- [InvokeCMMIterateUPP](./api-1805325-invokecmmiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback for the [CMIterateCMMInfo](./api-1805185-cmiteratecmminfo.md) function.
- [NewCMProfileIterateUPP](./api-1805339-newcmprofileiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-iteration callback.
- [DisposeCMProfileIterateUPP](./api-1805341-disposecmprofileiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-iteration callback.
- [InvokeCMProfileIterateUPP](./api-1805343-invokecmprofileiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-iteration callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805306-newcmconcatcallbackupp)*