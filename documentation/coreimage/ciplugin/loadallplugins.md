# loadAllPlugIns()

**Framework**: Core Image  
**Kind**: method

Scans directories for files that have the `.plugin` extension and then loads the image units.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func loadAllPlugIns()
```

#### Discussion

This method scans the following directories:

- `/Library/Graphics/Image Units`
- ~`/Library/Graphics/Image Units`

Call this method once. If you call this method more than once, Core Image loads newly added image units, but image units (and the filters they contain) that are already loaded are not removed.

## See Also

- [Image Unit Tutorial](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004531)
- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [class func load(URL!, allowExecutableCode: Bool)](ciplugin/load(_:allowexecutablecode:).md)
  Loads filters from an image unit that have the appropriate executable status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin/loadallplugins())*