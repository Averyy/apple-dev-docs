# getBytesNoCopy

**Framework**: Kernel  
**Kind**: instm

Returns a pointer to the OSData object's internal data buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual const void * getBytesNoCopy(void);
```

#### Return_value

A pointer to the data or NULL if the OSData has zero length.

## See Also

- [- getBytesNoCopy](osdata/3433842-getbytesnocopy.md)
  Returns a pointer to the OSData object's internal data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3180879-getbytesnocopy)*