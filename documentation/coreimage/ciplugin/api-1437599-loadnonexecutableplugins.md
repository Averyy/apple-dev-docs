# loadNonExecutablePlugIns()

**Framework**: Core Image  
**Kind**: clm

Scans directories for plugins.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func loadNonExecutablePlugIns()
```

#### Discussion

This call scans for plugins with the extension `.plugin` in the following directories:

- /Library/Graphics/Image Units
- ~Library/Graphics/Image Units

This call adds new plug-ins. It doesn’t remove any plug-ins.

## See Also

- [class func loadNonExecutablePlugIn(URL!)](ciplugin/3180431-loadnonexecutableplugin.md)
  Loads a non-executable plug-in specified by its URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin/1437599-loadnonexecutableplugins)*