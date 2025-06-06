# getInputQueueMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOMemoryDescriptor *getInputQueueMemoryDescriptor(
 void);
```

#### Return_value

An IOMemoryDescriptor object repesenting the shared memory input queue buffer.

## See Also

- [createQueues](iostream/1809702-createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by handleOpen().
- [destroyQueues](iostream/1809709-destroyqueues.md)
  Releases the shared input and output queues.
- [getInputQueue](iostream/1809718-getinputqueue.md)
- [getOutputQueue](iostream/1809738-getoutputqueue.md)
- [getOutputQueueMemoryDescriptor](iostream/1809744-getoutputqueuememorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809727-getinputqueuememorydescriptor)*