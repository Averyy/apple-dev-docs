# CIFilterConstructor

**Framework**: Core Image  
**Kind**: protocol

A general interface for objects that produce filters.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIFilterConstructor
```

#### Overview

Objects implementing this protocol are called —they produce new instances of [`CIFilter`](cifilter-swift.class.md) subclasses when filters are requested by name. You can create a filter constructor to provide new, custom filters that other Core Image clients can discover using the `CIFilter` class. Normally, you create and register custom filters by packaging them as Image Units (see [`Packaging and Loading Image Units`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_image_units/ci_image_units.html#//apple_ref/doc/uid/TP30001185-CH7)), but you can use this protocol to provide new filters within your app that are compositions of existing filters.

To provide custom filters using this protocol, you must:

1. Create your custom filters as `CIFilter` subclasses.
2. Create a class that implements this protocol to vend instances of the appropriate `CIFilter` subclasses when requested.
3. Call the `CIFilter` class method [`registerName(_:constructor:classAttributes:)`](cifilter-swift.class/registername(_:constructor:classattributes:).md) for each custom filter, providing the filter’s name, an instance of your filter constructor class, and information about the filter’s attributes.

## Topics

### Providing Filter Objects
- [func filter(withName: String) -> CIFilter?](cifilterconstructor/filter(withname:).md)
  Returns a filter object specified by name.

## Relationships

### Conforming Types
- [CIFilterGenerator](cifiltergenerator.md)

## See Also

- [class CIPlugIn](ciplugin.md)
  The mechanism for loading image units in macOS.
- [class CIFilterGenerator](cifiltergenerator.md)
  An object that creates and configures chains of individual image filters.
- [protocol CIPlugInRegistration](cipluginregistration.md)
  The interface for loading Core Image image units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilterconstructor)*