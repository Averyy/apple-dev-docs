# IOHIDInterface::InterruptReportAction

**Framework**: Kernel  
**Kind**: tdef

Callback to handle an asynchronous report received from the HID device.

## Declaration

```swift
typedef void ( *InterruptReportAction)(
   OSObject *target,
   AbsoluteTime timestamp,
   IOMemoryDescriptor *report,
   IOHIDReportType type,
   UInt32 reportID,
   void *refcon);
```

#### Overview

This callback is set when calling IOHIDInterface::open.

## Parameters

- `target`: Pointer to your data object.
- `timestamp`: Time when the report was delivered.
- `report`: A memory descriptor that describes the report.
- `reportType`: The type of report.
- `reportID`: The ID of the report.
- `refcon`: void * pointer to more data.

## See Also

- [CompletionAction](iohidinterface/completionaction.md)
- [InterruptReportAction](iohidinterface/interruptreportaction.md)
  Callback to handle an asynchronous report received from the HID device.
- [IOHIDInterface::CompletionAction](iohidinterface/iohidinterface_completionaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidinterface/iohidinterface_interruptreportaction)*