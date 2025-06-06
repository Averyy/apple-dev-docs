# IOUSBIsocCompletionAction

**Framework**: Kernel  
**Kind**: tdef

The function that executes when the isochronous USB input/output request completes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef void (*IOUSBIsocCompletionAction)(void *target, void *parameter, IOReturn status, IOUSBIsocFrame *pFrames);
```

## Parameters

- `target`: The target that the   structure specifies.
- `parameter`: The parameter that the   structure specifies.
- `status`: The completion status.
- `pFrames`: A pointer to the frame list containing the status for each frame that transfers.

## See Also

- [IOUSBCompletionAction](iousbcompletionaction.md)
  A function the system calls when the USB input/output request completes.
- [IOUSBCompletion](iousbcompletion.md)
  The structure that specifies the action to perform when the USB input/output request completes.
- [IOUSBHostBundledCompletion](iousbhostbundledcompletion.md)
  The structure that specifies the action to perform when a bulk USB input/output request completes.
- [IOUSBHostBundledCompletionAction](iousbhostbundledcompletionaction.md)
  The function description for a USB host bundled completion action.
- [IOUSBHostCompletion](iousbhostcompletion.md)
  The structure that specifies the action to perform when the USB input/output request completes.
- [IOUSBHostCompletionAction](iousbhostcompletionaction.md)
  The function description for a USB host completion action.
- [IOUSBHostIsochronousCompletion](iousbhostisochronouscompletion.md)
  A structure describing the completion callback for an asynchronous isochronous operation.
- [IOUSBHostIsochronousCompletionAction](iousbhostisochronouscompletionaction.md)
  The function description for a USB host isochronous completion action.
- [IOUSBIsocCompletion](iousbisoccompletion.md)
  A structure specifying the action to perform when an isochronous USB input/output operation completes.
- [IOUSBLowLatencyIsocCompletion](iousblowlatencyisoccompletion.md)
  The function that executes when the low-latency isochronous USB input/output request completes.
- [IOUSBLowLatencyIsocCompletionAction](iousblowlatencyisoccompletionaction.md)
  The function that excutes when the low-latency isochronous USB input/output request completes.
- [IOUSBCompletionActionWithTimeStamp](iousbcompletionactionwithtimestamp.md)
  The function that executes when the USB input/output request completes.
- [IOUSBCompletionWithTimeStamp](iousbcompletionwithtimestamp.md)
  A structure specifying action to perform when the USB input/output request completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbisoccompletionaction)*