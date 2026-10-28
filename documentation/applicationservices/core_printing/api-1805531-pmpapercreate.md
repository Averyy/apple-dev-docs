# PMPaperCreate

**Framework**: Application Services  
**Kind**: func

Creates a paper object.

> **Deprecated**: Use [`PMPrinterGetPaperList`](../api-1460088-pmprintergetpaperlist.md) to find the built-in papers available for a given printer or use [`PMPaperCreateCustom`](../api-1459322-pmpapercreatecustom.md) to create a custom paper.

## Declaration

```c
OSStatus PMPaperCreate (
   PMPrinter printer,
   CFStringRef id,
   CFStringRef name,
   double width,
   double height,
   const PMPaperMargins *margins,
   PMPaper *paperP
);
```

## Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

## Overview

This function creates a paper object appropriate for the specified printer. To obtain one of the available built-in paper sizes for a given printer, you should use the function [`PMPrinterGetPaperList`](../api-1460088-pmprintergetpaperlist.md).

### Special Considerations

This function creates a paper object but does not mark it as a custom paper, so it appears to the printing system as if it were a built-in paper. This can be produce unpredictable results, so this function is deprecated.

## Parameters

- `printer`: A printer object for which the paper is appropriate.
- `id`: A unique identifier for this paper.
- `name`: The name to display to the user for this paper.
- `width`: The width of the paper, in points.
- `height`: The height of the paper, in points.
- `margins`: A pointer to a [`PMPaperMargins`](../pmpapermargins.md) structure that specifies the unprintable margins of the paper, in points. The four values in the structure specify the top, left, bottom, and right imageable area margins of the paper.
- `paperP`: A pointer to your [`PMPaper`](../pmpaper.md) variable. On return, the variable refers to a new paper object with the specified attributes. You are responsible for releasing the paper object with the function [`PMRelease`](../api-1461402-pmrelease.md). The variable is set to `NULL` if the object could not be created.

## See Also

### Creating and Using Paper Objects
- [PMPaperCreateCustom](../api-1459322-pmpapercreatecustom.md)
  Creates a custom paper object.
- [PMPaperIsCustom](../api-1459526-pmpaperiscustom.md)
  Returns a Boolean value indicating whether a specified paper is a custom paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805531-pmpapercreate)*