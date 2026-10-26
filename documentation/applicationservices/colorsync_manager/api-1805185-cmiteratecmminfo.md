# CMIterateCMMInfo

**Framework**: Application Services  
**Kind**: func

Iterates through the color management modules installed on the system.

## Declaration

```c
CMError CMIterateCMMInfo (
   CMMIterateUPP proc,
   UInt32 *count,
   void *refCon
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMIterateCMMInfo` function returns information for all CMMs installed on the system. The caller can pass nil for the `CMMIterateUPP` param to simply get a count of CMMs. If a `CMMIterateUPP` proc is provided, it is called once for each CMM installed - with the `CMMInfo` structure filled accordingly. The caller can pass a data reference to `CMIterateCMMInfo` which will then be passed to the `CMMIterateUPP`. This might be used to allow some of the information in the `CMMInfo` data structure to be put into a menu, for example, by passing a menu reference as the refcon. Either the proc or the count parameter must be provided. The caller will get a `paramErr` if both are nil.

## Parameters

- `proc`: A calling-program-supplied callback function that allows your application to monitor progress or abort the operation. 
- `count`: A pointer to the number of available CMMs. 
- `refCon`: A reference constant containing data specified by the calling application program. 

## See Also

### Working With CMMs
- [CMGetPreferredCMM](./api-1805182-cmgetpreferredcmm.md)
  Identifies the preferred CMM specified by the ColorSync control panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805185-cmiteratecmminfo)*