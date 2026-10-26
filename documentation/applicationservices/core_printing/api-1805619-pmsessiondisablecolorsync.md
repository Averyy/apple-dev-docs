# PMSessionDisableColorSync

**Framework**: Application Services  
**Kind**: func

Disables use of a custom ColorSync profile previously enabled by the function [PMSessionEnableColorSync](./api-1805617-pmsessionenablecolorsync.md).

> **Deprecated**: There is no replacement; draw using Quartz 2D instead.

## Declaration

```c
OSStatus PMSessionDisableColorSync (
   PMPrintSession printSession
);
```

#### Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

#### Overview

You must call the `PMSessionDisableColorSync` function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md). You must call this function within the scope of calls to the functions `PMSessionBeginPage` and `PMSessionEndPage`.

The function `PMSessionDisableColorSync` applies only to the current page. The function is useful only if the graphics context is QuickDraw and the current port is the printing port.

##### Special Considerations

This function is deprecated because QuickDraw is deprecated. When drawing with Quartz, the current stroke and fill color space and the color space associated with an image are used to characterize color. Quartz provides ways to use ColorSync profiles to create color spaces, so you can characterize color using ColorSync simply by drawing with Quartz.

## Parameters

- `printSession`: The printing session whose page-specific ColorSync profile you want to disable.

## See Also

### Matching Color With ColorSync
- [PMSetProfile](./api-1805614-pmsetprofile.md)
  Embeds a color profile during printing.
- [PMSessionEnableColorSync](./api-1805617-pmsessionenablecolorsync.md)
  Enables use of a custom ColorSync profile previously set by the function [PMSetProfile](./api-1805614-pmsetprofile.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805619-pmsessiondisablecolorsync)*