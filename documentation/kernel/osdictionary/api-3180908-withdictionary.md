# withDictionary

**Framework**: Kernel  
**Kind**: clm

Allocates an OSDictionary object with given members and preallocated capacity.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
static OSPtr<OSDictionary> withDictionary(const OSDictionary *dict, unsigned int capacity);
```

#### Return_value

NULL on failure, otherwise the allocated OSDictionary with reference count 1 to be released by the caller.

## Parameters

- `dictionary`: Dictionary object containing members for the new dictionary.
- `capacity`: Count of allocated capacity for members in array.

## See Also

- [+ withCapacity](osdictionary/3180907-withcapacity.md)
  Allocates an OSDictionary object with preallocated capacity.
- [+ withObjects](osdictionary/3180909-withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [- merge](osdictionary/3180904-merge.md)
  Adds all members of a dictionary to this dictionary.
- [- free](osdictionary/3180898-free.md)
- [- flushCollection](osdictionary/3180897-flushcollection.md)
  Removes and drops references to all members of dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180908-withdictionary)*