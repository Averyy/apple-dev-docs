# createQueues

**Framework**: VideoDriverKit  
**Kind**: method

Creates the shared input and output queues, without regard to whether the stream is open or not.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t createQueues(uint32_t queueCount, uint32_t options);
```

#### Return Value

`kIOReturnSuccess` if the queues were successfully created.

#### Discussion

Normally, `IOUserVideoStream::init` calls this method.

## See Also

- [GetInputQueue](iouservideostream/getinputqueue.md)
  Gets the buffer queue for the stream.
- [GetOutputQueue](iouservideostream/getoutputqueue.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [destroyQueues](iouservideostream/destroyqueues.md)
  Releases the shared input and output queues.
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
  Sends a notification to the host that the buffer queue has changed.
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/createqueues)*