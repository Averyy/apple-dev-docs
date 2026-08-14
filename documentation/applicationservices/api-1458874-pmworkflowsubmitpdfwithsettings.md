# PMWorkflowSubmitPDFWithSettings(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Submits a PDF file for workflow processing using the specified print settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMWorkflowSubmitPDFWithSettings(_ workflowItem: CFURL, _ settings: PMPrintSettings, _ pdfFile: CFURL) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

The printing system uses this function in conjunction with the function [`PMWorkflowCopyItems(_:)`](1459914-pmworkflowcopyitems.md) to implement the PDF workflow button in the Print dialog.

##### 1771115

In OS X v10.4 and earlier, this function is not implemented and returns an error. You can use the function [`PMWorkflowSubmitPDFWithOptions(_:_:_:_:)`](1463747-pmworkflowsubmitpdfwithoptions.md) together with the function [`PMPrintSettingsToOptions(_:_:)`](1459069-pmprintsettingstooptions.md) instead.

## Parameters

- `workflowItem`: A file system URL pointing to the workflow item that will handle the PDF file. See [`PMWorkflowCopyItems(_:)`](1459914-pmworkflowcopyitems.md). The following table describes the different types of workflow items for this function. | Workflow item | Description |
| --- | --- |
| Automator action | The action is executed for the PDF file. Available in macOS 10.4 and later. |
| Folder alias | The PDF file is moved to the resolved folder. |
| Application or application alias | The application is sent an open event along with a reference to the PDF file. |
| Compiled AppleScript | The script is run with an open event along with a reference to the PDF file. |
| Executable tool | The tool is run with the specified settings and PDF file. This function converts these parameters into a CUPS options string and passes the options string to the tool. |
- `settings`: The print settings to apply to the PDF document. These settings are passed to the workflow item as a CUPS options string.
- `pdfFile`: A file system URL pointing to the PDF file to be processed by the workflow item.

## See Also

- [func PMWorkflowCopyItems(UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](1459914-pmworkflowcopyitems.md)
  Obtains an array of the available PDF workflow items.
- [func PMWorkflowSubmitPDFWithOptions(CFURL, CFString?, UnsafePointer<CChar>?, CFURL) -> OSStatus](1463747-pmworkflowsubmitpdfwithoptions.md)
  Submits a PDF file for workflow processing using the specified CUPS options string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1458874-pmworkflowsubmitpdfwithsettings)*