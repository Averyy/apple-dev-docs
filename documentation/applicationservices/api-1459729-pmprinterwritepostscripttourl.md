# PMPrinterWritePostScriptToURL(_:_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Converts an input file of the specified MIME type to printer-ready PostScript for a destination printer.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func PMPrinterWritePostScriptToURL(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat?, _ mimeType: CFString?, _ sourceFileURL: CFURL, _ destinationFileURL: CFURL) -> OSStatus
```

#### Return_value

A result code. If the printing system cannot convert the input MIME type to PostScript, this function fails and returns an error.

#### Discussion

This function is synchronous; the conversion of the input file to PostScript is performed before the function returns. This can take a significant amount of time for longer documents. You may want to perform this operation on a thread other than the main application thread or fork a separate process for this purpose.

## Parameters

- `printer`: The destination printer for which printer-ready PostScript will be generated.
- `settings`: The print settings for the print job.
- `format`: The page format specifying the physical page size and orientation on which the document should be printed.
- `mimeType`: The MIME type of the file to be printed. If you pass  , the file is typed automatically. You can obtain a list of the MIME types supported by a given printer using the function  .
- `sourceFileURL`: A URL specifying the input file to be converted to printer-ready PostScript data. Only file-based URLs are supported.
- `destinationFileURL`: A URL specifying the destination file to be created. If the file already exists, it will be overwritten. Only file-based URLs are supported.

## See Also

- [func PMCGImageCreateWithEPSDataProvider(CGDataProvider?, CGImage) -> Unmanaged<CGImage>?](1462361-pmcgimagecreatewithepsdataprovid.md)
  Creates an image that references both the PostScript contents of EPS data and a preview (proxy) image for the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459729-pmprinterwritepostscripttourl)*