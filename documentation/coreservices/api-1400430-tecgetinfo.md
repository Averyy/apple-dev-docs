# TECGetInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Allocates a converter information structure of type `TECInfo` inthe application heap using `NewHandle`,fills it out, and returns a handle. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECGetInfo(TECInfoHandle *tecInfo);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324). This function canreturn memory errors.

## Discussion

When you are finished with the handle, your application mustdispose of it using `DisposeHandle`.You must also perform any required preflighting or memory rearrangementbefore calling `TECGetInfo`. 

## Parameters

- `tecInfo`: A handle to a structure of type [`TECInfo`](./tecinfo.md) containing information about the converter. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400430-tecgetinfo)*