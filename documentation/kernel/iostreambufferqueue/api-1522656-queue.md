# queue

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The array of queue entries.

**Availability**:
- macOS 10.6+

## Declaration

```c
IOStreamBufferQueueEntry queue[0];
```

## See Also

### Fields
- [entryCount](./api-1522693-entrycount.md)
  The number of queue entries in the queue.
- [headIndex](./api-1522653-headindex.md)
  The index of the next queue slot that will be filled in by the queue writer.
- [tailIndex](./api-1522692-tailindex.md)
  The index of the next queue slot that can be read by the queue reader.
- [reserved](./api-1522694-reserved.md)
  Reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreambufferqueue/1522656-queue)*