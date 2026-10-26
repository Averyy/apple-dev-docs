# EnqueueInputEntry

**Framework**: IOKit  
**Kind**: func

## Declaration

```c
IOReturn ( *EnqueueInputEntry)(
   IOStreamRef stream,
   IOStreamBufferQueueEntry *entry);
```

## See Also

### Buffer operations on streams
- [DequeueOutputEntry](./api-1810159-dequeueoutputentry.md)
  Get the next IOStreamBufferQueueEntry available from the output queue.
- [EnqueueInputBuffer](./api-1810172-enqueueinputbuffer.md)
  Send a buffer to the kernel side of the IOStream on the input queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810188-enqueueinputentry)*