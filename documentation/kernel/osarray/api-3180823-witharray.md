# withArray

**Framework**: Kernel  
**Kind**: clm

Allocates an OSArray object with given members and preallocated capacity.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
static OSPtr<OSArray> withArray(const OSArray *array, unsigned int capacity);
```

#### Return_value

NULL on failure, otherwise the allocated OSArray with reference count 1 to be released by the caller.

## Parameters

- `array`: Array object containing members for the new array.
- `capacity`: Count of allocated capacity for members in array.

## See Also

- [+ withCapacity](osarray/3180824-withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [+ withObjects](osarray/3180825-withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [- merge](osarray/3180819-merge.md)
  Appends all members of an array to this array.
- [- free](osarray/3180811-free.md)
- [- flushCollection](osarray/3180810-flushcollection.md)
  Removes and drops references to all members of array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180823-witharray)*