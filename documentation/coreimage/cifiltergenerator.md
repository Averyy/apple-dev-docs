# CIFilterGenerator

**Framework**: Core Image  
**Kind**: cl

An object that creates and configures chains of individual image filters. 

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CIFilterGenerator : NSObject
```

#### Overview

The [`CIFilterGenerator`](cifiltergenerator.md) class provides methods for creating a [`CIFilter`](cifilter.md) object by chaining together existing [`CIFilter`](cifilter.md) objects to create complex effects. (A  refers to the `CIFilter` objects that are connected in the `CIFilterGenerator` object.) The complex effect can be encapsulated as a [`CIFilterGenerator`](cifiltergenerator.md) object and saved as a file so that it can be used again. The  contains an archived instance  of all the `CIFilter` objects that are chained together. 

Any filter generator files that you copy to `/Library/Graphics/Image Units/` are loaded when any of the loading methods provided by the [`CIPlugIn`](ciplugin.md) class are invoked. A [`CIFilterGenerator`](cifiltergenerator.md) object is registered by its filename or, if present, by a class attribute that you supply in its description.

You can create a  [`CIFilterGenerator`](cifiltergenerator.md) object  programmatically, using the methods provided by the [`CIFilterGenerator`](cifiltergenerator.md) class, or by using the editor view provided by Core Image.

## Topics

### Initializing a Filter Generator Object
- [init?(contentsOf: URL)](cifiltergenerator/1437742-init.md)
  Initializes a filter generator object with the contents of a filter generator file.
### Connecting and Disconnecting Objects
- [func connect(Any, withKey: String?, to: Any, withKey: String)](cifiltergenerator/1438159-connect.md)
  Adds an object to the filter chain.
- [func disconnectObject(Any, withKey: String, to: Any, withKey: String)](cifiltergenerator/1438075-disconnectobject.md)
  Removes the connection between two objects in the filter chain.
### Managing Exported Keys
- [var exportedKeys: [AnyHashable : Any]](cifiltergenerator/1437955-exportedkeys.md)
  Returns an array of the exported keys.
- [func exportKey(String, from: Any, withName: String?)](cifiltergenerator/1438155-exportkey.md)
  Exports an input or output key of an object in the filter chain.
- [func removeExportedKey(String)](cifiltergenerator/1438191-removeexportedkey.md)
  Removes a key that was previously exported.
- [func setAttributes([AnyHashable : Any], forExportedKey: String)](cifiltergenerator/1438069-setattributes.md)
  Sets a dictionary of attributes for an exported key.
### Setting and Getting Class Attributes
- [var classAttributes: [AnyHashable : Any]](cifiltergenerator/1437855-classattributes.md)
  The class attributes associated with the filter.
### Archiving a Filter Generator Object
- [func write(to: URL, atomically: Bool) -> Bool](cifiltergenerator/1438179-write.md)
  Archives a filter generator object to a filter generator file.
### Registering a Filter Chain
- [func registerFilterName(String)](cifiltergenerator/1437891-registerfiltername.md)
  Registers the name associated with a filter chain. 
### Creating a Filter from a Filter Chain
- [func filter() -> CIFilter](cifiltergenerator/1438044-filter.md)
  Creates a filter object based on the filter chain.
### Constants
- [Exported Keys](cifiltergenerator/exported_keys.md)
  Keys for the exported parameters of a filter generator object.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CIFilterConstructor](cifilterconstructor.md)
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CIPlugIn](ciplugin.md)
  The mechanism for loading image units in macOS. 
- [protocol CIPlugInRegistration](cipluginregistration.md)
  The interface for loading Core Image image units.
- [protocol CIFilterConstructor](cifilterconstructor.md)
  A general interface for objects that produce [`CIFilter`](cifilter.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator)*