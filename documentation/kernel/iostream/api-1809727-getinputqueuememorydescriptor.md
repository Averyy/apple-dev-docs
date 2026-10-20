# getInputQueueMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOMemoryDescriptor *getInputQueueMemoryDescriptor(
 void);
```

#### Return Value

An IOMemoryDescriptor object repesenting the shared memory input queue buffer.

## See Also

### Managing shared queues
- [createQueues](./api-1809702-createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by handleOpen().
- [destroyQueues](./api-1809709-destroyqueues.md)
  Releases the shared input and output queues.
- [getInputQueue](./api-1809718-getinputqueue.md)
- [getOutputQueue](./api-1809738-getoutputqueue.md)
- [getOutputQueueMemoryDescriptor](./api-1809744-getoutputqueuememorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809727-getinputqueuememorydescriptor)*