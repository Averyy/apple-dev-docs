# timeStamp

**Framework**: USBDriverKit  
**Kind**: property

The frame’s observed completion time.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint64_t timeStamp;
```

#### Discussion

Interrupt latency and system load may result in more than one frame completing with the same timestamp.

## See Also

- [status](iousbisochronousframe/status.md)
  The completion status for this individual frame.
- [requestCount](iousbisochronousframe/requestcount.md)
  The number of bytes to transfer for this frame.
- [completeCount](iousbisochronousframe/completecount.md)
  The number of bytes actually transferred for this frame.
- [reserved](iousbisochronousframe/reserved.md)
  Reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbisochronousframe/timestamp)*