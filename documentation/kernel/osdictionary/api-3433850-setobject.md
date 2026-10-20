# setObject

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Add or replace an object in the dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

*DriverKit*

```cpp
bool setObject(const char *aKey, const OSMetaClassBase *anObject);
```

*macOS*

```cpp
virtual bool setObject(const char *aKey, const OSMetaClassBase *anObject);
```

#### Return Value

true on success, which retains the object, or false on failure which does not retain the object.

#### Discussion

The object is added to the dictionary with the key object. If an object with the given key existed prior to the call it is replaced and released. The dictionary capacity will be grown if necessary.

## Parameters

- `aKey`: A c-string key. An OSString is created from aKey and used as the key for the dictionary.
- `anObject`: Object to be added to the dictionary.

## See Also

### Accessing Keys and Values
- [- getObject](./api-3180901-getobject.md)
  Returns a member of the dictionary.
- [- getObject](./api-3433846-getobject.md)
  Returns a member of the dictionary.
- [- setObject](./api-3180906-setobject.md)
  Add or replace an object in the dictionary.
- [- removeObject](./api-3180905-removeobject.md)
  Remove an object by key from the dictionary.
- [- removeObject](./api-3433849-removeobject.md)
  Remove an object by key from the dictionary.
- [- iterateObjects](../../DriverKit/osdictionary/iterateobjects-9h89s.md)
  Iterates the dictionary calling a callback block for each member.
- [- iterateObjects](../../DriverKit/osdictionary/iterateobjects-6cv0d.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](../../DriverKit/osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](../../DriverKit/osdictionaryiterateobjectscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3433850-setobject)*