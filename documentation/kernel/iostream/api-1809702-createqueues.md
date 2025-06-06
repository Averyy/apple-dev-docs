# createQueues

**Framework**: Kernel  
**Kind**: instm

Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by handleOpen().

## Declaration

```swift
virtual IOReturn createQueues(
 IOItemCount queueLength = 0,
 IOOptionBits options = 0 );
```

#### Return_value

Returns kIOReturnSuccess if the queues were successfully created.

## Parameters

- `queueLength`: 
- `options`: 

## See Also

- [destroyQueues](iostream/1809709-destroyqueues.md)
  Releases the shared input and output queues.
- [getInputQueue](iostream/1809718-getinputqueue.md)
- [getInputQueueMemoryDescriptor](iostream/1809727-getinputqueuememorydescriptor.md)
- [getOutputQueue](iostream/1809738-getoutputqueue.md)
- [getOutputQueueMemoryDescriptor](iostream/1809744-getoutputqueuememorydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809702-createqueues)*