# CIPlugIn

**Framework**: Core Image  
**Kind**: cl

The mechanism for loading image units in macOS. 

**Availability**:
- macOS 10.4+

## Declaration

```swift
class CIPlugIn : NSObject
```

#### Overview

An image unit is an image processing bundle that contains one or more Core Image filters. Th`e.plugin` extension indicates one or more filters packaged as an image unit.

> **Note**: Starting in macOS 10.15, loading executable CIFilter plugins is deprecated.

Starting in macOS 10.15, loading executable CIFilter plugins is deprecated.

## Topics

### Loading Plug-ins
- [class func loadNonExecutablePlugIns()](ciplugin/1437599-loadnonexecutableplugins.md)
  Scans directories for plugins.
- [class func loadNonExecutablePlugIn(URL!)](ciplugin/3180431-loadnonexecutableplugin.md)
  Loads a non-executable plug-in specified by its URL.
### Deprecated
- [class func loadAllPlugIns()](ciplugin/1437653-loadallplugins.md)
  Scans directories for files that have the `.plugin` extension and then loads the image units.
- [class func load(URL!, allowExecutableCode: Bool)](ciplugin/1438187-load.md)
  Loads filters from an image unit that have the appropriate executable status.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class CIFilterGenerator](cifiltergenerator.md)
  An object that creates and configures chains of individual image filters. 
- [protocol CIPlugInRegistration](cipluginregistration.md)
  The interface for loading Core Image image units.
- [protocol CIFilterConstructor](cifilterconstructor.md)
  A general interface for objects that produce [`CIFilter`](cifilter.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin)*