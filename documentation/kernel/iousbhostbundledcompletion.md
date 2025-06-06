# IOUSBHostBundledCompletion

**Framework**: Kernel  
**Kind**: tag

The structure that specifies the action to perform when a bulk USB input/output request completes.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostBundledCompletion {
    ...
};
```

## Topics

### Getting the Properties
- [owner](iousbhostbundledcompletion/3230705-owner.md)
  A pointer to an object that owns the transfer.
- [action](iousbhostbundledcompletion/3230704-action.md)
  The action that executes when the input/output request completes.
- [parameter](iousbhostbundledcompletion/3230706-parameter.md)
  A context pointer within the completion action.

## See Also

- [IOUSBCompletionAction](iousbcompletionaction.md)
  A function the system calls when the USB input/output request completes.
- [IOUSBCompletion](iousbcompletion.md)
  The structure that specifies the action to perform when the USB input/output request completes.
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
- [IOUSBIsocCompletionAction](iousbisoccompletionaction.md)
  The function that executes when the isochronous USB input/output request completes.
- [IOUSBLowLatencyIsocCompletion](iousblowlatencyisoccompletion.md)
  The function that executes when the low-latency isochronous USB input/output request completes.
- [IOUSBLowLatencyIsocCompletionAction](iousblowlatencyisoccompletionaction.md)
  The function that excutes when the low-latency isochronous USB input/output request completes.
- [IOUSBCompletionActionWithTimeStamp](iousbcompletionactionwithtimestamp.md)
  The function that executes when the USB input/output request completes.
- [IOUSBCompletionWithTimeStamp](iousbcompletionwithtimestamp.md)
  A structure specifying action to perform when the USB input/output request completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostbundledcompletion)*