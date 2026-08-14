# getLastObject

**Framework**: Kernel  
**Kind**: instm

Returns the last member of the array.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual OSObject * getLastObject(void);
```

#### Return_value

Member at the last index or NULL if array has no members.

#### Discussion

If the array has non-zero count the member at the last index is returned, with no additional retain count (the caller should not release). Otherwise NULL.

## See Also

- [- getObject](osarray/3180816-getobject.md)
  Returns a member of the array.
- [- getNextIndexOfObject](osarray/3180815-getnextindexofobject.md)
  Searches the array for an object.
- [- setObject](osarray/3180822-setobject.md)
  Appends an object as the last member of the array.
- [- setObject](osarray/3433840-setobject.md)
  Sets an object as the member of the array at a given index.
- [- iterateObjects](../driverkit/osarray/iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [- replaceObject](osarray/3180821-replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [- removeObject](osarray/3180820-removeobject.md)
  Removes a current member of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180814-getlastobject)*