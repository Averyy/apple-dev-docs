# CIFilterGenerator

**Framework**: Core Image  
**Kind**: class

An object that creates and configures chains of individual image filters.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CIFilterGenerator
```

#### Overview

The `CIFilterGenerator` class provides methods for creating a [`CIFilter`](cifilter-swift.class.md) object by chaining together existing `CIFilter` objects to create complex effects. (A  refers to the `CIFilter` objects that are connected in the `CIFilterGenerator` object.) The complex effect can be encapsulated as a [`CIFilterGenerator`](cifiltergenerator.md) object and saved as a file so that it can be used again. The  contains an archived instance  of all the `CIFilter` objects that are chained together.

Any filter generator files that you copy to `/Library/Graphics/Image Units/` are loaded when any of the loading methods provided by the [`CIPlugIn`](ciplugin.md) class are invoked. A `CIFilterGenerator` object is registered by its filename or, if present, by a class attribute that you supply in its description.

You can create a  `CIFilterGenerator` object  programmatically, using the methods provided by the `CIFilterGenerator` class, or by using the editor view provided by Core Image.

## Topics

### Initializing a Filter Generator Object
- [init?(contentsOf: URL)](cifiltergenerator/init(contentsof:).md)
  Initializes a filter generator object with the contents of a filter generator file.
### Connecting and Disconnecting Objects
- [func connect(Any, withKey: String?, to: Any, withKey: String)](cifiltergenerator/connect(_:withkey:to:withkey:).md)
  Adds an object to the filter chain.
- [func disconnectObject(Any, withKey: String, to: Any, withKey: String)](cifiltergenerator/disconnectobject(_:withkey:to:withkey:).md)
  Removes the connection between two objects in the filter chain.
### Managing Exported Keys
- [var exportedKeys: [AnyHashable : Any]](cifiltergenerator/exportedkeys.md)
  Returns an array of the exported keys.
- [func exportKey(String, from: Any, withName: String?)](cifiltergenerator/exportkey(_:from:withname:).md)
  Exports an input or output key of an object in the filter chain.
- [func removeExportedKey(String)](cifiltergenerator/removeexportedkey(_:).md)
  Removes a key that was previously exported.
- [func setAttributes([AnyHashable : Any], forExportedKey: String)](cifiltergenerator/setattributes(_:forexportedkey:).md)
  Sets a dictionary of attributes for an exported key.
### Setting and Getting Class Attributes
- [var classAttributes: [AnyHashable : Any]](cifiltergenerator/classattributes.md)
  The class attributes associated with the filter.
### Archiving a Filter Generator Object
- [func write(to: URL, atomically: Bool) -> Bool](cifiltergenerator/write(to:atomically:).md)
  Archives a filter generator object to a filter generator file.
### Registering a Filter Chain
- [func registerFilterName(String)](cifiltergenerator/registerfiltername(_:).md)
  Registers the name associated with a filter chain.
### Creating a Filter from a Filter Chain
- [func filter() -> CIFilter](cifiltergenerator/filter.md)
  Creates a filter object based on the filter chain.
### Constants
- [Exported Keys](exported-keys.md)
  Keys for the exported parameters of a filter generator object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CIFilterConstructor](cifilterconstructor.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CIPlugIn](ciplugin.md)
  The mechanism for loading image units in macOS.
- [protocol CIPlugInRegistration](cipluginregistration.md)
  The interface for loading Core Image image units.
- [protocol CIFilterConstructor](cifilterconstructor.md)
  A general interface for objects that produce filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator)*