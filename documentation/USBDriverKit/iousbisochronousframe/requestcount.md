# requestCount

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The number of bytes to transfer for this frame.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint32_t requestCount;
```

#### Discussion

Set the value of this field before making an isochronous request.

## See Also

### Getting the Frame Properties
- [status](./status.md)
  The completion status for this individual frame.
- [completeCount](./completecount.md)
  The number of bytes actually transferred for this frame.
- [reserved](./reserved.md)
  Reserved for future use.
- [timeStamp](./timestamp.md)
  The frame’s observed completion time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbisochronousframe/requestcount)*