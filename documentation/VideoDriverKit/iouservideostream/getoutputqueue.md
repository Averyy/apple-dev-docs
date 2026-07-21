# GetOutputQueue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
IOStreamBufferQueue * GetOutputQueue();
```

#### Return Value

Returns IOMemoryDescriptor in an OSSharedPtr.

#### Discussion

Get the IOMemoryDescriptor used for video IO that was initialied with or set on the video stream

```None
@function getOutputQueue
@result A pointer to the output IOStreamBufferQueue structure for the stream,
or NULL if the stream is not open and the queue has not been created yet.
```

## See Also

- [GetInputQueue](iouservideostream/getinputqueue.md)
- [createQueues](iouservideostream/createqueues.md)
- [destroyQueues](iouservideostream/destroyqueues.md)
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getoutputqueue)*