# enumerateValuesExcept(forProperties:using:)

**Framework**: iTunes Library  
**Kind**: method  
**Role**: Instance Method

Executes a provided block with the fetched values for all properties in the entity except for the provided set.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
func enumerateValuesExcept(forProperties properties: Set<String>?, using block: @escaping (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateValuesExceptForProperties:(NSSet<NSString *> *) properties usingBlock:(void (^)(NSString *property, id value, BOOL *stop)) block;
```

#### Discussion

Use this method to get property values in a batch fashion. In some cases, enumerating over a set of property keys can be more efficient than fetching each individual property with [`value(forProperty:)`](./value%28forproperty%29.md).

## Parameters

- `properties`: A set of keys for the properties to enumerate, or `nil` to enumerate all properties. Takes Media Item Properties and Playlist Properties from [`ITLibMediaItem`](../itlibmediaitem.md).
- `block`: A block object that executes for each property in the properties set.

## See Also

### Getting Media Item Properties
- [func enumerateValues(forProperties: Set<String>?, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratevalues%28forproperties,using%29.md)
  Executes a provided block with the fetched values for the item properties.
- [func value(forProperty: String) -> Any?](./value%28forproperty%29.md)
  Gets the value for a specified media property key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaentity/enumeratevaluesexcept(forproperties:using:))*