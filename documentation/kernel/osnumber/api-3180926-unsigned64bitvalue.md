# unsigned64BitValue

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns the value of the OSNumber as a uint64_t value.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
uint64_t unsigned64BitValue(void);
```

*macOS*

```cpp
virtual unsigned long long unsigned64BitValue(void);
```

#### Return Value

Returns the value of the OSNumber as a uint64_t value.

## See Also

### Getting Integer Values
- [- unsigned8BitValue](./api-3180927-unsigned8bitvalue.md)
  Returns the value of the OSNumber as a uint8_t value.
- [- unsigned16BitValue](./api-3180924-unsigned16bitvalue.md)
  Returns the value of the OSNumber as a uint16_t value.
- [- unsigned32BitValue](./api-3180925-unsigned32bitvalue.md)
  Returns the value of the OSNumber as a uint32_t value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osnumber/3180926-unsigned64bitvalue)*