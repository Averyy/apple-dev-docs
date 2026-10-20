# isEqualTo

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Compares certain members of two dictionaries with isEqualTo().

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool isEqualTo(const OSDictionary *aDictionary, const OSCollection *keys);
```

*macOS*

```cpp
virtual bool isEqualTo(const OSDictionary *aDictionary, const OSCollection *keys);
```

#### Return Value

true if both dictionaries have equal counts, every key exists in both, values for each key compare true with isEqualTo().

#### Discussion

For each key in the given collection, both dictionaries must contain values for the key that compare successfully with isEqualTo().

## Parameters

- `aDictionary`: The other dictionary to compare with.

## See Also

### Comparing Dictionaries
- [- isEqualTo](./api-3433847-isequalto.md)
  Compares all members of two dictionaries with isEqualTo().
- [- isEqualTo](./api-3433848-isequalto.md)
  Compares the dictionary with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180902-isequalto)*