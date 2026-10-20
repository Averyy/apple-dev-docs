# output(IOMbufQueue *, UInt32 *)

**Framework**: Kernel  
**Kind**: instm

Transfers all packets in the mbuf queue to the target.

## Declaration

```cpp
virtual void output(
 IOMbufQueue *queue,
 UInt32 *state);
```

## Parameters

- `queue`: A queue of output packets.
- `state`: Return a state bit defined by IOBasicOutputQueue that declares the new state of the queue following this method call. A kStateStalled is returned if the queue should stall, otherwise 0 is returned.

## See Also

### Miscellaneous
- [free](./api-1812925-free.md)
  Frees the IOGatedOutputQueue object.
- [init](./api-1812930-init.md)
  Initializes an IOGatedOutputQueue object.
- [output(void *)](./api-1812941-output.md)
  Overrides the method inherited from IOOutputQueue.
- [scheduleServiceThread](./api-1812945-scheduleservicethread.md)
  Overrides the method inherited from IOOutputQueue.
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32)](./api-1812948-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32, UInt32)](./api-1812950-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32)](./api-1812954-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32, UInt32)](./api-1812957-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogatedoutputqueue/1812936-output)*