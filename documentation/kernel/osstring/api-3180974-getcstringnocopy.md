# getCStringNoCopy

**Framework**: Kernel  
**Kind**: instm

Returns a pointer to the OSString object's internal data buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual const char * getCStringNoCopy(void);
```

#### Return_value

A pointer to the string or NULL if the OSString has zero length. The string will be null terminated.

## See Also

- [OSStringPtr](../driverkit/osstringptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3180974-getcstringnocopy)*