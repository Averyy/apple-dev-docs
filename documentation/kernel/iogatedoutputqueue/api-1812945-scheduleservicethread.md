# scheduleServiceThread

**Framework**: Kernel  
**Kind**: instm

Overrides the method inherited from IOOutputQueue.

## Declaration

```cpp
virtual bool scheduleServiceThread(
 void *param);
```

## Return Value

Returns true if a thread was successfully scheduled to service the queue.

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
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32)](./api-1812948-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32, UInt32)](./api-1812950-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32)](./api-1812954-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32, UInt32)](./api-1812957-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogatedoutputqueue/1812945-scheduleservicethread)*