# requestCount

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The number of bytes to transfer for this frame.

**Availability**:
- macOS 10.15+

## Declaration

```c
uint32_t requestCount;
```

#### Discussion

Set the value of this field before making an isochronous request.

## See Also

### Getting the Frame Properties
- [status](./api-3294856-status.md)
  The completion status for this individual frame.
- [completeCount](./api-3294854-completecount.md)
  The number of bytes that the system actually transferred for this frame.
- [reserved](./api-3377598-reserved.md)
  Reserved for future use.
- [timeStamp](./api-3294857-timestamp.md)
  The frame’s observed completion time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbisochronousframe/3294855-requestcount)*