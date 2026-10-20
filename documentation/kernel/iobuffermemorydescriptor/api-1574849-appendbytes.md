# appendBytes

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Adds the specified data to the end of the memory buffer.

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual bool appendBytes(const void *bytes, vm_size_t withLength);
```

#### Return Value

true if the bytes were appended successfully, or false if an error occurred.

## Parameters

- `bytes`: A pointer to the bytes to add.
- `withLength`: The number of bytes in the `bytes` parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574849-appendbytes)*