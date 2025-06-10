# status

**Framework**: Kernel  
**Kind**: structp

The completion status for this individual frame.

**Availability**:
- macOS 10.15+

## Declaration

```swift
IOReturn status;
```

#### Discussion

The system initializes this field to `kIOReturnInvalid` and updates it with a valid status code upon completion of the frame.

## See Also

- [requestCount](iousbisochronousframe/3294855-requestcount.md)
  The number of bytes to transfer for this frame.
- [completeCount](iousbisochronousframe/3294854-completecount.md)
  The number of bytes that the system actually transferred for this frame.
- [reserved](iousbisochronousframe/3377598-reserved.md)
  Reserved for future use.
- [timeStamp](iousbisochronousframe/3294857-timestamp.md)
  The frame’s observed completion time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbisochronousframe/3294856-status)*