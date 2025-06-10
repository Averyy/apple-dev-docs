# requestCount

**Framework**: Kernel  
**Kind**: structp

The number of bytes to transfer for this frame.

**Availability**:
- macOS 10.15+

## Declaration

```swift
uint32_t requestCount;
```

#### Discussion

Set the value of this field before making an isochronous request.

## See Also

- [status](iousbisochronousframe/3294856-status.md)
  The completion status for this individual frame.
- [completeCount](iousbisochronousframe/3294854-completecount.md)
  The number of bytes that the system actually transferred for this frame.
- [reserved](iousbisochronousframe/3377598-reserved.md)
  Reserved for future use.
- [timeStamp](iousbisochronousframe/3294857-timestamp.md)
  The frame’s observed completion time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbisochronousframe/3294855-requestcount)*