# startTimeCodeForMedia()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the source media timecode details.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func startTimeCodeForMedia() -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) startTimeCodeForMedia;
```

#### Return Value

A dictionary with key-value pairs specifying the source media timecode information.

#### Discussion

Use this timecode information if you plan to encode the source media timecode. The dictionary has the following keys:

- **`hours`, `minutes`, `seconds`, `frames`**: Integer
- **`frameRate`**: Double
- **`isDrop`**: Bool
- **`reelName`**: NSString

## See Also

### Getting Decoding Attributes
- [func decodingAttributes() -> [AnyHashable : Any]!](./decodingattributes%28%29.md)
  Returns a set of video attributes of the decoded source media file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressormediadecoder/starttimecodeformedia())*