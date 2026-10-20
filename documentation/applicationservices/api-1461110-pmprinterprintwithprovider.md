# PMPrinterPrintWithProvider(_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Submits a print job to a specified printer using a Quartz data provider to obtain the print data.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMPrinterPrintWithProvider(_ printer: PMPrinter, _ settings: PMPrintSettings, _ format: PMPageFormat?, _ mimeType: CFString, _ provider: CGDataProvider) -> OSStatus
```

```c
OSStatus PMPrinterPrintWithProvider(PMPrinter printer, PMPrintSettings settings, PMPageFormat format, CFStringRef mimeType, CGDataProviderRef provider);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

#### Discussion

This function can fail if the specified printer cannot handle the data provider’s MIME type. Use the function [`PMPrinterGetMimeTypes(_:_:_:)`](./api-1460125-pmprintergetmimetypes.md) to check whether a MIME type is supported.

##### Special Considerations

In OS X v10.4 and earlier, this function is not implemented and returns the error code –1 when called. You can write your print data to a file and use `PMPrinterPrintWithFile` instead.

## Parameters

- `printer`: The destination printer.
- `settings`: The print settings for the print job.
- `format`: The physical page size and orientation with which the document should be printed. This parameter can be `NULL`.
- `mimeType`: The MIME type of the data to be printed. This parameter cannot be `NULL`. If you want automatic typing, use the function [`PMPrinterPrintWithFile(_:_:_:_:_:)`](./api-1464600-pmprinterprintwithfile.md) instead. You can obtain a list of the MIME types supported by a given printer using the function [`PMPrinterGetMimeTypes(_:_:_:)`](./api-1460125-pmprintergetmimetypes.md).
- `provider`: The data provider that supplies the print data.

## See Also

### Submitting a Print Job to a Printer
- [func PMPrinterPrintWithFile(PMPrinter, PMPrintSettings, PMPageFormat?, CFString?, CFURL) -> OSStatus](./api-1464600-pmprinterprintwithfile.md)
  Submits a print job to a specified printer using a file that contains print data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461110-pmprinterprintwithprovider)*