# IOStreamBufferQueue

**Framework**: VideoDriverKit  
**Kind**: struct

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
struct IOStreamBufferQueue;
```

## Topics

### Accessing queue contents
- [entryCount](iostreambufferqueue/entrycount.md)
- [headIndex](iostreambufferqueue/headindex.md)
- [tailIndex](iostreambufferqueue/tailindex.md)
- [queue](iostreambufferqueue/queue.md)
- [IOStreamBufferQueueEntry](iostreambufferqueueentry.md)
### Accessing reserved properties
- [reserved](iostreambufferqueue/reserved.md)

## See Also

- [GetInputQueue](iouservideostream/getinputqueue.md)
  Gets the buffer queue for the stream.
- [GetOutputQueue](iouservideostream/getoutputqueue.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [createQueues](iouservideostream/createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not.
- [destroyQueues](iouservideostream/destroyqueues.md)
  Releases the shared input and output queues.
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
  Sends a notification to the host that the buffer queue has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iostreambufferqueue)*