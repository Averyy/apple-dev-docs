# init(source:time:includeFilters:parameterID:)

**Framework**: Professional Video Applications  
**Kind**: init  
**Role**: Initializer

Initializes an `FxImageTileRequestSource`.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
init?(source requestSource: FxImageTileRequestSource, time requestTime: CMTime, includeFilters: Bool, parameterID: UInt32)
```

```objc
- (id) initWithSource:(FxImageTileRequestSource) requestSource time:(CMTime) requestTime includeFilters:(BOOL) includeFilters parameterID:(UInt32) parameterID;
```

#### Discussion

Use this method to notify the host application of the location to pull image tiles from (either the effect’s input or parameters), at what time to pull the images, and whether to include other filters.

For parameter requests, this method is used to identify the parameter.

## Parameters

- `requestSource`: The type of image input requested. Set the type to the filter’s input or one of its parameters.
- `requestTime`: The time to pull the images.
- `includeFilters`: Set to true if you request the filter input and you want it to include the output of other FxPlug-ins applied before your filter.
- `parameterID`: If the `requestSource` is `kFxImageTileRequestSourceParameter`, then this parameter holds the `parameterID`, otherwise this parameter is ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetilerequest/init(source:time:includefilters:parameterid:))*