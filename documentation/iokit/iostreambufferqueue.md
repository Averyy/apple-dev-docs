# IOStreamBufferQueue

**Framework**: IOKit  
**Kind**: tag

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
struct IOStreamBufferQueue {
    ...
};
```

## Topics

### Fields
- [entryCount](./iostreambufferqueue/api-1470527-entrycount.md)
  The number of queue entries in the queue.
- [headIndex](./iostreambufferqueue/api-1470565-headindex.md)
  The index of the next queue slot that will be filled in by the queue writer.
- [tailIndex](./iostreambufferqueue/api-1470567-tailindex.md)
  The index of the next queue slot that can be read by the queue reader.
- [reserved](./iostreambufferqueue/api-1470540-reserved.md)
  Reserved for future use.
- [queue](./iostreambufferqueue/api-1470592-queue.md)
  The array of queue entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreambufferqueue)*