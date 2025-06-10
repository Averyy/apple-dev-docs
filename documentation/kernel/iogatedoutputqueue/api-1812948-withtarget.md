# withTarget(IONetworkController *, IOWorkLoop *, UInt32)

**Framework**: Kernel  
**Kind**: instm

Factory method that constructs and initializes an IOGatedOutputQueue object.

## Declaration

```swift
static IOGatedOutputQueue * withTarget(
 IONetworkController *target, 
 IOWorkLoop *workloop, 
 UInt32 capacity = 0);
```

#### Return_value

Returns an IOGatedOutputQueue object on success, or 0 otherwise.

## Parameters

- `target`: An IONetworkController object that will handle packets removed from the queue.
- `workloop`: A workloop object. An IOCommandGate object is created and added to this workloop as an event source.
- `capacity`: The initial capacity of the output queue.

## See Also

- [free](iogatedoutputqueue/1812925-free.md)
  Frees the IOGatedOutputQueue object.
- [init](iogatedoutputqueue/1812930-init.md)
  Initializes an IOGatedOutputQueue object.
- [output(IOMbufQueue *, UInt32 *)](iogatedoutputqueue/1812936-output.md)
  Transfers all packets in the mbuf queue to the target.
- [output(void *)](iogatedoutputqueue/1812941-output.md)
  Overrides the method inherited from IOOutputQueue.
- [scheduleServiceThread](iogatedoutputqueue/1812945-scheduleservicethread.md)
  Overrides the method inherited from IOOutputQueue.
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32, UInt32)](iogatedoutputqueue/1812950-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32)](iogatedoutputqueue/1812954-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32, UInt32)](iogatedoutputqueue/1812957-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogatedoutputqueue/1812948-withtarget)*