# SendBufferQueueChange

**Framework**: VideoDriverKit  
**Kind**: method

Sends a notification to the host that the buffer queue has changed.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SendBufferQueueChange();
```

#### Return Value

`kIOReturnSuccess` if the notification was successfully sent.

#### Discussion

This will result in the user’s buffer queue changed handler being called, if they registered one.

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
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/sendbufferqueuechange)*