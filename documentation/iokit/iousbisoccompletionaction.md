# IOUSBIsocCompletionAction

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
typedef void (*IOUSBIsocCompletionAction)(void *target, void *parameter, IOReturn status, IOUSBIsocFrame *pFrames);
```

#### Discussion

Function called when Isochronous USB I/O completes.

## Parameters

- `target`: The target specified in the IOUSBIsocCompletionn struct.
- `parameter`: The parameter specified in the IOUSBIsocCompletion struct.
- `status`: Completion status.
- `pFrames`: Pointer to the frame list containing the status for each frame transferred.

## See Also

### Callbacks
- [IOUSBCompletionAction](./iousbcompletionaction.md)
- [IOUSBCompletionActionWithTimeStamp](./iousbcompletionactionwithtimestamp.md)
- [IOUSBLowLatencyIsocCompletionAction](./iousblowlatencyisoccompletionaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbisoccompletionaction)*