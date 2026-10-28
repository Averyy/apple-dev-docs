# appendBytes

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Appends a buffer of bytes to the OSData object's internal data buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

*DriverKit*

```cpp
bool appendBytes(const OSData *aDataObj);
```

*macOS*

```cpp
virtual bool appendBytes(const OSData *aDataObj);
```

## Return Value

true on success or false on failure, due to allocation failure.

## Parameters

- `aDataObj`: An OSData object to copy all bytes from.

## See Also

### Appending Data to the Object
- [- appendBytes](../../DriverKit/osdata/appendbytes-lbqa.md)
  Appends a buffer of bytes to the OSData object's internal data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3433841-appendbytes)*