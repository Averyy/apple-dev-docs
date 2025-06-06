# destroyQueues

**Framework**: Kernel  
**Kind**: instm

Releases the shared input and output queues.

## Declaration

```swift
virtual IOReturn destroyQueues(
 void );
```

#### Return_value

Returns kIOReturnSuccess if the queues were successfully destroyed. The queues cannot be destroyed while the stream is open by a client.

## See Also

- [createQueues](iostream/1809702-createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by handleOpen().
- [getInputQueue](iostream/1809718-getinputqueue.md)
- [getInputQueueMemoryDescriptor](iostream/1809727-getinputqueuememorydescriptor.md)
- [getOutputQueue](iostream/1809738-getoutputqueue.md)
- [getOutputQueueMemoryDescriptor](iostream/1809744-getoutputqueuememorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809709-destroyqueues)*