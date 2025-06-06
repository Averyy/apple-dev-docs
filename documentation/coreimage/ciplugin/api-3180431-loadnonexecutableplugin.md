# loadNonExecutablePlugIn(_:)

**Framework**: Core Image  
**Kind**: clm

Loads a non-executable plug-in specified by its URL.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func loadNonExecutablePlugIn(_ url: URL!)
```

#### Discussion

If the filters contain executable code the plugin isn’t loaded.

## Parameters

- `url`: The location of the plugin to load.

## See Also

- [class func loadNonExecutablePlugIns()](ciplugin/1437599-loadnonexecutableplugins.md)
  Scans directories for plugins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin/3180431-loadnonexecutableplugin)*