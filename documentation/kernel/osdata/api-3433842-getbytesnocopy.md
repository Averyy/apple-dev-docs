# getBytesNoCopy

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns a pointer to the OSData object's internal data buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

*DriverKit*

```cpp
const void * getBytesNoCopy(size_t start, size_t numBytes);
```

*macOS*

```cpp
virtual const void * getBytesNoCopy(unsigned int start, unsigned int numBytes);
```

## Return Value

A pointer to the data or NULL if the OSData does not have data for all the requested range.

## Parameters

- `start`: An offset into the OSData object.
- `numBytes`: The length of data intended to be read. If (start + numBytes) exceeds the size of the OSData's length, the call will fail.

## See Also

### Getting Bytes
- [- getBytesNoCopy](./api-3180879-getbytesnocopy.md)
  Returns a pointer to the OSData object's internal data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3433842-getbytesnocopy)*