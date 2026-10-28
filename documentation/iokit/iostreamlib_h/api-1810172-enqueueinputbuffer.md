# EnqueueInputBuffer

**Framework**: IOKit  
**Kind**: func

Send a buffer to the kernel side of the IOStream on the input queue.

## Declaration

```c
IOReturn ( *EnqueueInputBuffer)(
   IOStreamRef stream,
   IOStreamBufferID bufferID,
   IOByteCount dataOffset,
   IOByteCount dataLength,
   IOByteCount controlOffset,
   IOByteCount controlLength );
```

## Return Value

Returns kIOReturnSuccess if the buffer was successfully placed on the input queue.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.
- `bufferID`: The IOStreamBufferID of the buffer to place on the queue.
- `dataLength`: The length of the valid data in the buffer.

## See Also

### Buffer operations on streams
- [DequeueOutputEntry](./api-1810159-dequeueoutputentry.md)
  Get the next IOStreamBufferQueueEntry available from the output queue.
- [EnqueueInputEntry](./api-1810188-enqueueinputentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810172-enqueueinputbuffer)*