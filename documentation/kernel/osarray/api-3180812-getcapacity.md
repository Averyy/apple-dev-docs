# getCapacity

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns count of currently allocated capacity for members in array.

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

Capacity for members in array.

## See Also

### Inspecting an Array
- [- getCount](./api-3180813-getcount.md)
  Returns count of members in array.
- [- ensureCapacity](./api-3180809-ensurecapacity.md)
  Allocates capacity for members in array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180812-getcapacity)*