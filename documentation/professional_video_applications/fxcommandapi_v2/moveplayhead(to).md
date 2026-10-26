# movePlayhead(to:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Moves the playhead to the desired time.

**Availability**:
- FxPlug 4.2+

## Declaration

```swift
func movePlayhead(to playheadTime: CMTime) throws
```

```objc
- (BOOL) movePlayheadToTime:(CMTime) playheadTime error:(NSError * *) error;
```

## Parameters

- `playheadTime`: The time at which you want the playhead to be positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcommandapi_v2/moveplayhead(to:))*