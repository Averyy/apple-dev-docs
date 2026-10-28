# value(forProperty:)

**Framework**: iTunes Library  
**Kind**: method  
**Role**: Instance Method

Gets the value for a specified media property key.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
func value(forProperty property: String) -> Any?
```

```objc
- (id) valueForProperty:(NSString *) property;
```

## Return Value

The value of the specified media property key.

## Parameters

- `property`: The media property to retrieve the value from. Takes Media Item Properties and Playlist Properties from [`ITLibMediaItem`](../itlibmediaitem.md).

## See Also

### Getting Media Item Properties
- [func enumerateValues(forProperties: Set<String>?, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratevalues%28forproperties,using%29.md)
  Executes a provided block with the fetched values for the item properties.
- [func enumerateValuesExcept(forProperties: Set<String>?, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratevaluesexcept%28forproperties,using%29.md)
  Executes a provided block with the fetched values for all properties in the entity except for the provided set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaentity/value(forproperty:))*