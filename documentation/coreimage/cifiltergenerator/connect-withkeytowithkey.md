# connect(_:withKey:to:withKey:)

**Framework**: Core Image  
**Kind**: method

Adds an object to the filter chain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func connect(_ sourceObject: Any, withKey sourceKey: String?, to targetObject: Any, withKey targetKey: String)
```

## Parameters

- `sourceObject`: A   object, a    object, or the path (an   or   object) to an image.
- `sourceKey`: The key that specifies the source object. For example, if the source is the output image of a filter, pass the   key. Pass   if the source object is used directly.
- `targetObject`: The object to which the source object links.
- `targetKey`: The key that specifies the target for the source. For example, if you are connecting the source to the input image of a   object, you would pass the   key.

## See Also

- [func disconnectObject(Any, withKey: String, to: Any, withKey: String)](cifiltergenerator/disconnectobject(_:withkey:to:withkey:).md)
  Removes the connection between two objects in the filter chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/connect(_:withkey:to:withkey:))*