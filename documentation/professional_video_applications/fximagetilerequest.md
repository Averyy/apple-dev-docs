# FxImageTileRequest

**Framework**: Professional Video Applications  
**Kind**: class  
**Role**: Class

An image tile request object that is passed between an out-of-process FxPlug plug-in and a host application.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
class FxImageTileRequest
```

```objc
@interface FxImageTileRequest : NSObject
```

## Topics

### Instance Properties
- [var includeLeadingFilters: Bool](./fximagetilerequest/includeleadingfilters.md)
  Add filters from other FxPlug-ins.
- [var parameterID: UInt32](./fximagetilerequest/parameterid.md)
  The parameter ID if the requested source is `kFxImageTileRequestSourceParameter.`
- [var requestTime: CMTime](./fximagetilerequest/requesttime.md)
  The time to pull the images.
- [var source: FxImageTileRequestSource](./fximagetilerequest/source.md)
  The type of image input requested.
### Instance Methods
- [init?(source: FxImageTileRequestSource, time: CMTime, includeFilters: Bool, parameterID: UInt32)](./fximagetilerequest/init%28source,time,includefilters,parameterid%29.md)
  Initializes an `FxImageTileRequestSource`.
### Initializers
- [init?(coder: NSCoder)](./fximagetilerequest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Exchanging Image Tiles Between Host and Plug-in
- [class FxImageTile](./fximagetile.md)
  An image tile object that is passed between an out-of-process FxPlug plug-in and a host application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetilerequest)*