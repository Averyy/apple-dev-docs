# ensureCapacity

**Framework**: Kernel  
**Kind**: instm

Allocates capacity for members in dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual unsigned int ensureCapacity(unsigned int newCapacity);
```

#### Return_value

New count of capacity for members in dictionary, may return prior capacity on failure.

## Parameters

- `newCapacity`: Count of allocated capacity for members in dictionary.

## See Also

- [- getCapacity](osdictionary/3180899-getcapacity.md)
  Returns count of currently allocated capacity for members in dictionary.
- [- getCount](osdictionary/3180900-getcount.md)
  Returns count of members in dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180896-ensurecapacity)*