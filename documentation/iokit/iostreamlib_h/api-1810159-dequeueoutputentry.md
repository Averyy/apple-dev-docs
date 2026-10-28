# DequeueOutputEntry

**Framework**: IOKit  
**Kind**: func

Get the next IOStreamBufferQueueEntry available from the output queue.

## Declaration

```c
IOReturn ( *DequeueOutputEntry)(
   IOStreamRef stream,
   IOStreamBufferQueueEntry *entry );
```

## Return Value

The IOStreamBufferID of the next available buffer, or kInvalidIOStreamBufferID if no buffer is in the queue.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.
- `entry`: A pointer to an IOStreamBufferQueueEntry structure. The next available entry from the output queue will be copied into it.

## See Also

### Buffer operations on streams
- [EnqueueInputBuffer](./api-1810172-enqueueinputbuffer.md)
  Send a buffer to the kernel side of the IOStream on the input queue.
- [EnqueueInputEntry](./api-1810188-enqueueinputentry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810159-dequeueoutputentry)*