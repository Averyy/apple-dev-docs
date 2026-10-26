# source

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property

The type of image input requested.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
var source: FxImageTileRequestSource { get }
```

```objc
@property (nonatomic, readonly) FxImageTileRequestSource source;
```

#### Discussion

Set the type to the filter’s input or one of its parameters.

## See Also

### Instance Properties
- [var includeLeadingFilters: Bool](./includeleadingfilters.md)
  Add filters from other FxPlug-ins.
- [var parameterID: UInt32](./parameterid.md)
  The parameter ID if the requested source is `kFxImageTileRequestSourceParameter.`
- [var requestTime: CMTime](./requesttime.md)
  The time to pull the images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetilerequest/source)*