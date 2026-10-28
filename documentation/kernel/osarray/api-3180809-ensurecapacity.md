# ensureCapacity

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Allocates capacity for members in array.

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

## Return Value

New count of capacity for members in array, may return prior capacity on failure.

## Parameters

- `newCapacity`: Count of allocated capacity for members in array.

## See Also

### Inspecting an Array
- [- getCount](./api-3180813-getcount.md)
  Returns count of members in array.
- [- getCapacity](./api-3180812-getcapacity.md)
  Returns count of currently allocated capacity for members in array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180809-ensurecapacity)*