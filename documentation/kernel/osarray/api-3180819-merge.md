# merge

**Framework**: Kernel  
**Kind**: instm

Appends all members of an array to this array.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual bool merge(const OSArray *otherArray);
```

#### Return_value

true on success, which retains all the added objects, or false on failure which does not retain the objects.

#### Discussion

Appends all members of an array to this array. The array capacity will be grown if necessary.

## Parameters

- `otherArray`: All members of thie array will be appended to the array.

## See Also

- [+ withArray](osarray/3180823-witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [+ withCapacity](osarray/3180824-withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [+ withObjects](osarray/3180825-withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [- free](osarray/3180811-free.md)
- [- flushCollection](osarray/3180810-flushcollection.md)
  Removes and drops references to all members of array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180819-merge)*