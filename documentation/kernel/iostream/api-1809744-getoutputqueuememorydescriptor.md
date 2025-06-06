# getOutputQueueMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOMemoryDescriptor *getOutputQueueMemoryDescriptor(
 void);
```

#### Return_value

An IOMemoryDescriptor object repesenting the shared memory output queue buffer.

## See Also

- [createQueues](iostream/1809702-createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by handleOpen().
- [destroyQueues](iostream/1809709-destroyqueues.md)
  Releases the shared input and output queues.
- [getInputQueue](iostream/1809718-getinputqueue.md)
- [getInputQueueMemoryDescriptor](iostream/1809727-getinputqueuememorydescriptor.md)
- [getOutputQueue](iostream/1809738-getoutputqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809744-getoutputqueuememorydescriptor)*