# withTarget(IONetworkController *, IOWorkLoop *, UInt32, UInt32)

**Framework**: Kernel  
**Kind**: instm

Factory method that constructs and initializes an IOGatedOutputQueue object.

## Declaration

```c
static IOGatedOutputQueue * withTarget(
 IONetworkController *target, 
 IOWorkLoop *workloop, 
 UInt32capacity, 
 UInt32priorities);
```

#### Return Value

Returns an IOGatedOutputQueue object on success, or 0 otherwise.

## Parameters

- `target`: An IONetworkController object that will handle packets removed from the queue.
- `workloop`: A workloop object. An IOCommandGate object is created and added to this workloop as an event source.
- `capacity`: The initial capacity of the output queue.
- `priorities`: The number of traffic priorities supported

## See Also

### Miscellaneous
- [free](./api-1812925-free.md)
  Frees the IOGatedOutputQueue object.
- [init](./api-1812930-init.md)
  Initializes an IOGatedOutputQueue object.
- [output(IOMbufQueue *, UInt32 *)](./api-1812936-output.md)
  Transfers all packets in the mbuf queue to the target.
- [output(void *)](./api-1812941-output.md)
  Overrides the method inherited from IOOutputQueue.
- [scheduleServiceThread](./api-1812945-scheduleservicethread.md)
  Overrides the method inherited from IOOutputQueue.
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32)](./api-1812948-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32)](./api-1812954-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32, UInt32)](./api-1812957-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogatedoutputqueue/1812950-withtarget)*