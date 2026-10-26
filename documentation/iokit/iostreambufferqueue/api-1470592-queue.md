# queue

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

The array of queue entries.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
IOStreamBufferQueueEntry queue[0];
```

## See Also

### Fields
- [entryCount](./api-1470527-entrycount.md)
  The number of queue entries in the queue.
- [headIndex](./api-1470565-headindex.md)
  The index of the next queue slot that will be filled in by the queue writer.
- [tailIndex](./api-1470567-tailindex.md)
  The index of the next queue slot that can be read by the queue reader.
- [reserved](./api-1470540-reserved.md)
  Reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreambufferqueue/1470592-queue)*