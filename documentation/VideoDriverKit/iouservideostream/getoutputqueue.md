# GetOutputQueue

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the memory descriptor used for video IO that was initialized with or set on the video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
IOStreamBufferQueue * GetOutputQueue();
```

## Return Value

A pointer to the output buffer queue for the stream, or `NULL` if the stream is not open and the queue has not been created yet.

## See Also

### Working with queues
- [GetInputQueue](./getinputqueue.md)
  Gets the buffer queue for the stream.
- [createQueues](./createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not.
- [destroyQueues](./destroyqueues.md)
  Releases the shared input and output queues.
- [dequeueInputEntry](./dequeueinputentry.md)
- [enqueueOutputEntry](./enqueueoutputentry.md)
- [SendBufferQueueChange](./sendbufferqueuechange.md)
  Sends a notification to the host that the buffer queue has changed.
- [IOStreamBufferQueue](../iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getoutputqueue)*