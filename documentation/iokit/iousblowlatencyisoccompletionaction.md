# IOUSBLowLatencyIsocCompletionAction

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
typedef void (*IOUSBLowLatencyIsocCompletionAction)(void *target, void *parameter, IOReturn status, IOUSBLowLatencyIsocFrame *pFrames);
```

#### Discussion

Function called when Low Latency Isochronous USB I/O completes.

## Parameters

- `target`: The target specified in the IOUSBLowLatencyIsocCompletion struct.
- `parameter`: The parameter specified in the IOUSBLowLatencyIsocCompletion struct.
- `status`: Completion status.
- `pFrames`: Pointer to the low latency frame list containing the status for each frame transferred.

## See Also

### Callbacks
- [IOUSBCompletionAction](./iousbcompletionaction.md)
- [IOUSBCompletionActionWithTimeStamp](./iousbcompletionactionwithtimestamp.md)
- [IOUSBIsocCompletionAction](./iousbisoccompletionaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousblowlatencyisoccompletionaction)*