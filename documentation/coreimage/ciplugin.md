# CIPlugIn

**Framework**: Core Image  
**Kind**: class

The mechanism for loading image units in macOS.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class CIPlugIn
```

#### Overview

An image unit is an image processing bundle that contains one or more Core Image filters. Th`e.plugin` extension indicates one or more filters packaged as an image unit.

> **Note**:  Starting in macOS 10.15, loading executable CIFilter plugins is deprecated.

## Topics

### Loading Plug-ins
- [class func loadNonExecutablePlugIns()](ciplugin/loadnonexecutableplugins.md)
  Scans directories for plugins.
- [class func loadNonExecutablePlugIn(URL!)](ciplugin/loadnonexecutableplugin(_:).md)
  Loads a non-executable plug-in specified by its URL.
### Deprecated
- [class func loadAllPlugIns()](ciplugin/loadallplugins.md)
  Scans directories for files that have the `.plugin` extension and then loads the image units.
- [class func load(URL!, allowExecutableCode: Bool)](ciplugin/load(_:allowexecutablecode:).md)
  Loads filters from an image unit that have the appropriate executable status.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CIFilterGenerator](cifiltergenerator.md)
  An object that creates and configures chains of individual image filters.
- [protocol CIPlugInRegistration](cipluginregistration.md)
  The interface for loading Core Image image units.
- [protocol CIFilterConstructor](cifilterconstructor.md)
  A general interface for objects that produce filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin)*