# CIPlugInRegistration

**Framework**: Core Image  
**Kind**: intf

The interface for loading Core Image image units.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol CIPlugInRegistration
```

#### Overview

The principal class of an image unit—a loadable bundle containing custom Core Image filters for macOS—must support this protocol.

## Topics

### Initializing Plug-ins
- [func load(UnsafeMutableRawPointer!) -> Bool](cipluginregistration/1437823-load.md)
  Loads and initializes an image unit, performing custom tasks as needed.

## See Also

- [class CIPlugIn](ciplugin.md)
  The mechanism for loading image units in macOS. 
- [class CIFilterGenerator](cifiltergenerator.md)
  An object that creates and configures chains of individual image filters. 
- [protocol CIFilterConstructor](cifilterconstructor.md)
  A general interface for objects that produce [`CIFilter`](cifilter.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipluginregistration)*