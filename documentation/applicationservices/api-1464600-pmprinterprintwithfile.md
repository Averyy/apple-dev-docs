# PMPrinterPrintWithFile(_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Submits a print job to a specified printer using a file that contains print data.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPrinterPrintWithFile(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat?, _ mimeType: CFString?, _ fileURL: CFURL) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md). If the specified printer cannot handle the file's MIME type, a non-zero error code is returned.

#### Discussion

This function can fail if the specified printer cannot handle the file’s MIME type. Use the function [`PMPrinterGetMimeTypes(_:_:_:)`](1460125-pmprintergetmimetypes.md) to check whether a MIME type is supported.

## Parameters

- `printer`: The destination printer.
- `settings`: The print settings for the print job.
- `format`: The physical page size and orientation with which the document should be printed. This parameter can be  .
- `mimeType`: The MIME type of the data to be printed. If this parameter is  , the MIME type will be determined automatically. You can obtain a list of the MIME types supported by a given printer using the function  .
- `fileURL`: The URL of the file that supplies the print data.

## See Also

- [func PMPrinterPrintWithProvider(PMPrinter, PMPrintSettings, PMPageFormat?, CFString, CGDataProvider) -> OSStatus](1461110-pmprinterprintwithprovider.md)
  Submits a print job to a specified printer using a Quartz data provider to obtain the print data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464600-pmprinterprintwithfile)*