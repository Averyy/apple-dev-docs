# createQueues

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t createQueues(uint32_t queueCount, uint32_t options);
```

#### Return Value

Returns kIOReturnSuccess if the queues were successfully created.

#### Discussion

Creates the shared input and output queues, without regard to whether the stream is open or not. Normally this is called by IOUserVideoStream::init.

## Parameters

- `options`: 

## See Also

- [GetInputQueue](iouservideostream/getinputqueue.md)
- [GetOutputQueue](iouservideostream/getoutputqueue.md)
- [destroyQueues](iouservideostream/destroyqueues.md)
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/createqueues)*