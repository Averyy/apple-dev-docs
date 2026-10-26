# parameterID

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property

The parameter ID if the requested source is `kFxImageTileRequestSourceParameter.`

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
var parameterID: UInt32 { get }
```

```objc
@property (nonatomic, readonly) UInt32 parameterID;
```

#### Discussion

If the `requestSource` is `kFxImageTileRequestSourceParameter`, then this parameter holds the `parameterID`, otherwise this parameter is ignored.

Set to `0` for effect source, otherwise the ID of the image parameter for the requested frame.` `

## See Also

### Instance Properties
- [var includeLeadingFilters: Bool](./includeleadingfilters.md)
  Add filters from other FxPlug-ins.
- [var requestTime: CMTime](./requesttime.md)
  The time to pull the images.
- [var source: FxImageTileRequestSource](./source.md)
  The type of image input requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetilerequest/parameterid)*