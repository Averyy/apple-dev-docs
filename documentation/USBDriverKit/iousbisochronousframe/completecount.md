# completeCount

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The number of bytes actually transferred for this frame.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint32_t completeCount;
```

## Discussion

The system updates this field upon completion of the frame.

## See Also

### Getting the Frame Properties
- [status](./status.md)
  The completion status for this individual frame.
- [requestCount](./requestcount.md)
  The number of bytes to transfer for this frame.
- [reserved](./reserved.md)
  Reserved for future use.
- [timeStamp](./timestamp.md)
  The frame’s observed completion time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbisochronousframe/completecount)*