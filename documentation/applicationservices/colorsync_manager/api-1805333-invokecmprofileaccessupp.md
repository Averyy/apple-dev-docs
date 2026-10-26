# InvokeCMProfileAccessUPP

**Framework**: Application Services  
**Kind**: func

Invokes a universal procedure pointer (UPP) to a profile-access callback.

## Declaration

```c
OSErr InvokeCMProfileAccessUPP (
   SInt32 command,
   SInt32 offset,
   SInt32 *size,
   void *data,
   void *refCon,
   CMProfileAccessUPP userUPP
);
```

#### Overview

In most cases, you do not need to call this function as ColorSync Manager invokes your callback for you. See the `CMProfileAccessProcPtr` callback for more information and for a description of the parameters.

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
- [InvokeCMMIterateUPP](./api-1805325-invokecmmiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback for the [CMIterateCMMInfo](./api-1805185-cmiteratecmminfo.md) function.
- [NewCMProfileAccessUPP](./api-1805327-newcmprofileaccessupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-access callback.
- [DisposeCMProfileAccessUPP](./api-1805329-disposecmprofileaccessupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-access callback.
- [NewCMProfileFilterUPP](./api-1805336-newcmprofilefilterupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-filter callback.
- [DisposeCMProfileFilterUPP](./api-1805337-disposecmprofilefilterupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-filter callback.
- [InvokeCMProfileFilterUPP](./api-1805338-invokecmprofilefilterupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-filter callback.
- [NewCMProfileIterateUPP](./api-1805339-newcmprofileiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-iteration callback.
- [DisposeCMProfileIterateUPP](./api-1805341-disposecmprofileiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-iteration callback.
- [InvokeCMProfileIterateUPP](./api-1805343-invokecmprofileiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-iteration callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805333-invokecmprofileaccessupp)*