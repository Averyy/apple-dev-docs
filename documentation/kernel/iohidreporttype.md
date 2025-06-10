# IOHIDReportType

**Framework**: Kernel  
**Kind**: tdef

Describes different type of HID reports.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef enum IOHIDReportType IOHIDReportType;
```

#### Discussion

Used by the IOHIDFamily to identify the type of report being processed.

## Topics

### Constants
- [kIOHIDReportTypeInput](iohidreporttype/kiohidreporttypeinput.md)
- [kIOHIDReportTypeOutput](iohidreporttype/kiohidreporttypeoutput.md)
- [kIOHIDReportTypeFeature](iohidreporttype/kiohidreporttypefeature.md)
- [kIOHIDReportTypeCount](iohidreporttype/kiohidreporttypecount.md)

## See Also

- [HIDReportCommandType](hidreportcommandtype.md)
- [IOHIDCompletion](iohidcompletion.md)
  Struct specifying action to perform when set/get report completes.
- [IOHIDCompletionAction](iohidcompletionaction.md)
  Function called when set/get report completes
- [IOHIDReportType](../iokit/iohidreporttype.md)
  Describes different type of HID reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidreporttype)*