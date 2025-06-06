# completeCount

**Framework**: USBDriverKit  
**Kind**: property

The number of bytes actually transferred for this frame.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint32_t completeCount;
```

#### Discussion

The system updates this field upon completion of the frame.

## See Also

- [status](iousbisochronousframe/status.md)
  The completion status for this individual frame.
- [requestCount](iousbisochronousframe/requestcount.md)
  The number of bytes to transfer for this frame.
- [reserved](iousbisochronousframe/reserved.md)
  Reserved for future use.
- [timeStamp](iousbisochronousframe/timestamp.md)
  The frame’s observed completion time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbisochronousframe/completecount)*