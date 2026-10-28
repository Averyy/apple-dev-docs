# destroyQueues

**Framework**: Kernel  
**Kind**: instm

Releases the shared input and output queues.

## Declaration

```cpp
virtual IOReturn destroyQueues(
 void );
```

## Return Value

Returns kIOReturnSuccess if the queues were successfully destroyed. The queues cannot be destroyed while the stream is open by a client.

## See Also

### Managing shared queues
- [createQueues](./api-1809702-createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by handleOpen().
- [getInputQueue](./api-1809718-getinputqueue.md)
- [getInputQueueMemoryDescriptor](./api-1809727-getinputqueuememorydescriptor.md)
- [getOutputQueue](./api-1809738-getoutputqueue.md)
- [getOutputQueueMemoryDescriptor](./api-1809744-getoutputqueuememorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809709-destroyqueues)*