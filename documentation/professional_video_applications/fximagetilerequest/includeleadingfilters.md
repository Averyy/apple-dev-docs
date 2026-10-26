# includeLeadingFilters

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property

Add filters from other FxPlug-ins.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
var includeLeadingFilters: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL includeLeadingFilters;
```

#### Discussion

Set to true if you request the filter input and you want it to include the output of other FxPlugs applied before your filter. Each tile is pre-processed by filters higher in the processing order.

## See Also

### Instance Properties
- [var parameterID: UInt32](./parameterid.md)
  The parameter ID if the requested source is `kFxImageTileRequestSourceParameter.`
- [var requestTime: CMTime](./requesttime.md)
  The time to pull the images.
- [var source: FxImageTileRequestSource](./source.md)
  The type of image input requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetilerequest/includeleadingfilters)*