# CMGetColorSyncVersion

**Framework**: Application Services  
**Kind**: func

Gets ColorSync version information.

## Declaration

```c
CMError CMGetColorSyncVersion (
   UInt32 *version
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

`CMGetColorSyncVersion` relieves you from having to call `Gestalt` to find out the version of ColorSync installed on the system. 

## Parameters

- `version`: On output, points to the version of ColorSync installed on the system.

## See Also

### Miscellaneous
- [CMLaunchControlPanel](./api-1805294-cmlaunchcontrolpanel.md)
  Launches the ColorSync preferences pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805293-cmgetcolorsyncversion)*