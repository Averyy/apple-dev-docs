# requestCount

**Framework**: USBDriverKit  
**Kind**: property

The number of bytes to transfer for this frame.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint32_t requestCount;
```

#### Discussion

Set the value of this field before making an isochronous request.

## See Also

- [status](iousbisochronousframe/status.md)
  The completion status for this individual frame.
- [completeCount](iousbisochronousframe/completecount.md)
  The number of bytes actually transferred for this frame.
- [reserved](iousbisochronousframe/reserved.md)
  Reserved for future use.
- [timeStamp](iousbisochronousframe/timestamp.md)
  The frame’s observed completion time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbisochronousframe/requestcount)*