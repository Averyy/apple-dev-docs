# getCStringNoCopy

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns a pointer to the OSString object's internal data buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
const char * getCStringNoCopy(void);
```

*macOS*

```cpp
virtual const char * getCStringNoCopy(void);
```

## Return Value

A pointer to the string or NULL if the OSString has zero length. The string will be null terminated.

## See Also

### Getting a C String
- [OSStringPtr](../../DriverKit/osstringptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3180974-getcstringnocopy)*