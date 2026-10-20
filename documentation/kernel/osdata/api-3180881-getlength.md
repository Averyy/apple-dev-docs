# getLength

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns length of data present.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
size_t getLength(void);
```

*macOS*

```cpp
virtual unsigned int getLength(void);
```

#### Return Value

length of data present.

## See Also

### Inspecting a Data Object
- [- getCapacity](./api-3180880-getcapacity.md)
  Returns length of preallocated capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3180881-getlength)*