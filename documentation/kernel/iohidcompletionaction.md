# IOHIDCompletionAction

**Framework**: Kernel  
**Kind**: tdef

Function called when set/get report completes

**Availability**:
- macOS 10.15+

## Declaration

```swift
typedef void (*IOHIDCompletionAction)(void *target, void *parameter, IOReturn status, uint32_t bufferSizeRemaining);
```

## Parameters

- `target`: The target specified in the IOHIDCompletion struct.
- `parameter`: The parameter specified in the IOHIDCompletion struct.
- `status`: Completion status

## See Also

- [IOHIDReportType](iohidreporttype.md)
  Describes different type of HID reports.
- [HIDReportCommandType](hidreportcommandtype.md)
- [IOHIDCompletion](iohidcompletion.md)
  Struct specifying action to perform when set/get report completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidcompletionaction)*