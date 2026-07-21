# GetInputQueue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
IOStreamBufferQueue * GetInputQueue();
```

#### Return Value

A pointer to the input IOStreamBufferQueue structure for the stream, or NULL if the stream is not open and the queue has not been created yet.

## See Also

- [GetOutputQueue](iouservideostream/getoutputqueue.md)
- [createQueues](iouservideostream/createqueues.md)
- [destroyQueues](iouservideostream/destroyqueues.md)
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getinputqueue)*