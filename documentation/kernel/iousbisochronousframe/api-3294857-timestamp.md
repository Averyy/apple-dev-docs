# timeStamp

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The frame’s observed completion time.

**Availability**:
- macOS 10.15+

## Declaration

```c
uint64_t timeStamp;
```

## Discussion

Interrupt latency and system load may result in more than one frame completing with the same timestamp.

## See Also

### Getting the Frame Properties
- [status](./api-3294856-status.md)
  The completion status for this individual frame.
- [requestCount](./api-3294855-requestcount.md)
  The number of bytes to transfer for this frame.
- [completeCount](./api-3294854-completecount.md)
  The number of bytes that the system actually transferred for this frame.
- [reserved](./api-3377598-reserved.md)
  Reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbisochronousframe/3294857-timestamp)*