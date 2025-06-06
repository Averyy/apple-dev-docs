# async

**Framework**: Core Services  
**Kind**: structdata

Requests that the application be launched asynchronously.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var async: LSLaunchFlags { get }
```

#### Discussion

The Launch Services function launching it returns control immediately without waiting for it to complete its launch sequence (indicated visually to the user when the application’s icon stops “bouncing” in the Dock).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lslaunchflags/1445037-async)*