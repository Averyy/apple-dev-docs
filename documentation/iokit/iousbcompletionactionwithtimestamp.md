# IOUSBCompletionActionWithTimeStamp

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
typedef void (*IOUSBCompletionActionWithTimeStamp)(void *target, void *parameter, IOReturn status, UInt32 bufferSizeRemaining, AbsoluteTime timeStamp);
```

#### Discussion

Function called when USB I/O completes.

## Parameters

- `target`: The target specified in the IOUSBCompletion struct.
- `parameter`: The parameter specified in the IOUSBCompletion struct.
- `status`: Completion status.
- `bufferSizeRemaining`: Bytes left to be transferred.
- `timeStamp`: Time at which the transaction was processed.

## See Also

### Callbacks
- [IOUSBCompletionAction](./iousbcompletionaction.md)
- [IOUSBIsocCompletionAction](./iousbisoccompletionaction.md)
- [IOUSBLowLatencyIsocCompletionAction](./iousblowlatencyisoccompletionaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbcompletionactionwithtimestamp)*