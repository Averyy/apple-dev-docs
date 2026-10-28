# headIndex

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The index of the next queue slot that will be filled in by the queue writer.

**Availability**:
- macOS 10.6+

## Declaration

```c
volatile UInt32 headIndex;
```

## See Also

### Fields
- [entryCount](./api-1522693-entrycount.md)
  The number of queue entries in the queue.
- [tailIndex](./api-1522692-tailindex.md)
  The index of the next queue slot that can be read by the queue reader.
- [reserved](./api-1522694-reserved.md)
  Reserved for future use.
- [queue](./api-1522656-queue.md)
  The array of queue entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreambufferqueue/1522653-headindex)*