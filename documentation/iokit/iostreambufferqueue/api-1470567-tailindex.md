# tailIndex

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

The index of the next queue slot that can be read by the queue reader.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
volatile UInt32 tailIndex;
```

## See Also

### Fields
- [entryCount](./api-1470527-entrycount.md)
  The number of queue entries in the queue.
- [headIndex](./api-1470565-headindex.md)
  The index of the next queue slot that will be filled in by the queue writer.
- [reserved](./api-1470540-reserved.md)
  Reserved for future use.
- [queue](./api-1470592-queue.md)
  The array of queue entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreambufferqueue/1470567-tailindex)*