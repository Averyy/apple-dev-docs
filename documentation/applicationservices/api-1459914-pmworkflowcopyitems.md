# PMWorkflowCopyItems(_:)

**Framework**: Application Services  
**Kind**: func

Obtains an array of the available PDF workflow items.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMWorkflowCopyItems(_ workflowItems: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

## Parameters

- `workflowItems`: A pointer to your   variable. On return, the variable refers to an Core Foundation array. Each element in the array is a dictionary that describes either a PDF workflow item or a folder containing a set of PDF workflow items. For a list of possible keys, see  . You are responsible for releasing the array.

## See Also

- [func PMWorkflowSubmitPDFWithOptions(CFURL, CFString?, UnsafePointer<CChar>?, CFURL) -> OSStatus](1463747-pmworkflowsubmitpdfwithoptions.md)
  Submits a PDF file for workflow processing using the specified CUPS options string.
- [func PMWorkflowSubmitPDFWithSettings(CFURL, PMPrintSettings, CFURL) -> OSStatus](1458874-pmworkflowsubmitpdfwithsettings.md)
  Submits a PDF file for workflow processing using the specified print settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459914-pmworkflowcopyitems)*