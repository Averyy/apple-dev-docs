# IOUSBCompletionAction

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
typedef void (*IOUSBCompletionAction)(void *target, void *parameter, IOReturn status, UInt32 bufferSizeRemaining);
```

#### Discussion

Function called when USB I/O completes.

## Parameters

- `target`: The target specified in the IOUSBCompletion struct.
- `parameter`: The parameter specified in the IOUSBCompletion struct.
- `status`: Completion status.
- `bufferSizeRemaining`: Bytes left to be transferred.

## See Also

### Callbacks
- [IOUSBCompletionActionWithTimeStamp](./iousbcompletionactionwithtimestamp.md)
- [IOUSBIsocCompletionAction](./iousbisoccompletionaction.md)
- [IOUSBLowLatencyIsocCompletionAction](./iousblowlatencyisoccompletionaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbcompletionaction)*