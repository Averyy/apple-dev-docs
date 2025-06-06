# getInputQueue

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOStreamBufferQueue *getInputQueue(
 void);
```

#### Return_value

A pointer to the input IOStreamBufferQueue structure for the stream, or NULL if the stream is not open and the queue has not been created yet.

## See Also

- [createQueues](iostream/1809702-createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by handleOpen().
- [destroyQueues](iostream/1809709-destroyqueues.md)
  Releases the shared input and output queues.
- [getInputQueueMemoryDescriptor](iostream/1809727-getinputqueuememorydescriptor.md)
- [getOutputQueue](iostream/1809738-getoutputqueue.md)
- [getOutputQueueMemoryDescriptor](iostream/1809744-getoutputqueuememorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809718-getinputqueue)*