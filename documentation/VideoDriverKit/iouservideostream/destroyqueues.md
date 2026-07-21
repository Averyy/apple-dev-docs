# destroyQueues

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t destroyQueues();
```

#### Return Value

Returns kIOReturnSuccess if the queues were successfully destroyed. The queues cannot be destroyed while the stream is open by a client.

#### Discussion

Releases the shared input and output queues.

## See Also

- [GetInputQueue](iouservideostream/getinputqueue.md)
- [GetOutputQueue](iouservideostream/getoutputqueue.md)
- [createQueues](iouservideostream/createqueues.md)
- [dequeueInputEntry](iouservideostream/dequeueinputentry.md)
- [enqueueOutputEntry](iouservideostream/enqueueoutputentry.md)
- [SendBufferQueueChange](iouservideostream/sendbufferqueuechange.md)
- [IOStreamBufferQueue](iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/destroyqueues)*