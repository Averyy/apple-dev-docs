# setHostKeyCommands(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets host key commands.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func setHostKeyCommands(_ newCommands: [[AnyHashable : Any]]!)
```

```objc
- (void) setHostKeyCommands:(NSArray<NSDictionary *> *) newCommands;
```

## Discussion

If your plug-in displays its own custom window, you may wish to support the passing of some key presses to the application in order for the application to handle them. This method gives you a mapping from some common functions that plug-ins would like to pass on to the host application to their key commands. This method will be called whenever the user changes the key bindings for the application.

## Parameters

- `newCommands`: An array of dictionaries mapping FxCommands to keys and modifiers. Each element of the array is an NSDictionary containing 3 key-value pairs for the keys: kKey_Command, kKey_Character, and kKey_Modifiers. Note that if a command does not have a key equivalent assigned in the host application, the kKey_Character key will have a value of 0. Each application may implement only a subset of the desired commands. Furthermore, there may be more than one key combination assigned to a given function. You should support all of them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcommandhandler/sethostkeycommands(_:))*