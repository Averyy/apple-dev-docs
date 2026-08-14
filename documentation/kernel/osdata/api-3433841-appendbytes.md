# appendBytes

**Framework**: Kernel  
**Kind**: instm

Appends a buffer of bytes to the OSData object's internal data buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool appendBytes(const OSData *aDataObj);
```

#### Return_value

true on success or false on failure, due to allocation failure.

## Parameters

- `aDataObj`: An OSData object to copy all bytes from.

## See Also

- [- appendBytes](../driverkit/osdata/appendbytes-lbqa.md)
  Appends a buffer of bytes to the OSData object's internal data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3433841-appendbytes)*