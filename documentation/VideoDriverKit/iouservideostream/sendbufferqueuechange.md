# SendBufferQueueChange

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SendBufferQueueChange();
```

#### Return Value

Returns kIOReturnSuccess if the notification was successfully sent.

#### Discussion

Send a notification to the host that the buffer queue has changed. This will result in the user’s buffer queue changed handler being called, if they registered one.

## See Also

- [GetInputQueue](iouservideostream/getinputqueue.md)
- [GetOutputQueue](iouservideostream/getoutputqueue.md)
- [createQueues](iouservideostream/createqueues.md)
- [destroyQueues](iouservideostream/destroyqueues.md)
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/sendbufferqueuechange)*