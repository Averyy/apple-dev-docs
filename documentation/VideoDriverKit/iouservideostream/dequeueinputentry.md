# dequeueInputEntry

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t dequeueInputEntry(IOStreamBufferQueueEntry *entry);
```

## Parameters

- `entry`: 

## See Also

### Working with queues
- [GetInputQueue](./getinputqueue.md)
  Gets the buffer queue for the stream.
- [GetOutputQueue](./getoutputqueue.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [createQueues](./createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not.
- [destroyQueues](./destroyqueues.md)
  Releases the shared input and output queues.
- [enqueueOutputEntry](./enqueueoutputentry.md)
- [SendBufferQueueChange](./sendbufferqueuechange.md)
  Sends a notification to the host that the buffer queue has changed.
- [IOStreamBufferQueue](../iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/dequeueinputentry)*