# createQueues

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Creates the shared input and output queues, without regard to whether the stream is open or not.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t createQueues(uint32_t queueCount, uint32_t options);
```

## Return Value

`kIOReturnSuccess` if the queues were successfully created.

## Discussion

Normally, [`init`](./init.md) calls this method.

## See Also

### Working with queues
- [GetInputQueue](./getinputqueue.md)
  Gets the buffer queue for the stream.
- [GetOutputQueue](./getoutputqueue.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [destroyQueues](./destroyqueues.md)
  Releases the shared input and output queues.
- [dequeueInputEntry](./dequeueinputentry.md)
- [enqueueOutputEntry](./enqueueoutputentry.md)
- [SendBufferQueueChange](./sendbufferqueuechange.md)
  Sends a notification to the host that the buffer queue has changed.
- [IOStreamBufferQueue](../iostreambufferqueue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/createqueues)*