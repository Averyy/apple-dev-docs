# statusMessage()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the status of an encoding job.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func statusMessage() -> String!
```

```objc
- (NSString *) statusMessage;
```

## Return Value

A string indicating the status of an encoding job, or `null` if there is no update about the encoding process.

## Discussion

The following code shows an example of an encoder status message:

```objc
message = [video_encoder_extension localizedStringForKey:@"AudioEncodingInProgress"];

```

## See Also

### Providing Updates of the Encoding Process
- [func percentDone() -> Double](./percentdone%28%29.md)
  Returns the completion percentage of an encoding job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/statusmessage())*