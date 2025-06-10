# appendBytes

**Framework**: Kernel  
**Kind**: instm

Adds the specified data to the end of the memory buffer.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool appendBytes(const void *bytes, vm_size_t withLength);
```

#### Return_value

true if the bytes were appended successfully, or false if an error occurred.

## Parameters

- `bytes`: A pointer to the bytes to add.
- `withLength`: The number of bytes in the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574849-appendbytes)*