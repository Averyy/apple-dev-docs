# timeStamp

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The frame’s observed completion time.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint64_t timeStamp;
```

## Discussion

Interrupt latency and system load may result in more than one frame completing with the same timestamp.

## See Also

### Getting the Frame Properties
- [status](./status.md)
  The completion status for this individual frame.
- [requestCount](./requestcount.md)
  The number of bytes to transfer for this frame.
- [completeCount](./completecount.md)
  The number of bytes actually transferred for this frame.
- [reserved](./reserved.md)
  Reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbisochronousframe/timestamp)*