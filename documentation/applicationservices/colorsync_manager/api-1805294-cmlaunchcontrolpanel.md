# CMLaunchControlPanel

**Framework**: Application Services  
**Kind**: func

Launches the ColorSync preferences pane.

## Declaration

```c
CMError CMLaunchControlPanel (
   UInt32 flags
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

When your application calls the function `CMLaunchControlPanel`, any changes made by the user will not be available (through calls such as `CMGetDefaultProfileBySpace`) until the user closes the ColorSync preferences pane. There is currently no ColorSync function that determines if the ColorSync preferences pane has been closed, but you can use the Process Manager API for this purpose. 

## Parameters

- `flags`: A value that specifies how the preferences pane is launched. You currently must pass a value of 0 for this parameter.

## See Also

### Miscellaneous
- [CMGetColorSyncVersion](./api-1805293-cmgetcolorsyncversion.md)
  Gets ColorSync version information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805294-cmlaunchcontrolpanel)*