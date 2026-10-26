# IOStreamBufferQueue

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```c
struct IOStreamBufferQueue {
    ...
};
```

## Topics

### Fields
- [entryCount](./iostreambufferqueue/api-1522693-entrycount.md)
  The number of queue entries in the queue.
- [headIndex](./iostreambufferqueue/api-1522653-headindex.md)
  The index of the next queue slot that will be filled in by the queue writer.
- [tailIndex](./iostreambufferqueue/api-1522692-tailindex.md)
  The index of the next queue slot that can be read by the queue reader.
- [reserved](./iostreambufferqueue/api-1522694-reserved.md)
  Reserved for future use.
- [queue](./iostreambufferqueue/api-1522656-queue.md)
  The array of queue entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreambufferqueue)*