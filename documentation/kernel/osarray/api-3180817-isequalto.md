# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares all members of two arrays with isEqualTo().

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool isEqualTo(const OSArray *anArray);
```

*macOS*

```cpp
virtual bool isEqualTo(const OSArray *anArray);
```

#### Return Value

true if both arrays have equal counts and all members compare successfully with isEqualTo.

#### Discussion

If the arrays have equal counts, each member is compared with the other at the same index with isEqualTo(). Otherwise false is returned.

## Parameters

- `anArray`: The other array to compare with.

## See Also

### Comparing Arrays
- [- isEqualTo](./api-3433839-isequalto.md)
  Compares the array with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180817-isequalto)*