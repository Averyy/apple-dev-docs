# CMGetPreferredCMM

**Framework**: Application Services  
**Kind**: func

Identifies the preferred CMM specified by the ColorSync control panel.

## Declaration

```c
CMError CMGetPreferredCMM (
   OSType *cmmType,
   Boolean *prefCMMnotfound
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMGetPreferredCMM` function returns in the `cmmType` parameter a value that identifies the preferred CMM the user last specified in the ColorSync control panel. `CMGetPreferredCMM` returns `false` in the `preferredCMMnotfound` parameter if the preferred CMM is currently available and `true` if it is not. The preferred CMM may not be available, for example, because a user specifies a preferred CMM in the ColorSync control panel, then reboots with extensions off. ColorSync does not change the preferred CMM setting when the preferred CMM is not available. 

## Parameters

- `cmmType`: A pointer to an `OSType`. On return, the component subtype for the preferred CMM. For example, the subtype for ColorSync’s default CMM is `'appl`' and the subtype for the Kodak CMM is `'KCMS'`. A return value of `NULL` indicates the preferred CMM in the ColorSync control panel is set to Automatic. 
- `preferredCMMnotfound`: A pointer to a Boolean flag for whether the preferred CMM was not found. On return, has the value `true` if the CMM was not found, `false` if it was found. 

## See Also

### Working With CMMs
- [CMIterateCMMInfo](./api-1805185-cmiteratecmminfo.md)
  Iterates through the color management modules installed on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805182-cmgetpreferredcmm)*