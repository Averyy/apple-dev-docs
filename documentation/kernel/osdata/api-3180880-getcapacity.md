# getCapacity

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns length of preallocated capacity.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
size_t getCapacity(void);
```

*macOS*

```cpp
virtual unsigned int getCapacity(void);
```

#### Return Value

length of preallocated capacity.

## See Also

### Inspecting a Data Object
- [- getLength](./api-3180881-getlength.md)
  Returns length of data present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3180880-getcapacity)*