# getCapacity

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns count of currently allocated capacity for members in dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
virtual uint32_t getCapacity(void);
```

*macOS*

```cpp
virtual unsigned int getCapacity(void);
```

## Return Value

Capacity for members in dictionary.

## See Also

### Inspecting a Dictionary
- [- ensureCapacity](./api-3180896-ensurecapacity.md)
  Allocates capacity for members in dictionary.
- [- getCount](./api-3180900-getcount.md)
  Returns count of members in dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180899-getcapacity)*