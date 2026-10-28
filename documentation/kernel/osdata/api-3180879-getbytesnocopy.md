# getBytesNoCopy

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns a pointer to the OSData object's internal data buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
const void * getBytesNoCopy(void);
```

*macOS*

```cpp
virtual const void * getBytesNoCopy(void);
```

## Return Value

A pointer to the data or NULL if the OSData has zero length.

## See Also

### Getting Bytes
- [- getBytesNoCopy](./api-3433842-getbytesnocopy.md)
  Returns a pointer to the OSData object's internal data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3180879-getbytesnocopy)*