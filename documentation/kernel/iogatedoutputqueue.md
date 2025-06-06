# IOGatedOutputQueue

**Framework**: Kernel  
**Kind**: cl

An extension of an IOBasicOutputQueue.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOGatedOutputQueue : IOBasicOutputQueue
```

#### Overview

An IOCommandGate object is created by this queue and added to a work loop as an event source. All calls to the target by the consumer thread must occur with the gate closed. Therefore, all calls to the target of this type of queue will be serialized with any other thread that runs on the same work loop context. This is useful for network drivers that have a tight hardware coupling between the transmit and receive engines, and a single-threaded hardware access model is desirable.

## Topics

### Miscellaneous
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
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32)](iogatedoutputqueue/1812948-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(IONetworkController *, IOWorkLoop *, UInt32, UInt32)](iogatedoutputqueue/1812950-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32)](iogatedoutputqueue/1812954-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, IOWorkLoop *, UInt32, UInt32)](iogatedoutputqueue/1812957-withtarget.md)
  Factory method that constructs and initializes an IOGatedOutputQueue object.
### Instance Methods
- [- free](iogatedoutputqueue/1485485-free.md)
- [- getMetaClass](iogatedoutputqueue/1485479-getmetaclass.md)
- [- output](iogatedoutputqueue/1485495-output.md)
- [- scheduleServiceThread](iogatedoutputqueue/1485488-scheduleservicethread.md)
### Type Methods
- [+ gatedOutput](iogatedoutputqueue/1485502-gatedoutput.md)
- [+ restartDeferredOutput](iogatedoutputqueue/1485498-restartdeferredoutput.md)
- [+ withTarget](iogatedoutputqueue/1485491-withtarget.md)
- [+ withTarget](iogatedoutputqueue/3516609-withtarget.md)

## Relationships

### Inherits From
- [IOBasicOutputQueue](iobasicoutputqueue.md)

## See Also

- [IOBasicOutputQueue](iobasicoutputqueue.md)
  A concrete implementation of an IOOutputQueue.
- [IOOutputQueue](iooutputqueue.md)
  A packet queue that supports multiple producers and a single consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogatedoutputqueue)*