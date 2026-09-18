# destroyQueues

**Framework**: VideoDriverKit  
**Kind**: method

Releases the shared input and output queues.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t destroyQueues();
```

#### Return Value

`kIOReturnSuccess` if the queues were successfully destroyed.

#### Discussion

The queues cannot be destroyed while the stream is open by a client.

## See Also

- [GetInputQueue](iouservideostream/getinputqueue.md)
  Gets the buffer queue for the stream.
- [GetOutputQueue](iouservideostream/getoutputqueue.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [createQueues](iouservideostream/createqueues.md)
  Creates the shared input and output queues, without regard to whether the stream is open or not.
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
  Sends a notification to the host that the buffer queue has changed.
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/destroyqueues)*