# PMWorkflowCopyItems(_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Obtains an array of the available PDF workflow items.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func PMWorkflowCopyItems(_ workflowItems: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

```c
OSStatus PMWorkflowCopyItems(CFArrayRef  _Nullable *workflowItems);
```

#### Return Value

A result code. See [Result Codes](./core_printing.md#1670007).

## Parameters

- `workflowItems`: A pointer to your [`CFArray`](../CoreFoundation/cfarray.md) variable. On return, the variable refers to an Core Foundation array. Each element in the array is a dictionary that describes either a PDF workflow item or a folder containing a set of PDF workflow items. For a list of possible keys, see [PDF Workflow Dictionary Keys](./core_printing/pdf_workflow_dictionary_keys.md). You are responsible for releasing the array.

## See Also

### Using PDF Workflow Items
- [func PMWorkflowSubmitPDFWithOptions(CFURL, CFString?, UnsafePointer<CChar>?, CFURL) -> OSStatus](./api-1463747-pmworkflowsubmitpdfwithoptions.md)
  Submits a PDF file for workflow processing using the specified CUPS options string.
- [func PMWorkflowSubmitPDFWithSettings(CFURL, PMPrintSettings, CFURL) -> OSStatus](./api-1458874-pmworkflowsubmitpdfwithsettings.md)
  Submits a PDF file for workflow processing using the specified print settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459914-pmworkflowcopyitems)*