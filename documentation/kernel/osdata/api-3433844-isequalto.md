# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares the data with a pointer to bytes

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

*DriverKit*

```cpp
bool isEqualTo(const void *bytes, size_t numBytes);
```

*macOS*

```cpp
virtual bool isEqualTo(const void *bytes, unsigned int numBytes);
```

#### Return Value

true iff the length of the data are equal and all bytes are identical.

#### Discussion

If the passed data has the same length and all bytes are identical, true is returned. Otherwise false is returned.

## Parameters

- `bytes`: C-pointer to untyped data.
- `numBytes`: Count of bytes to be compared.

## See Also

### Comparing Data Objects
- [- isEqualTo](./api-3180882-isequalto.md)
  Compares the data with an OSData
- [- isEqualTo](./api-3433843-isequalto.md)
  Compares the data with an OSString
- [- isEqualTo](./api-3433858-isequalto.md)
  Compares the data with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3433844-isequalto)*