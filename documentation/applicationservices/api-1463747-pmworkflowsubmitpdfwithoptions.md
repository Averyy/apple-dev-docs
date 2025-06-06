# PMWorkflowSubmitPDFWithOptions(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Submits a PDF file for workflow processing using the specified CUPS options string.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMWorkflowSubmitPDFWithOptions(_ workflowItem: CFURL, _ title: CFString?, _ options: UnsafePointer<CChar>?, _ pdfFile: CFURL) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

The printing system uses this function in conjunction with the function [`PMWorkflowCopyItems(_:)`](1459914-pmworkflowcopyitems.md) to implement the PDF workflow button in the Print dialog.

## Parameters

- `workflowItem`: A file system URL pointing to the workflow item that will handle the PDF file. See  . The following table describes the different types of workflow items for this function.
- `title`: The user-displayable name of the PDF document.
- `options`: A string of CUPS-style key-value pairs that may be passed to the PDF workflow item. This parameter can be   in which case an empty string of options is used.
- `pdfFile`: A file system URL pointing to the PDF file to be processed by the workflow item.

## See Also

- [func PMWorkflowCopyItems(UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1459914-pmworkflowcopyitems.md)
  Obtains an array of the available PDF workflow items.
- [func PMWorkflowSubmitPDFWithSettings(CFURL, PMPrintSettings, CFURL) -> OSStatus](1458874-pmworkflowsubmitpdfwithsettings.md)
  Submits a PDF file for workflow processing using the specified print settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463747-pmworkflowsubmitpdfwithoptions)*