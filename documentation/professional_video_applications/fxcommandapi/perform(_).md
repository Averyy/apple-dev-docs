# perform(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Instructs the host application to perform a command.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func perform(_ command: FxCommand) throws
```

```objc
- (BOOL) performCommand:(FxCommand) command error:(NSError * *) error;
```

## Parameters

- `command`: The command you wish the host application to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcommandapi/perform(_:))*