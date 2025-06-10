# scheduleServiceThread

**Framework**: Kernel  
**Kind**: instm

Overrides the method inherited from IOOutputQueue.

## Declaration

```swift
virtual bool scheduleServiceThread(
 void *param);
```

#### Return_value

Returns true if a thread was successfully scheduled to service the queue.

## See Also

- [free](iogatedoutputqueue/1812925-free.md)
  Frees the IOGatedOutputQueue object.
- [init](iogatedoutputqueue/1812930-init.md)
  Initializes an IOGatedOutputQueue object.
- [output(IOMbufQueue *, UInt32 *)](iogatedoutputqueue/1812936-output.md)
  Transfers all packets in the mbuf queue to the target.
- [output(void *)](iogatedoutputqueue/1812941-output.md)
  Overrides the method inherited from IOOutputQueue.
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32)](iogatedoutputqueue/1812948-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32, UInt32)](iogatedoutputqueue/1812950-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32)](iogatedoutputqueue/1812954-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32, UInt32)](iogatedoutputqueue/1812957-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogatedoutputqueue/1812945-scheduleservicethread)*