# IOHIDInterface::CompletionAction

**Framework**: Kernel  
**Kind**: tdef

## Declaration

```swift
typedef void ( *CompletionAction)(
   OSObject *target,
   void *refcon,
   IOReturn status,
   UInt32 bufferSizeRemaining);
```

#### Overview

Function called when HID I/O completes.

## Parameters

- `target`: 
- `refcon`: 
- `status`: Completion status.
- `bufferSizeRemaining`: Bytes left to be transferred.

## See Also

- [CompletionAction](iohidinterface/completionaction.md)
- [InterruptReportAction](iohidinterface/interruptreportaction.md)
  Callback to handle an asynchronous report received from the HID device.
- [IOHIDInterface::InterruptReportAction](iohidinterface/iohidinterface_interruptreportaction.md)
  Callback to handle an asynchronous report received from the HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidinterface/iohidinterface_completionaction)*