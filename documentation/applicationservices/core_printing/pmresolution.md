# PMResolution

**Framework**: Application Services  
**Kind**: tag

A data structure that contains printing resolution information.

## Declaration

```c
struct PMResolution {
   double hRes;
   double vRes;
};
```

## Overview

The functions [PMGetResolution](./api-1805451-pmgetresolution.md) and [PMPrinterGetPrinterResolution](./api-1805554-pmprintergetprinterresolution.md) use this structure to return printing resolution information. Your application can pass this information to the function [PMSetResolution](./api-1805452-pmsetresolution.md).

## Topics

### Fields
- [hRes](../pmresolution/api-1460032-hres.md)
  The horizontal resolution in dots per inch (dpi).
- [vRes](../pmresolution/api-1464671-vres.md)
  The vertical resolution in dots per inch (dpi).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/pmresolution)*