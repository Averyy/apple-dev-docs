# status

**Framework**: USBDriverKit  
**Kind**: property

The completion status for this individual frame.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
IOReturn status;
```

#### Discussion

The system initializes this field to `kIOReturnInvalid` and updates it with a valid status code upon completion of the frame.

## See Also

- [requestCount](iousbisochronousframe/requestcount.md)
  The number of bytes to transfer for this frame.
- [completeCount](iousbisochronousframe/completecount.md)
  The number of bytes actually transferred for this frame.
- [reserved](iousbisochronousframe/reserved.md)
  Reserved for future use.
- [timeStamp](iousbisochronousframe/timestamp.md)
  The frame’s observed completion time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbisochronousframe/status)*