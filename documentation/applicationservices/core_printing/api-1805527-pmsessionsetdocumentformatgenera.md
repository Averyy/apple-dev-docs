# PMSessionSetDocumentFormatGeneration

**Framework**: Application Services  
**Kind**: func

Requests a specified spool file format and supplies the graphics context type to use for drawing pages within the print loop.

> **Deprecated**: If you’re drawing using Quartz 2D instead of QuickDraw, use `PMSessionBeginCGDocument` or [`PMSessionBeginCGDocumentNoDialog`](../api-1460101-pmsessionbegincgdocumentnodialog.md); for submitting PostScript data, use [`PMPrinterPrintWithFile`](../api-1464600-pmprinterprintwithfile.md) or [`PMPrinterPrintWithProvider`](../api-1461110-pmprinterprintwithprovider.md); to draw EPS data, use [`PMCGImageCreateWithEPSDataProvider`](../api-1462361-pmcgimagecreatewithepsdataprovid.md).

## Declaration

```c
OSStatus PMSessionSetDocumentFormatGeneration (
   PMPrintSession printSession,
   CFStringRef docFormat,
   CFArrayRef graphicsContextTypes,
   CFTypeRef options
);
```

## Return Value

A result code. See [Result Codes](../core_printing.md#1670007).

## Overview

You only need to call the function `PMSessionSetDocumentFormatGeneration` if you want to specify a format other than the default format (PDF) or a graphics context other than the default context (QuickDraw). If you want to use the default format for the operating system and to draw with QuickDraw, then you do not need to call this function. If you want to generate PICT + PS to use as one of the supported formats, then call `PMSessionSetDocumentFormatGeneration` to set the graphics context to QuickDraw and the format to PICT + PS. Note that the PICT + PS format is not available on Intel-based systems.

If you want to use a Quartz 2D graphics context to draw each page, you can call the following code to inform the printing system in all versions of macOS. 

```occ
static OSStatus MyPMSessionBeginCGDocument (
    PMPrintSession printSession,
    PMPrintSettings printSettings,
    PMPageFormat pageFormat)
{
    OSStatus err = noErr;
 
    // Use the simpler call if it is present.
    if(&PMSessionBeginCGDocument != NULL) {
        err = PMSessionBeginCGDocument (printSession, printSettings, pageFormat);
    }
    else {
        CFStringRef s[1] = { kPMGraphicsContextCoreGraphics };
        CFArrayRef graphicsContextsArray = CFArrayCreate (
            kCFAllocatorDefault, (const void**)s, 1, &kCFTypeArrayCallBacks);
        err = PMSessionSetDocumentFormatGeneration (
            printSession, kPMDocumentFormatPDF, graphicsContextsArray, NULL);
        CFRelease (graphicsContextsArray);
        if(!err)
            err = PMSessionBeginDocument (
                printSession, printSettings, pageFormat);
    }
    return err;
}
```

The previous code informs the printing system that you want a Quartz graphics context, but you get the actual context for your printing port only after you call the function `PMSessionBeginPage` and then call the following code.

```occ
static OSStatus MyPMSessionGetCGGraphicsContext (
    PMPrintSession printSession,
    CGContextRef *printingContextP)
{
    OSStatus err = noErr;
 
    // Use the simpler call if it is present.
    if(&PMSessionGetCGGraphicsContext != NULL) {
        err = PMSessionGetCGGraphicsContext (printSession, printingContextP);
    }
    else {
        err = PMSessionGetGraphicsContext (
            printSession, kPMGraphicsContextCoreGraphics,
            (void**)printingContextP);
    }
    return err;
}
```

The printing context you get is a Quartz context into which you can draw. Note that the default coordinate system for Quartz 2D is not the same as that used for QuickDraw. Quartz 2D defines the coordinates of the lower-left corner of the sheet as (0,0) whereas the origin for the QuickDraw port is the upper-left corner of the imageable area.

You must call this function between the creation and release of a printing session. See the function [`PMCreateSession`](../api-1463247-pmcreatesession.md). You must call the function `PMSessionSetDocumentFormatGeneration` before you call PMSessionBeginDocument or [PMSessionBeginDocumentNoDialog](./api-1805538-pmsessionbegindocumentnodialog.md). Before requesting a spool file format using this function, you should call the function `PMSessionGetDocumentFormatGeneration` to get the list of supported formats.

### Special Considerations

The PICT + PS spool file format is not available on Intel-based systems.

## Parameters

- `printSession`: The printing session whose spool file format and graphics context type you want to specify.
- `docFormat`: A Core Foundation string that specifies the desired spool file format as a MIME type. See [Document Format Strings](./document_format_strings.md) for a description of the constants you can use to specify the document format.
- `graphicsContexts`: A reference to a Core Foundation array of graphics contexts to use for drawing pages within the print loop. You can supply a QuickDraw graphics context (`kPMGraphicsContextQuickDraw`) or a Quartz 2D graphics context (`kPMGraphicsContextCoreGraphics`). An array of length 1 is the only length that is supported, regardless of graphics context type. See [Graphics Context Types](./graphics_context_types.md) for a description of the constants you can use to specify a graphics context.
- `options`: Reserved for future use. 

## See Also

### Accessing Data in Printing Session Objects
- [PMSessionGetDataFromSession](../api-1462964-pmsessiongetdatafromsession.md)
  Obtains application-specific data previously stored in a printing session object.
- [PMSessionSetDataInSession](../api-1461902-pmsessionsetdatainsession.md)
  Stores your application-specific data in a printing session object.
- [PMSessionGetCurrentPrinter](../api-1458998-pmsessiongetcurrentprinter.md)
  Obtains the current printer associated with a printing session.
- [PMSessionSetCurrentPrinter](./api-1805523-pmsessionsetcurrentprinter.md)
  Changes the current printer for a printing session to a printer specified by name.
- [PMSessionSetCurrentPMPrinter](../api-1461096-pmsessionsetcurrentpmprinter.md)
  Changes the current printer for a printing session.
- [PMSessionGetDocumentFormatGeneration](./api-1805525-pmsessiongetdocumentformatgenera.md)
  Obtains the spool file formats that can be generated for the specified printing session.
- [PMSessionGetCGGraphicsContext](../api-1461952-pmsessiongetcggraphicscontext.md)
  Obtains the Quartz graphics context for the current page in a printing session.
- [PMSessionGetGraphicsContext](./api-1805529-pmsessiongetgraphicscontext.md)
  Obtains the graphics context for the current page in a printing session.
- [PMSessionError](../api-1460003-pmsessionerror.md)
  Obtains the result code for any error returned by the printing session. 
- [PMSessionSetError](../api-1460216-pmsessionseterror.md)
  Sets the value of the current result code for the specified printing session.
- [PMSessionGeneral](./api-1805530-pmsessiongeneral.md)
  Maintains compatibility with the `PrGeneral` function in the classic Printing Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/1805527-pmsessionsetdocumentformatgenera)*