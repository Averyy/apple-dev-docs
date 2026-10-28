# getCount

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns count of members in dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
virtual uint32_t getCount(void);
```

*macOS*

```cpp
virtual unsigned int getCount(void);
```

## Return Value

Count of members in dictionary.

## See Also

### Inspecting a Dictionary
- [- ensureCapacity](./api-3180896-ensurecapacity.md)
  Allocates capacity for members in dictionary.
- [- getCapacity](./api-3180899-getcapacity.md)
  Returns count of currently allocated capacity for members in dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180900-getcount)*