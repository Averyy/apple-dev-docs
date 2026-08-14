# setObject

**Framework**: Kernel  
**Kind**: instm

Sets an object as the member of the array at a given index.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual bool setObject(unsigned int index, const OSMetaClassBase *anObject);
```

#### Return_value

true on success, which retains the object, or false on failure which does not retain the object.

#### Discussion

Sets an object as the member of the array at a given index. The array capacity will be grown if necessary.

## Parameters

- `index`: Zero based index less than or equal to the array count to add the object.
- `anObject`: Object to be added to the array.

## See Also

- [- getObject](osarray/3180816-getobject.md)
  Returns a member of the array.
- [- getLastObject](osarray/3180814-getlastobject.md)
  Returns the last member of the array.
- [- getNextIndexOfObject](osarray/3180815-getnextindexofobject.md)
  Searches the array for an object.
- [- setObject](osarray/3180822-setobject.md)
  Appends an object as the last member of the array.
- [- iterateObjects](../driverkit/osarray/iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [- replaceObject](osarray/3180821-replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [- removeObject](osarray/3180820-removeobject.md)
  Removes a current member of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3433840-setobject)*