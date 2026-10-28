# extensionDidFinishLaunching()

**Framework**: XcodeKit  
**Kind**: method  
**Role**: Instance Method

Tells the extension that it successfully launched and may begin to receive editor commands.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func extensionDidFinishLaunching()
```

```objc
- (void) extensionDidFinishLaunching;
```

## Discussion

There are no guarantees about the thread or queue on which this method is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourceeditorextension/extensiondidfinishlaunching())*