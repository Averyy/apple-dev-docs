# ensureCapacity

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Allocates capacity for members in dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
virtual uint32_t ensureCapacity(uint32_t newCapacity);
```

*macOS*

```cpp
virtual unsigned int ensureCapacity(unsigned int newCapacity);
```

#### Return Value

New count of capacity for members in dictionary, may return prior capacity on failure.

## Parameters

- `newCapacity`: Count of allocated capacity for members in dictionary.

## See Also

### Inspecting a Dictionary
- [- getCapacity](./api-3180899-getcapacity.md)
  Returns count of currently allocated capacity for members in dictionary.
- [- getCount](./api-3180900-getcount.md)
  Returns count of members in dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180896-ensurecapacity)*