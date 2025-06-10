# DispatchSync

**Framework**: Kernel  
**Kind**: instm

Schedule a block for synchronous execution on the current queue.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
void DispatchSync(IODispatchBlock block);
```

#### Discussion

This method schedules the block for execution on the queue and waits for it to complete before returning. The system retains the queue until the block completes.

## Parameters

- `block`: The block to execute on the queue. 

## See Also

- [- DispatchSync_f](iodispatchqueue/3438193-dispatchsync_f.md)
  Schedule a C-style function for synchronous execution on the current queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchqueue/3438192-dispatchsync)*