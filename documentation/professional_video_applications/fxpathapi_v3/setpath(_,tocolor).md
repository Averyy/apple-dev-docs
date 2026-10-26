# setPath(_:toColor:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the color the host app uses to draw the path with the given ID.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func setPath(_ pathID: FxPathID!, toColor newColor: FxPathColor) throws
```

```objc
- (BOOL) setPath:(FxPathID) pathID toColor:(FxPathColor) newColor error:(NSError * *) err;
```

## Parameters

- `pathID`: The ID of the path you want to draw in a different color.
- `newColor`: The FxPathColor to use to draw the path in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxpathapi_v3/setpath(_:tocolor:))*