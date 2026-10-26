# decodingAttributes()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a set of video attributes of the decoded source media file.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func decodingAttributes() -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) decodingAttributes;
```

#### Return Value

A dictionary with key-value pairs specifying the attributes of the decoded video.

#### Discussion

The decoding attribute dictionary contains the following keys:

- **`width`**: int32_t
- **`height`**: int32_t
- **`pixelType`**: OSType
- **`pixelAspectRatio`**: Double
- **`frameRate`**: Double
- **`source-start-time-code`**: Dictionary with the following keys:

`rate` (Double)

`frameNumber` (int)

`isDropFrame` (Boolean)

- **`segment-start-time-code`**: Dictionary with the following keys:

`rate` (Double)

`frameNumber` (int)

`isDropFrame` (Boolean)

- **`segment-type`**: String with one of the following values: “only”, “first”, “middle”, “last”
- **`decoding-color-primaries`**: NCLC integer values
- **`decoding-color-transfer`**: NCLC integer values
- **`decoding-color-matrix`**: NCLC integer values

## See Also

### Getting Decoding Attributes
- [func startTimeCodeForMedia() -> [AnyHashable : Any]!](./starttimecodeformedia%28%29.md)
  Returns the source media timecode details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressormediadecoder/decodingattributes())*