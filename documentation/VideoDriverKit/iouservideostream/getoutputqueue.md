# GetOutputQueue

**Framework**: VideoDriverKit  
**Kind**: method

Gets the memory descriptor used for video IO that was initialized with or set on the video stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
IOStreamBufferQueue * GetOutputQueue();
```

#### Return Value

A pointer to the output buffer queue for the stream, or `NULL` if the stream is not open and the queue has not been created yet.

## See Also

- [GetInputQueue](iouservideostream/getinputqueue.md)
  Gets the buffer queue for the stream.
- [createQueues](iouservideostream/createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not.
- [destroyQueues](iouservideostream/destroyqueues.md)
  Releases the shared input and output queues.
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
  Sends a notification to the host that the buffer queue has changed.
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getoutputqueue)*